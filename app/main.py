from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI(
    title="device_systems",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to device_systems API"
    }