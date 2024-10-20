from typing import List
import aiohttp
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.logs import Log
from schemas.logs import LogHistory
from schemas.query import QueryForServer


async def write_log(log: Log, db: AsyncSession) -> None:
    """Пишет переданный лог в базу."""

    db.add(log)
    await db.commit()


async def send_coords(query_data: QueryForServer, db: AsyncSession) -> bool:
    """Отправляет координаты на сторонний API."""

    data = query_data.model_dump()

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post("http://app2:8000/result", json=data) as response:
                response = await response.json()
        except aiohttp.ClientConnectionError:
            response = {"message": "Второй сервер не отвечает"}
        except aiohttp.ClientError as e:
            response = {"message from app2": e.message}
        else:
            data["response"] = response
            await write_log(Log(**data), db)

    return response


async def get_logs(db: AsyncSession) -> List[LogHistory]:
    """Получает историю запросов к стороннему API с результатом."""

    query = select(Log)
    response = await db.execute(query)

    logs = response.scalars().all()
    return logs
