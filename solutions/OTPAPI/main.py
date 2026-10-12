from fastapi import FastAPI
from router import router

app = FastAPI(
    title="TFLInsurance OTP API",
    version="1.0.0",
    description="OTP generation and verification learning project"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to TFLInsurance OTP API"}