from pydantic import BaseModel
from typing import Union, List
from fastapi import Form
from datetime import datetime

class OTA(BaseModel):
    id: Union[int, None] = None #   Optional[int] = None
    createdAt: datetime = datetime.now()
    title: str
    authorName: str
    storeName: str
    memberCount: int = 1

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        authorName: str = Form(...),
        storeName: str = Form(...),
    ):
        return cls(title=title, authorName=authorName,
                   storeName=storeName)
