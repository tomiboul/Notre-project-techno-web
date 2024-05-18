from uuid import uuid4
from typing import Annotated
from app.services.voiture import get_all_car_for_rent
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from app.schemas.users import UserSchema
from app import login_manager
from app.login_manager import login_manager
import app.services.location as services


router = APIRouter(prefix="/forum", tags=["forum"])
templates = Jinja2Templates(directory="./templates")

@router.get('/questions',response_class=HTMLResponse )
def questionnement(request: Request,  user: UserSchema = Depends(login_manager.optional)):
       
        if user.blocked == True:
            return templates.TemplateResponse(
            "blockedRedirect.html",
            context={'request': request, 'current_user' : user})


