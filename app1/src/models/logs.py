from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from config.db import Base


class Log(Base):
    cadastral_number: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    time_request: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    response: Mapped[bool]
