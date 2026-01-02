from typing import Dict, Any

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def dict(self) -> Dict[str, Any]:
        return {key: value for key, value in self.__dict__.items() if not key.startswith("_") is not None}
