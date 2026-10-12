from fastapi import HTTPException

from schemas import (
    OTPRequest,
    OTPVerifyRequest,
    OTPResponse,
    VerifyResponse
)
from service import OTPService

class OTPController:
    def __init__(self, service: OTPService):
        self.service = service

    def generate(self, request: OTPRequest) -> OTPResponse:
        otp = self.service.generate_otp(request.mobile)

        # Demo only: returning the OTP is NOT safe in production.
        return OTPResponse(
            message="OTP generated successfully",
            otp=otp
        )

    def verify(self, request: OTPVerifyRequest) -> VerifyResponse:
        verified = self.service.verify_otp(
            request.mobile,
            request.otp
        )

        if not verified:
            raise HTTPException(
                status_code=400,
                detail="Invalid, expired, or unavailable OTP"
            )

        return VerifyResponse(
            message="OTP verified successfully",
            verified=True
        )