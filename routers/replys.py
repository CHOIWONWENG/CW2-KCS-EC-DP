from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.replys import Replys
from fastapi.responses import RedirectResponse

router = APIRouter()
reply_list = []

templates = Jinja2Templates(directory='templates/')