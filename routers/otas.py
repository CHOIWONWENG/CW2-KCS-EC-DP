from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.otas import OTA
from fastapi.responses import RedirectResponse

router = APIRouter()
ota_list = []

templates = Jinja2Templates(directory='templates/')

@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_otas(otas: OTA = Depends(OTA.as_form)):
    otas.id = len(ota_list) + 1
    ota_list.append(otas)
    return RedirectResponse(url="http://localhost:8000/")

@router.get('/', status_code=status.HTTP_200_OK)
async def createPage(request: Request):
    return templates.TemplateResponse(
        "createOTA.html",
        {
            "request": request,
            "otas": ota_list
        }
    )

@router.get('/{ota_id}', status_code=status.HTTP_200_OK)
async def detailPage(request: Request, ota_id: int):
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

@router.delete('/{ota_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_ota(ota_id: int):
    for index in range(len(ota_list)):
        if ota_list[index].id == ota_id:
            ota_list.pop(index)
            return None  
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
        )
@router.get('/{ota_id}/add', status_code=status.HTTP_202_ACCEPTED)
async def add_count(ota_id: int):
    for index in range(len(ota_list)):
        if ota_list[index].id == ota_id:
            ota_list[index].memberCount += 1
            return None  
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
        

@router.get('/{ota_id}/sub', status_code=status.HTTP_202_ACCEPTED)
async def sub_count(ota_id: int):
    for index in range(len(ota_list)):
        if ota_list[index].id == ota_id:
            if ota_list[index].memberCount > 1:
                ota_list[index].memberCount -= 1
            return None  
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)



