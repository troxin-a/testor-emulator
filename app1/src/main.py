from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.admin import AdminAuth, LogAdmin, UserAdmin
from config.settings import settings
from api.base import base_router
from api.users import users_router
from sqladmin import Admin
from config.db import engine


app = FastAPI(**settings.model_dump())

# Все для админки
admin = Admin(app=app, engine=engine, authentication_backend=AdminAuth(settings.jwt.secret_key, settings.jwt.algoritm))
admin.add_view(UserAdmin)
admin.add_view(LogAdmin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=("GET", "POST"),
    allow_headers=["*"],
)

app.include_router(base_router)
app.include_router(users_router)
