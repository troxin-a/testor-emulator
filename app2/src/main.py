import asyncio
from random import choice, randint
from fastapi import FastAPI

from schemas.coords import Coords


app = FastAPI()


@app.post("/")
async def index(coords: Coords):

    await asyncio.sleep(randint(0, 5))  # Рекламная пауза

    return choice([True, False])
