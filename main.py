from urllib import request

from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from bd_conex import Conexao
from classes import class_token

app = FastAPI()

templates = Jinja2Templates( directory="templates" )
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


''' 
@app.post("/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(), password: str = Form(), ):
    conn = Conexao()
    conn.conn()
    res = conn.pesquisar(f"select iduser, usernome, senha FROM login WHERE usernome = '{username}' AND senha = '{password}' ")
    if not res:
        return templates.TemplateResponse( "index.html", {"request" : request, 'resp':0} )
    else:
        token = class_token.Token()
        token.setSub(username)
        token.setName(password)
        token.setToken(token.criarToken())
        dcd = token.decode(token.getToken())
        return templates.TemplateResponse("teste.html", {"request": request, 'token': dcd})


@app.get ( "/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode()
        return templates.TemplateResponse( "dashboard.html", {"request" : request, 'resp': resp} )
    except:
        return templates.TemplateResponse( "error.html", {"request" : request} )


@app.get ("/servicos", response_class=HTMLResponse)
async def services(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode(tkn.getToken())
        return templates.TemplateResponse("servicos.html", {"request": request, 'resp': resp})
    except:
        return templates.TemplateResponse("error.html", {"request": request})


 @app.get ( "/usuarios", response_class=HTMLResponse)
async def usuario(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode()
        return templates.TemplateResponse( "usuarios.html", {"request" : request, 'resp': resp} )
    except:
        return templates.TemplateResponse( "error.html", {"request" : request} )


@app.get ( "/teste", response_class=HTMLResponse)
async def teste(request: Request):
    try:
        token = class_token.Token()
        resp = token.decode()
        return templates.TemplateResponse("teste.html", {"request": request})
    except:
        return templates.TemplateResponse( "error.html", {"request": request})


@app.get("/items/", response_class=HTMLResponse)
async def read_items(token: str = Depends(oauth2_scheme) ):
    return {"token": token} '''

'''################################################################################################'''


@app.get ( "/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse( "index.html", {"request" : request} )


@app.post("/token", response_class=HTMLResponse)
async def token(request: Request ,form_data: OAuth2PasswordRequestForm = Depends()):
    conn = Conexao()
    conn.conn()
    resp = conn.pesquisar(
        f"select iduser, usernome, senha FROM login WHERE usernome = '{form_data.username}' AND senha = '{form_data.password}' ")
    if not resp:
        return 'user ou senha incorretos'

    else:
        for user_pass in resp:
            chave_login = user_pass[0]
            user_login = user_pass[1]
            pwd_login = user_pass[2]

        if form_data.username == user_login:
            '''if form_data.password == pwd_login:
                    tkn = class_token.Token()
                    chave_login = user_pass[0]
                    tkn.setSub(user_pass[0])
                    tkn.setName(user_login)
                    tkn.setChave(chave_login)
                    tkn.setToken(tkn.criarToken())
                    return tkn.getToken()'''
            return templates.TemplateResponse("dashboard.html", {"request": request, "access_token": form_data.username})
            #return {"access_token": form_data.username }

        else:
            return 'Usuário ou senha incorretos'


@app.get ( "/dashboard", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse( "dashboard.html", {"request" : request} )

@app.get("/")
async def index(token: str = Depends(oauth2_scheme)):
    return {'token_the': token}

if __name__ == '__mail__':
    app.rum()