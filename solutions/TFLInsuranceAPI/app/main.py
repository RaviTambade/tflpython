from fastapi import FastAPI

from app.api.routes.policy_routes import router as policy_router
from app.repositories.policy_repository import PolicyRepository
from app.services.policy_service import PolicyService


app = FastAPI(
    title="TFLInsurance API",
    description="Insurance Policy Management REST API",
    version="1.0"
)


# Create shared application dependencies
repository = PolicyRepository()
app.state.policy_service = PolicyService(repository)


# Register API routes
app.include_router(policy_router)


@app.get("/")
def home():
    return {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs"
    }