from fastapi import FastAPI
from app.routes.user_routes import router
from app.database.connection import engine, Base
from app.models.user_model import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="device_systems API",
    description="API REST para la gestión de usuarios del sistema device_systems",
    version="2.0.0",
    contact={
        "name": "Ivan Florez"
    }
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to device_systems API"
    }
