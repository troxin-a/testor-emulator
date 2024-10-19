from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from config.settings import settings
from schemas.logs import LogHistory
from schemas.query import QueryForServer
from services.integration import get_logs, send_coords


app = FastAPI(**settings.model_dump())


@app.get(
    "/ping",
    summary="Проверка на доступность",
)
async def index():
    return True


@app.post(
    "/query",
    summary="Отправить запрос",
    description="Отправляет запрос на сторонний сервер, в ответ True или False.",
)
async def query(query_data: QueryForServer, db: AsyncSession = Depends(get_db)) -> bool | dict:
    return await send_coords(query_data, db)


@app.get("/history")
async def get_history(db: AsyncSession = Depends(get_db)) -> List[LogHistory]:
    return await get_logs(db)
