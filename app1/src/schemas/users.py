import re
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


class CreateUser(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[$%&!:])(?=.{8,})[A-Za-z\d$%&!:]*$"
        if not re.match(pattern, v):
            raise ValueError(
                """Пароль должен быть не менее 8 символов, только латиница, минимум 1 цифра, минимум 1 символ верхнего регистра, минимум 1 спец символ ($%&!:)."""
            )
        return v


class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
