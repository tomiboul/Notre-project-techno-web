from uuid import uuid4
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas.users import UserSchema
from pydantic import ValidationError
from app.login_manager import login_manager
from app.services.achat import get_id_car, car_sold
from app.services.autres import get_all_avis, save_avis
from app.schemas.avis import avisSchema


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
    car_sold(id)
    return RedirectResponse('/achat/catalogue', status_code=302)

@router.get('/contact', response_class=HTMLResponse)
def contact(request:Request, user:UserSchema=Depends(login_manager.optional)):
    return templates.TemplateResponse('contact.html', context={"request":request,"current_user":user})

@router.get('/entretien', response_class=HTMLResponse)
def entretien(request: Request, user:UserSchema=Depends(login_manager.optional)):
    return templates.TemplateResponse('entretien.html', context={"request":request, "current_user":user})

@router.post('/entretien')
def entretien_rendezvous(request:Request, date:Annotated[str, Form()], email:Annotated[str,Form()], heure:Annotated[str,Form()],user:UserSchema=Depends(login_manager.optional)) :
    
    return RedirectResponse('/autres/home', status_code=302)
    
@router.get('/avis')
def getAvisListe(request: Request, user:UserSchema=Depends(login_manager.optional)):
    avis = get_all_avis()
    align = [0,0,0,0]
    return templates.TemplateResponse('avis.html', context={"request":request,"current_user":user, "avis":avis, "align":align})

@router.get('/ecrireavis')
def avis(request: Request, user:UserSchema=Depends(login_manager.optional)):
    avis = get_all_avis()
    align = [0,0,0,0]
    return templates.TemplateResponse('ecrireavis.html', context={"request":request,"current_user":user, "avis":avis, "align":align})

@router.post('/ecrireavis')
def avis(request: Request, rating:Annotated[str,Form()], avis:Annotated[str,Form()], user:UserSchema=Depends(login_manager.optional)):
    new_avis = avisSchema(avisId=str(uuid4()), idUser= user.id, rating= rating, avis = avis)
    save_avis(new_avis)
    return RedirectResponse('/avis',status_code=302)