from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    telephone: str

    class Config:
        orm_mode = True