from fastapi import FastAPI

from app.database.connection import engine, Base

from app.models.user_model import User
from app.models.device_model import Device
from app.models.loan_model import Loan

from app.routes.user_routes import router as user_router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router


# Crear tablas
Base.metadata.create_all(bind=engine)

# Crear aplicación
app = FastAPI(
    title="device_systems API",
    description="API REST para gestión de usuarios, dispositivos y préstamos",
    version="4.0.0",
    contact={
        "name": "Ivan Florez"
    }
)

# Registrar rutas
app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to device_systems API"
    }
