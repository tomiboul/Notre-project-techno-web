from uuid import uuid4
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas.users import UserSchema
from pydantic import ValidationError
from app.login_manager import login_manager
from app.services.achat import get_id_car


router = APIRouter(prefix="/autres", tags=["Autres"])
templates = Jinja2Templates(directory="./templates")


@router.get('/home')
def home(request : Request, user:UserSchema = Depends(login_manager.optional)):  
    return templates.TemplateResponse('home.html', context={'request':request, 'current_user':user})

@router.get('/paiement/{id}')
def paiement(request : Request, id:str,user:UserSchema = Depends(login_manager.optional)):
    car = get_id_car(id)
    return templates.TemplateResponse('paiement.html' ,context={"request":request, "user":user, 'car':car})

@router.post('/paiement/{id}')
def paiement(request : Request, id:str, adresse:Annotated[str,Form()], titulaire:Annotated[str, Form()], numero:Annotated[str, Form()], pays:Annotated[str, Form()], date:Annotated[str, Form()], user:UserSchema = Depends(login_manager.optional)):
    #rien n'est pour l'instant fait avec les coordonnées bancaires et le paiement
    return RedirectResponse('/achat/catalogue', status_code=302)