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


router = APIRouter(prefix="/location", tags=["location"])
templates = Jinja2Templates(directory="./templates")


@router.get('/catalogue',response_class=HTMLResponse )
def catalogue_location(request: Request,  user: UserSchema = Depends(login_manager.optional)):
       if user is not None :
          if user.blocked == True:
            return templates.TemplateResponse(
            "blockedRedirect.html",
            context={'request': request, 'current_user' : user})
    
       cars = services.get_all_car_for_location()
       number_cars = str(len(cars))
       return templates.TemplateResponse(
        "catalogue.html",
        context={'request': request, 'cars': cars, 'number_cars' : number_cars, 'current_user' : user,'extra':'location'}
    )





