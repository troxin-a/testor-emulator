from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from config.db import Base


class User(Base):
    email: Mapped[str]
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True, server_default=text("'false'"))
