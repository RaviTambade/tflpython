from datetime import datetime
from typing import Optional


class OTPRepository:
    def __init__(self):
        self.otp_store = {}

    def save(self, mobile: str, otp: str, expires_at: datetime):
        self.otp_store[mobile] = {
            "otp": otp,
            "expires_at": expires_at,
            "attempts": 0
        }

    def get(self, mobile: str) -> Optional[dict]:
        return self.otp_store.get(mobile)

    def increment_attempts(self, mobile: str):
        record = self.otp_store.get(mobile)

        if record:
            record["attempts"] += 1

    def delete(self, mobile: str):
        self.otp_store.pop(mobile, None)