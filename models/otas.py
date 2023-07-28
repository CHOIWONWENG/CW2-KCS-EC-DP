from pydantic import BaseModel
from typing import Union, List
from fastapi import Form
from datetime import datetime
from models.replys import Replys

class OTA(BaseModel):
    id: Union[int, None] = None #   Optional[int] = None
    createdAt: datetime = datetime.now()
    createdAt: datetime
    title: str
    authorName: str
    storeName: str
    replys: List[Replys] = None

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        authorName: str = Form(...),
        storeName: str = Form(...),
    ):
        return cls(title=title, authorName=authorName,
                   storeName=storeName)

class OTAItem(BaseModel):
    title: str
    storeName: str
