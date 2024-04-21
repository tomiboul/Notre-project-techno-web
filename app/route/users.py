from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Depends, Body, Request, Form
from fastapi.templating import Jinja2Templates
from app.login_manager import login_manager
from app.services.users import get_user_by_email, get_all_users
from app.schemas.users import UserSchema
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import ValidationError
from fastapi.responses import RedirectResponse
import app.services.users as services
import hashlib

router = APIRouter(prefix="/users", tags=["Users"])
templates = Jinja2Templates(directory="./templates")

@router.get("/login", response_class=HTMLResponse)
def login_route_demande(request: Request, user:UserSchema =Depends(login_manager.optional)):
    return templates.TemplateResponse(
        "login.html",
        context={'request': request, 'current_user':user}
    )

@router.post("/login")
def login_route(
        request : Request,
        email: Annotated[str, Form()],
        password: Annotated[str, Form()],
        user:UserSchema=Depends(login_manager.optional)
):
    encoded_password = password.encode()
    hashed_password = hashlib.sha3_256(encoded_password).hexdigest()
    
    user = get_user_by_email(email)
   
    if user is None or user.hashed_password != hashed_password:
        return templates.TemplateResponse('exceptions.html', context={'request':request, 'status_code':401,'current_user':user, 'message':'L\'adresse email ou le mot de passe n\'est pas bon'})
        

    
    access_token = login_manager.create_access_token(
        data={'sub': user.id}
    )
    
    response = RedirectResponse('/autres/home', status_code = 302)
    response.set_cookie(
        key=login_manager.cookie_name,
        value=access_token,
        httponly=True
    )
    return response



@router.get('/logout')
def ask_logout(request : Request, user: UserSchema = Depends(login_manager.optional)) :
    return templates.TemplateResponse(
        'logout.html',
        context = {'request': request, 'current_user':user}
    )

@router.post('/logout')
def logout_route():
    response =  RedirectResponse(
        '/users/login',
        status_code = 302
    )
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
    return response


@router.get("/me")
def current_user_route(
    request : Request,
    user: UserSchema = Depends(login_manager),
):
    return templates.TemplateResponse(
        "profil.html",
        context={'request':request,"current_user":user}
    )
    

@router.get('/signin')
def signin_ask(request : Request, user:UserSchema=Depends(login_manager.optional)):
    return templates.TemplateResponse(
        "signin.html",
        context = {'request': request, 'current_user':user}
    )

@router.post('/signin')
def signin(request : Request, name : Annotated[str, Form()], firstname: Annotated[str, Form()], email: Annotated[str, Form()], phone: Annotated[str, Form()], adresse : Annotated[str,Form()], password: Annotated[str, Form()], confirmedpassword: Annotated[str, Form()], user:UserSchema=Depends(login_manager.optional)) :
    if not (name == "" or firstname =="" or email =="" or password=="" or confirmedpassword =="") :
        if get_user_by_email(email) is None :
            if not (confirmedpassword != password) :
                encoded_password = password.encode()
                hashed_password = hashlib.sha3_256(encoded_password).hexdigest()
                new_user_data = {
                    "id" : str(uuid4()),
                    "email" : email,
                    "name" : name,
                    "firstname" : firstname,
                    "hashed_password" : hashed_password,
                    "admin" : False,
                    "phone" : phone,
                    "adresse" : adresse,
                    "blocked" : False
                }
                try:
                    user_data = UserSchema.model_validate(new_user_data)
                except ValidationError:
                    status_code=status.HTTP_400_BAD_REQUEST
                    detail="informations invalides pour le nouvel utilisateur"
                    return templates.TemplateResponse('exceptions.html', context={'request':request, 'status_code': 400, 'message': 'Les informations ne sont pas valides', 'redir':'inscription'})
                    
                services.save_user(user_data)
                return RedirectResponse(url="/users/login", status_code=302)
            else :
                return templates.TemplateResponse('exceptions.html', context={'request':request, 'status_code': 400, 'message': 'Les deux mots de passe ne correspondent pas', 'redir':'inscription'})
        else :
            return templates.TemplateResponse('exceptions.html', context={'request': request, 'status_code': 400, 'message': 'L\'adresse email spécifiée est déjà inscrite', 'redir': 'inscription'})
    else :
        return templates.TemplateResponse('exceptions.html', context={'request': request, 'status_code': 400, 'message': 'Tous les champs n\'ont pas été renseignés', 'redir': 'inscription'})

@router.get('/users_list')
def get_user_list(request : Request, user: UserSchema = Depends(login_manager)) :
    if user.blocked == False:
        if user.admin == True :
            users = services.get_all_users()
            number_users=str(len(users))
            return templates.TemplateResponse(
                "usersList.html",
                context={'request': request, 'users': users, 'number_users' : number_users, 'current_user' : user}
            )
        else :
            return templates.TemplateResponse('exceptions.html', context={'status_code': 302, 'message': 'Vous n\'avez pas le droit d\'accéder à la liste des utilisateurs', 'request': request, 'redir':'connexion'})
    else:
        return templates.TemplateResponse(
            "blockedRedirect.html",
            context={'request': request, 'current_user' : user})
    
@router.get('/block/{id}')
def ask_block_user(request : Request, id : str, user: UserSchema = Depends(login_manager)):
    if user.admin == True :
        return templates.TemplateResponse(
            'block.html',
            context={"request": request,"id": id }
        )
    else :
        return templates.TemplateResponse('exceptions.html', context={'status_code' : 400, 'message': 'Vous n\'avez pas le droit de bloquer un utilisateur', 'redir':'connexion'})

@router.post('/block/{id}')
def block(request : Request,id : str):
    services.change_blocked_status(id)
    return RedirectResponse("/users/users_list", status_code=status.HTTP_303_SEE_OTHER)


@router.get('/password')
def passwordchange_ask(request : Request, user:UserSchema = Depends(login_manager)) :
    return templates.TemplateResponse(
        'passwordchange.html',
        context={'request':request, 'current_user':user}
    )

@router.post('/password')
def passwordchange(request : Request, password : Annotated[str,Form()], new_password : Annotated[str,Form()], new_password_confirmed : Annotated[str,Form()], user:UserSchema = Depends(login_manager.optional)) :
    encoded_password = password.encode()
    hashed_password = hashlib.sha3_256(encoded_password).hexdigest()
    if hashed_password == user.hashed_password : 
        if new_password_confirmed == new_password :
            encoded_new_password = new_password.encode()
            hashed_new_password = hashlib.sha3_256(encoded_new_password).hexdigest()
            services.change_password(hashed_new_password, user.id)
            return RedirectResponse('/users/me', status_code = 302)
        else :
            return templates.TemplateResponse('exceptions.html', context={'request':request, 'status_code': 400, 'message': 'Les deux mots de passe ne correspondent pas', 'redir':'profil'})
    return templates.TemplateResponse('exceptions.html', context={'request':request, 'status_code': 400, 'message': 'Votre ancien mot de passe est incorrect', 'redir':'profil'})
    
@router.get('/profilChange')
def profilchangeask(request : Request, user:UserSchema = Depends(login_manager)) :
    return templates.TemplateResponse('profilChange.html', context={'request':request, 'current_user':user})

@router.post('/profilChange')
def profilChange(request : Request, email : Annotated[str,Form()], name : Annotated[str,Form()], firstname : Annotated[str,Form()] ,user:UserSchema = Depends(login_manager)) :
    services.save_user_info(user.id, email, name, firstname)
    return RedirectResponse('/users/me', status_code=302)