from pydantic import BaseModel
from typing import Union
from fastapi import Form
from datetime import datetime

class Replys(BaseModel):
    id: Union[int, None] = None #   Optional[int] = None
    createdAt: datetime = datetime.now()
    content: str
    authorName: str
    passwd: str

    @classmethod
    def as_form(
        cls,
        content: str = Form(...),
        authorName: str = Form(...),
        passwd: str = Form(...),
    ):
        return cls(content=content, authorName=authorName,
                   passwd=passwd)