
from uuid import uuid4
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
#from app.login_manager import login_manager


router = APIRouter(prefix="/achat", tags=["Achat"])
templates = Jinja2Templates(directory="./templates")
