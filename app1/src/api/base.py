from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from models.users import User
from schemas.logs import LogHistory
from schemas.query import QueryForServer
from schemas.users import Token
from services.integration import get_logs, send_coords
from services.users import get_access_token, get_current_active_user

base_router = APIRouter(prefix="")


@base_router.get("/ping", summary="Проверка на доступность", tags=["Base"])
async def index():
    return True


@base_router.post(
    "/query",
    summary="Отправить запрос",
    description="Отправляет запрос на сторонний сервер, в ответ True или False.",
    tags=["Base"],
)
async def query(
    query_data: QueryForServer,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> bool | dict:
    return await send_coords(query_data, db)


@base_router.get(
    "/history",
    summary="История запросов",
    description="При вводе необязательного параметра number, происходит фильтрация по кадастровому номеру",
    response_model=List[LogHistory],
    tags=["Base"],
)
async def get_history(
    number: str | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await get_logs(db, number)


@base_router.post(
    "/token",
    summary="Получить Bearer токен",
    tags=["Users"],
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
) -> Token:
    access_token = await get_access_token(db, form_data)
    return Token(access_token=access_token, token_type="bearer")
