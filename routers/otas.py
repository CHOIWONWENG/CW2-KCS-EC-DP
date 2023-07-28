from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.otas import OTA, OTAItem
from fastapi.responses import RedirectResponse

router = APIRouter()
ota_list = []

templates = Jinja2Templates(directory='templates/')

@router.post('/')
async def add_otas(otas: OTA = Depends(OTA.as_form)):
    otas.id = len(ota_list) + 1
    ota_list.append(otas)
    return RedirectResponse(url="http://localhost:8000/")

@router.get('/')
async def retrieve_otas(request: Request):
    return templates.TemplateResponse(
        "createOTA.html",
        {
            "request": request,
            "otas": ota_list
        }
    )

@router.get('/{ota_id}')
async def retrieve_otas(request: Request, ota_id: int):
    for ota in ota_list:
        if ota.id == ota_id:
            return templates.TemplateResponse(
                "otaDetail.html",
                {
                    "request": request,
                    "ota": ota
                    }
                    )
        else:
            return templates.TemplateResponse(
                "otaDetail.html",
                {
                    "request": request,
                    "ota": None
                    }
                    )

@router.delete('/{ota_id}')
async def delete_ota(ota_id: int):
    for index in range(len(ota_list)):
        if ota_list[index].id == ota_id:
            ota_list.pop(index)
            break  # 테이블을 찾았으니 더 이상 순회할 필요가 없음
    return RedirectResponse(url="http://localhost:8000/")

@router.delete('/{ota_id}')
async def delete_ota(ota_id: int):
    for index in range(len(ota_list)):
        if ota_list[index].id == ota_id:
            ota_list.pop(index)
            return RedirectResponse(url="http://localhost:8000/")
    return RedirectResponse(url="http://localhost:8000/")
