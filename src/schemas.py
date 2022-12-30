from pydantic import BaseModel
from typing import Optional

class user(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    telefone: str