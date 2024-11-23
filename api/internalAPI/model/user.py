from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    age: int
    address: str
    joining_date: str
    is_registered: bool

    
