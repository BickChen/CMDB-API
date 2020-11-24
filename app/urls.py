from fastapi import APIRouter

from app.routers.api.v1 import index, items

api_router = APIRouter()
api_router.include_router(index.router, tags=["login"])
api_router.include_router(items.router, prefix="/api/v1", tags=["items"])