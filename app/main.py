from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

usuarios = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "usuarios": usuarios})

@app.post("/usuarios/", response_class=HTMLResponse)
async def create_user(request: Request, nome: str = Form(...), nomeGotico: str = Form(...)):
    usuario = {"nome": nome, "nomeGotico": nomeGotico}
    usuarios.append(usuario)
    return templates.TemplateResponse("index.html", {"request": request, "usuarios": usuarios})