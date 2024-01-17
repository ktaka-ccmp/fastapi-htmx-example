from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api01.customer
import hx01.hx01

app = FastAPI()

app.include_router(
    api01.customer.router,
    prefix="/api01",
    tags=["CustomerWOAuthentication"],
)

app.include_router(
    hx01.hx01.router,
    prefix="/hx01",
    tags=["HTMX"],
)

origins = [
    "http://localhost:3000",
    "http://10.0.0.201:3000",
    ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


