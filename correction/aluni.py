from typing import Optional, List
from pydantic import BaseModel


class Alumni(BaseModel):
    name: str
    lastname: str
    age: int
    hobbies: Optional[List[str]] = None