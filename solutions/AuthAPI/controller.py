from fastapi import HTTPException

from schemas import (
    RegisterRequest,
    LoginRequest,
    ResetOTPRequest,
    ResetPasswordRequest
)
from service import AuthService


class AuthController:
    def __init__(self, service: AuthService):
        self.service = service

    def register(self, request: RegisterRequest):
        success = self.service.register(
            request.name,
            request.email,
            request.password
        )

        if not success:
            raise HTTPException(
                status_code=409,
                detail="An account with this email already exists"
            )

        return {"message": "Registration successful"}

    def login(self, request: LoginRequest):
        success = self.service.login(
            request.email,
            request.password
        )

        if not success:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        # This verifies credentials only; JWT/session creation
        # is a separate step for a production authentication API.
        return {"message": "Login successful"}

    def request_password_reset(self, request: ResetOTPRequest):
        otp = self.service.request_password_reset(request.email)

        if otp is not None:
            # Demo only: never return an OTP in a production response.
            return {
                "message": "Reset OTP generated",
                "demo_otp": otp
            }

        return {
            "message": "If the account exists, reset instructions will be sent"
        }

    def reset_password(self, request: ResetPasswordRequest):
        success = self.service.reset_password(
            request.email,
            request.otp,
            request.new_password
        )

        if not success:
            raise HTTPException(
                status_code=400,
                detail="Invalid, expired, or unavailable reset OTP"
            )

        return {"message": "Password reset successful"}