from fastapi import FastAPI
from router import router

app = FastAPI(
    title="Transflower AuthAPI",
    description="Registration, Login and Password Reset API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to Transflower AuthAPI"}