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
from app.services.location import save_response
from app.schemas.question import questionSchema

router = APIRouter(prefix="/forum", tags=["Forum"])
templates = Jinja2Templates(directory="./templates")

@router.get('/questions',response_class=HTMLResponse )
def questionnement(request: Request,  user: UserSchema = Depends(login_manager.optional)):
    questions= services.get_all_questions()
    return templates.TemplateResponse("forum.html", context={'request': request, 'user':user,'questions':questions})

@router.post('/questions',response_class=HTMLResponse)
def post_question(request: Request, userquestion: Annotated[str, Form()], user : UserSchema=Depends(login_manager.optional)):
    if user is not None:
        data = questionSchema(id=str(uuid4()), userId = user.id, question= userquestion, reponse ="")


        services.save_question(data)
        return RedirectResponse(url='./questions',status_code=status.HTTP_303_SEE_OTHER)
    
@router.post('/reponse/{questionId}')
def repondre(request:Request, questionId:str,reponse:Annotated[str,Form()], user:UserSchema=Depends(login_manager.optional)):
    save_response(reponse, questionId)

    return RedirectResponse('/forum/questions',status_code=302)

