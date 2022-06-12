from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bd_conex import Conexao
from classes import class_token

app = FastAPI()

templates = Jinja2Templates( directory="templates" )


@app.get ( "/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse( "index.html", {"request" : request} )


@app.get ( "/usuarios", response_class=HTMLResponse)
async def usuario(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode()
        return templates.TemplateResponse( "usuarios.html", {"request" : request, 'resp': resp} )
    except:
        return templates.TemplateResponse( "error.html", {"request" : request} )


@app.get ( "/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode()
        return templates.TemplateResponse( "dashboard.html", {"request" : request, 'resp': resp} )
    except:
        return templates.TemplateResponse( "error.html", {"request" : request} )


@app.get ( "/servicos", response_class=HTMLResponse)
async def services(request: Request):
    try:
        tkn = class_token.Token()
        resp = tkn.decode()
        return templates.TemplateResponse("servicos.html", {"request": request, 'resp': resp})
    except:
        return templates.TemplateResponse("error.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(), password: str = Form()):
    conn = Conexao()
    conn.conn()
    res = conn.pesquisar(f"select iduser, usernome, senha FROM login WHERE usernome = '{username}' AND senha = '{password}' ")
    if not res:
        return templates.TemplateResponse( "index.html", {"request" : request, 'resp':0} )
    else:
        token = class_token.Token()
        token.setSub('username')
        token.setName('password')
        resp = token.criarToken()
        return templates.TemplateResponse( "dashboard.html", {"request" : request, 'resp': resp} )


@app.get ( "/teste", response_class=HTMLResponse)
async def teste(request: Request):
   return templates.TemplateResponse( "teste.html", {"request" : request} )


if __name__ == '__mail__':
    app.rum()
