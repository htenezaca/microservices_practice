from fastapi import FastAPI
from .routes import user_router

def create_app() -> FastAPI:
    app = FastAPI(title="User Service")
    app.include_router(user_router, prefix="/users")
    return app
