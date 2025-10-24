from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import product_controller
from app.auth import auth_controller

app = FastAPI(
    title="Product Management API",
    description="API para gerenciar produtos com autenticação JWT",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router)
app.include_router(product_controller.router)
