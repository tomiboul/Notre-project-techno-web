from fastapi import FastAPI, status, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses  import RedirectResponse
from fastapi.templating import Jinja2Templates
#from app.route.books import router as book_router
#from app.route.users import router as users_router
from app.database import create_database, delete_database

app = FastAPI(title="Bomel et compagnie")
#app.include_router(book_router)
#app.include_router(users_router)
app.mount("/static", StaticFiles(directory="././static"), name='static')
templates = Jinja2Templates(directory="././templates")



@app.on_event('startup')
def on_startup():
    print("Server started.")
    
    create_database()


def on_shutdown():
    print("Bye bye!")


@app.get("/")
def root():
    return RedirectResponse("users/login", status_code=status.HTTP_303_SEE_OTHER)



@app.exception_handler(HTTPException)
def Exception(request: Request, exc: HTTPException):
    return templates.TemplateResponse(
        "exceptions.html",
        context={
            "request": request,
            "status_code": exc.status_code,
            "message:" : exc.detail
        }
    )
