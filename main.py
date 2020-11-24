from fastapi import FastAPI
from app.urls import api_router


app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn as u
    u.run(app, host="0.0.0.0", port=8000)