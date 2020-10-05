from pydantic import BaseModel
from typing import List, Optional


class Student(BaseModel):
    name: str
    age: int
    sex: bool  # True women - False man
    hobbies: Optional[List[str]]

