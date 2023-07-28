from fastapi import APIRouter, Body, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from beanie import PydanticObjectId 
from fastapi.templating import Jinja2Templates
from database.connection import Database
from models.otas import OTA

router = APIRouter(
    tags=['OTAs']
)
ota_database = Database(OTA)  # MongoDB collection 객체

templates = Jinja2Templates(directory='templates/')

@router.get('/', status_code=status.HTTP_200_OK)
async def createPage(request: Request):
    otas = await ota_database.get_all()
    return templates.TemplateResponse(
        "createOTA.html",
        {
            "request": request,
            "otas": otas
        }
    )

@router.get('/{ota_id}', status_code=status.HTTP_200_OK)
async def detailPage(ota_id: PydanticObjectId, request: Request):
    ota = await ota_database.get(ota_id)
    if not ota:
        return templates.TemplateResponse(
            "otaDetail.html",
            {
                "request": request,
                "ota": None
            }
        )
    else:
        return templates.TemplateResponse(
            "otaDetail.html",
            {
                "request": request,
                "ota": ota
            }
        )

@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_otas(ota: OTA = Body(...)):
    await ota_database.save(ota)
    return RedirectResponse(url="http://localhost:8000/")


@router.delete('/{ota_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_ota(ota_id: PydanticObjectId):
    result = ota_database.delete(ota_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return None
    


@router.get('/{ota_id}/add', status_code=status.HTTP_202_ACCEPTED)
async def add_count(ota_id: str):
    ota = await ota_database.get(ota_id)
    if not ota:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    ota.memberCount += 1
    await ota_database.save(ota)
    return None

@router.get('/{ota_id}/sub', status_code=status.HTTP_202_ACCEPTED)
async def sub_count(ota_id: PydanticObjectId):
    ota = await ota_database.get(ota_id)
    if not ota:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if ota.memberCount > 1:
        ota.memberCount -= 1
        await ota_database.save(ota)
    return None

# from fastapi import APIRouter, HTTPException, status, Request, Depends
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import RedirectResponse
# from pymongo.collection import Collection
# from bson import ObjectId

# router = APIRouter()
# ota_list = Collection

# templates = Jinja2Templates(directory='templates/')

# @router.post('/', status_code=status.HTTP_201_CREATED)
# async def add_otas(otas: OTA = Depends(OTA.as_form)):
#     otas.id = len(ota_list) + 1
#     ota_list.append(otas)
#     return RedirectResponse(url="http://localhost:8000/")

# @router.get('/', status_code=status.HTTP_200_OK)
# async def createPage(request: Request):
#     return templates.TemplateResponse(
#         "createOTA.html",
#         {
#             "request": request,
#             "otas": ota_list
#         }
#     )

# @router.get('/{ota_id}', status_code=status.HTTP_200_OK)
# async def detailPage(request: Request, ota_id: int):
#     for ota in ota_list:
#         if ota.id == ota_id:
#             return templates.TemplateResponse(
#                 "otaDetail.html",
#                 {
#                     "request": request,
#                     "ota": ota
#                     }
#                     )
#         else:
#             return templates.TemplateResponse(
#                 "otaDetail.html",
#                 {
#                     "request": request,
#                     "ota": None
#                     }
#                     )

# @router.delete('/{ota_id}', status_code=status.HTTP_202_ACCEPTED)
# async def delete_ota(ota_id: int):
#     for index in range(len(ota_list)):
#         if ota_list[index].id == ota_id:
#             ota_list.pop(index)
#             return None  
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND
#         )
# @router.get('/{ota_id}/add', status_code=status.HTTP_202_ACCEPTED)
# async def add_count(ota_id: int):
#     for index in range(len(ota_list)):
#         if ota_list[index].id == ota_id:
#             ota_list[index].memberCount += 1
#             return None  
#     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
        

# @router.get('/{ota_id}/sub', status_code=status.HTTP_202_ACCEPTED)
# async def sub_count(ota_id: int):
#     for index in range(len(ota_list)):
#         if ota_list[index].id == ota_id:
#             if ota_list[index].memberCount > 1:
#                 ota_list[index].memberCount -= 1
#             return None  
#     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)



