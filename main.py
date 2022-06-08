from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bd_conex import Conexao

app = FastAPI()

templates = Jinja2Templates( directory="templates" )


@app.get ( "/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse( "index.html", {"request" : request} )


@app.get ( "/usuarios", response_class=HTMLResponse)
async def usuario(request: Request):
    return templates.TemplateResponse( "usuarios.html", {"request" : request} )


@app.get ( "/dashboard", response_class=HTMLResponse)
async def usuario(request: Request):
    return templates.TemplateResponse( "dashboard.html", {"request" : request} )


@app.get ( "/servicos", response_class=HTMLResponse)
async def usuario(request: Request):
    return templates.TemplateResponse( "servicos.html", {"request" : request} )


@app.post("/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(), password: str = Form()):

    conn = Conexao()
    conn.conn()
    res = conn.pesquisar(f"select iduser, usernome, senha FROM login WHERE usernome = '{username}' AND senha = '{password}' ")
    if not res:
        return templates.TemplateResponse( "teste.html", {"request" : request, 'resp': 0} )
    else:
        return templates.TemplateResponse( "teste.html", {"request" : request, 'resp': 1} )

if __name__ == '__mail__':
    app.rum()