from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pymongo.collection import Collection
from bson import ObjectId

router = APIRouter()
ota_collection = Collection  # MongoDB collection 객체

templates = Jinja2Templates(directory='templates/')

@router.get('/')
@router.post('/')
@router.delete('/')
async def mainPage(request: Request):
    otas = await ota_collection.find().to_list(length=None)
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "otas": otas
        }
    )