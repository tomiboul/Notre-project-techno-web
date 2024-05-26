from uuid import uuid4
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from app.schemas.users import UserSchema
from app import login_manager
from app.login_manager import login_manager
import app.services.location as services
from app.services.location import get_all_car_for_location
from app.login_manager import login_manager
from app.services.achat import get_all_car_for_sale, get_id_car
from app.services.autres import get_all_car_by_keyword


router = APIRouter(prefix="/location", tags=["location"])
templates = Jinja2Templates(directory="./templates")


@router.get('/catalogue',response_class=HTMLResponse)
def catalogue(request:Request, user:UserSchema = Depends(login_manager.optional)):
    cars = get_all_car_for_location()
    return templates.TemplateResponse('location.html', context={'request':request,'user':user,'cars':cars,'extra':'location', 'number_cars':len(cars)})

@router.get("/fiche/{car_id}",response_class=HTMLResponse)
def fiche(request : Request, car_id:str ,user:UserSchema=Depends(login_manager.optional)):
    car = get_id_car(car_id)
    return templates.TemplateResponse('fichedescriptive.html',context={"request":request,"car":car, "user":user})

@router.post("/catalogue/search")
def search(request:Request, keyword:Annotated[str,Form()], user:UserSchema=Depends(login_manager.optional)):
    cars = get_all_car_by_keyword(keyword, "location")

    return templates.TemplateResponse('search.html', context={"request":request, "user":user, "extra":"location", 'cars':cars,'number_cars':len(cars)})

