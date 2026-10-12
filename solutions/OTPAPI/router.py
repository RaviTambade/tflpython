from fastapi import APIRouter

from schemas import (
    OTPRequest,
    OTPVerifyRequest,
    OTPResponse,
    VerifyResponse
)
from controller import OTPController
from service import OTPService
from repository import OTPRepository


router = APIRouter(prefix="/api/otp", tags=["OTP"])

repository = OTPRepository()
service = OTPService(repository)
controller = OTPController(service)


@router.post("/generate", response_model=OTPResponse)
def generate_otp(request: OTPRequest):
    return controller.generate(request)


@router.post("/verify", response_model=VerifyResponse)
def verify_otp(request: OTPVerifyRequest):
    return controller.verify(request)