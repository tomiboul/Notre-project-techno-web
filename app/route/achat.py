
from uuid import uuid4
from typing import Annotated
from app.schemas.users import UserSchema
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from app.login_manager import login_manager
from app.services.achat import get_all_car_for_sale, get_id_car


router = APIRouter(prefix="/achat", tags=["Achat"])
templates = Jinja2Templates(directory="./templates")


@router.get('/catalogue',response_class=HTMLResponse)
def catalogue(request:Request, user:UserSchema = Depends(login_manager.optional)):
    cars = get_all_car_for_sale()
    return templates.TemplateResponse('catalogue.html', context={'request':request,'current_user':user,'cars':cars,'extra':'vente', 'number_cars':len(cars)})

@router.get("/fiche/{car_id}",response_class=HTMLResponse)
def fiche(request : Request, car_id:str ,user:UserSchema=Depends(login_manager.optional)):
    car = get_id_car(car_id)
    return templates.TemplateResponse('fichedescriptive.html',context={"request":request,"car":car, "current_user":user})