from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    telefone: str