from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import jwt
from models.logs import Log
from models.users import User
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from sqladmin import ModelView

from config.db import async_session_maker

from services.users import get_access_token


class AdminAuth(AuthenticationBackend):

    def __init__(self, secret_key, algoritm):
        super().__init__(secret_key)
        self.secret_key = secret_key
        self.algoritm = algoritm

    async def login(self, request: Request) -> bool:
        form = await request.form()
        form_data = OAuth2PasswordRequestForm(username=form["username"], password=form["password"])

        async with async_session_maker() as db:
            token = await get_access_token(db, form_data=form_data)
            request.session.update({"token": token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        payload = jwt.decode(token, key=self.secret_key, algorithms=[self.algoritm])
        username: str = payload.get("sub")

        # Ну здесь захардкодим. Хорошего помаленьку :)
        if username != "admin@admin.ru":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Только admin@admin.ru может войти",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return True


class UserAdmin(ModelView, model=User):
    """Модель Пользователь для отображения в админке"""

    name_plural = "Пользователи"
    column_list = [User.id, User.email, User.is_active]
    column_searchable_list = [User.email]
    column_labels = {
        User.email: "Email",
        User.is_active: "Активирован",
    }

    page_size = 50
    page_size_options = [25, 50, 100, 200]
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class LogAdmin(ModelView, model=Log):
    """Модель Запросы для отображения в админке"""

    name_plural = "Запросы"
    column_list = [Log.cadastral_number, Log.latitude, Log.longitude, Log.response]
    column_labels = {
        Log.cadastral_number: "Кадастровый номер",
        Log.latitude: "Широта",
        Log.longitude: "Долгота",
        Log.response: "Ответ сервера",
    }

    column_searchable_list = [Log.cadastral_number]

    page_size = 50
    page_size_options = [25, 50, 100, 200]
    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True
