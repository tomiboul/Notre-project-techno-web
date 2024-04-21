from uuid import uuid4
from typing import Annotated
from app.schemas.users import UserSchema
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from app.login_manager import login_manager
from app.schemas.voiture import CarSchema

router = APIRouter(prefix="/vente", tags=["Vente"])
templates = Jinja2Templates(directory="./templates")

@router.get ('/client',response_class=HTMLResponse)
def get_car_sale(request: Request,user:UserSchema=Depends(login_manager.optional)):
    if user is not None:
        return templates.TemplateResponse("vente.html",context={"request":request,'current_user':user})
    else :
        return templates.TemplateResponse("exceptions.html", context={'request':request, 'status_code':400,'message':'Le service de vente n\'est pas disponible pour les utilisateurs non connectés','current_user':user})
    
    
@router.get('/particulier',response_class=HTMLResponse)
def get_vente_partic(request:Request, user:UserSchema=Depends(login_manager.optional)) :
    return templates.TemplateResponse('ventePartic.html', context={'request':request, 'current_user':user})

@router.post('/particulier')
def vente_partic(request:Request, modele: Annotated[str,Form()], marque:Annotated[str,Form()],description:Annotated[str,Form()],date_fabrication:Annotated[str,Form()],image:Annotated[str,Form()],prix:Annotated[str,Form()], user:UserSchema=Depends(login_manager.optional)):
    new_car_for_sale = CarSchema(id=str(uuid4()),
                                 nomModel=modele,
                                 marque=marque,
                                 description=description,
                                 date_fabrication=date_fabrication,
                                 etat='vente',
                                 image=image,
                                 prix=prix,
                                 proprietaire_id=user.id)
    save_car_for_sale(new_car_for_sale)
    return RedirectResponse('/achat/catalogue')

@router.get('/professionnel')
def get_vente_professionnel(request:Request,user:UserSchema=Depends(login_manager.optional)):
    return templates.TemplateResponse('venteProfess.html',context={'request':request,'current_user':user})

@router.post('/professionnel')
def get_vente_professionnel(request:Request,user:UserSchema=Depends(login_manager.optional)):
    pass

