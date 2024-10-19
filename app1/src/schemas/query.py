import re
from pydantic import BaseModel, confloat, field_validator


class QueryForServer(BaseModel):
    cadastral_number: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)

    @field_validator("cadastral_number")
    @classmethod
    def validate_cadastral_number(cls, v):
        pattern = r"^(?!:)[0-9:]*(?<!:)$"
        if not re.match(pattern, v):
            raise ValueError(
                "Кадастровый номер должен начинаться и заканчиваться на цифру и может содержать только цифры и двоеточия"
            )
        return v
