from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from config.db import Base


class Log(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cadastral_number: Mapped[str]
    latitude: Mapped[str]
    longitude: Mapped[str]
    time_request: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    response: Mapped[bool]
