from fastapi import APIRouter

from app.routers.api.v1 import index, aliyun_api

api_router = APIRouter()
api_router.include_router(index.router, tags=["index"])
api_router.include_router(aliyun_api.router, prefix="/api/v1", tags=["aliyun_api"])