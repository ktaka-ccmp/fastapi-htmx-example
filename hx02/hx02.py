from typing import Optional
from fastapi import APIRouter, Depends, Request, Header
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from hx02.db import Customer, get_db


router = APIRouter()
templates = Jinja2Templates(directory='hx02')

# Ordinal API functions
@router.get("/")
async def json_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).offset(0).limit(100).all()
    return customers

# HTMX Response functions
@router.get("/list", response_class=HTMLResponse)
async def list(request: Request, skip: int = 0, limit: int = 1, hx_request: Optional[str] = Header(None), db: Session = Depends(get_db)):

    customers = db.query(Customer).offset(skip).limit(limit).all()
    context = {"skip_next": skip+limit, "limit": limit,"request": request, 'customers': customers}

    print("request.headers:", request.headers)

    if hx_request:
        return templates.TemplateResponse("list.tbody.html", context)
    return templates.TemplateResponse("list.html", context)
