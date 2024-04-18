from uuid import uuid4
from typing import Annotated
from app.schemas.users import UserSchema
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from app.login_manager import login_manager


router = APIRouter(prefix="/vente", tags=["Vente"])
templates = Jinja2Templates(directory="./templates")

@router.get ('/vente',response_class=HTMLResponse)
def get_voiture_sale(request: Request,user:UserSchema=Depends(login_manager)):
    if user is None:
        raise HTTPException(status_code=404,detail="you're not connected")
    else:
        return templates.TemplateResponse("voiture_sale.html",{"request":request,})
    
    
@router.get('/voiture{id}',response_class=HTMLResponse)
def get_voiture_détail( request:Request , id:str):
    #voiture_détail=
    if user is None:
        raise HTTPException(status_code=404,detail="car not found")
    else:
        return templates.TemplateResponse("voiture_détail.html",{"request":request,})