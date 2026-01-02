from pydantic import BaseModel


class WebAppAuthRequest(BaseModel):
    initData: str

import datetime
import json
from typing import Optional

from pydantic import BaseModel, field_validator

class UserSchema(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    language_code: str
    allows_write_to_pm: bool
    photo_url: Optional[str]


class WebAppInitDataResponse(BaseModel):
    query_id: str
    user: UserSchema
    auth_date: datetime.datetime
    signature: str

    @field_validator("user", mode="before")
    @classmethod
    def validate_user(cls, value: str) -> UserSchema:
        data = json.loads(value)
        return UserSchema(**data)
