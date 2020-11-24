from fastapi import APIRouter

from app.api import items, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(items.router, prefix="/api/v1", tags=["items"])