
from typing import Optional
from fastapi import APIRouter, Request, Header
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

templates = Jinja2Templates(directory='hx01')

@router.get("/index", response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request }
    return templates.TemplateResponse('index.html', context)

@router.get("/list", response_class=HTMLResponse)
async def list(request: Request, hx_request: Optional[str] = Header(None)):
    films = [
        {'name': 'Blade Runner', 'director': 'Ridley Scott'},
        {'name': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
        {'name': 'Mulholland Drive', 'director': 'David Lynch'},
    ]
    context = {"request": request, 'films': films}
    if hx_request:
        return templates.TemplateResponse("list.tbody.html", context)
    return templates.TemplateResponse("list.html", context)

@router.get("/list/tbody", response_class=HTMLResponse)
async def list_table(request: Request):
    films = [
        {'name': 'Blade Runner', 'director': 'Ridley Scott'},
        {'name': 'Pulp Fiction', 'director': 'Quentin Tarantino'},
        {'name': 'Mulholland Drive', 'director': 'David Lynch'},
    ]
    context = {"request": request, 'films': films}
    return templates.TemplateResponse("list.tbody.html", context)
