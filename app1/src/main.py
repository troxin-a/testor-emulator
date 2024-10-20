from fastapi import FastAPI
from config.settings import settings
from api.base import base_router
from api.users import users_router


app = FastAPI(**settings.model_dump())

app.include_router(base_router)
app.include_router(users_router)
