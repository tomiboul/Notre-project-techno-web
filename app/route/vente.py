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

@router.get ('/client',response_class=HTMLResponse)
def get_car_sale(request: Request,user:UserSchema=Depends(login_manager.optional)):
    if user is not None:
        return templates.TemplateResponse("vente.html",context={"request":request,'current_user':user})
    else :
        return templates.TemplateResponse("exceptions.html", context={'request':request, 'status_code':400,'message':'Le service de vente n\'est pas disponible pour les utilisateurs non connectés'})
    
    
@router.get('/particulier',response_class=HTMLResponse)
def get_vente_partic(request:Request, user:UserSchema=Depends(login_manager.optional)) :
    return templates.TemplateResponse('ventePartic.html', context={'request':request, 'current_user':user})

@router.get('/professionnel')
def get_vente_professionnel(request:Request,user:UserSchema=Depends(login_manager.optional)):
    return templates.TemplateResponse('venteProfess.html',context={'request':request,'current_user':user})

@router.post('/professionnel')
def get_vente_professionnel(request:Request,user:UserSchema=Depends(login_manager.optional)):
    pass