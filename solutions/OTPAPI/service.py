import secrets
from datetime import datetime, timedelta, timezone

from repository import OTPRepository


class OTPService:
    def __init__(self, repository: OTPRepository):
        self.repository = repository

    def generate_otp(self, mobile: str) -> str:
        otp = f"{secrets.randbelow(1_000_000):06d}"

        expires_at = datetime.now(timezone.utc) + timedelta(minutes=5)

        self.repository.save(mobile, otp, expires_at)

        return otp

    def verify_otp(self, mobile: str, submitted_otp: str) -> bool:
        record = self.repository.get(mobile)

        if not record:
            return False

        now = datetime.now(timezone.utc)

        if now >= record["expires_at"]:
            self.repository.delete(mobile)
            return False

        if record["attempts"] >= 5:
            self.repository.delete(mobile)
            return False

        if secrets.compare_digest(record["otp"], submitted_otp):
            self.repository.delete(mobile)
            return True

        self.repository.increment_attempts(mobile)
        return False