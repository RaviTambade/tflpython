from pydantic import BaseModel, Field


class OTPRequest(BaseModel):
    mobile: str = Field(min_length=10, max_length=15)


class OTPVerifyRequest(BaseModel):
    mobile: str = Field(min_length=10, max_length=15)
    otp: str = Field(pattern=r"^\d{6}$")


class OTPResponse(BaseModel):
    message: str
    otp: str | None = None


class VerifyResponse(BaseModel):
    message: str
    verified: bool