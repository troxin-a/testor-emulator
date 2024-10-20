from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from api.base import base_router
from api.users import users_router


app = FastAPI(**settings.model_dump())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=("GET", "POST"),
    allow_headers=["*"],
)

app.include_router(base_router)
app.include_router(users_router)
