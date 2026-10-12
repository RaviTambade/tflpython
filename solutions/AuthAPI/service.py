import hashlib
import hmac
import secrets
import time

from repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.reset_otps = {}

    def _hash_password(self, password: str, salt: str = None):
        if salt is None:
            salt = secrets.token_hex(16)

        digest = hashlib.pbkdf2_hmac("sha256",password.encode("utf-8"),bytes.fromhex(salt),600_000)

        return f"{salt}${digest.hex()}"

    def _verify_password(self, password: str, stored_hash: str):
        try:
            salt, expected_hash = stored_hash.split("$", 1)
            actual_hash = self._hash_password(password, salt).split("$", 1)[1]

            return hmac.compare_digest(actual_hash, expected_hash)
        except (ValueError, TypeError):
            return False

    def register(self, name: str, email: str, password: str):
        if self.repository.find_by_email(email):
            return False

        user = {
            "name": name.strip(),
            "email": email.strip().lower(),
            "password_hash": self._hash_password(password)
        }

        return self.repository.create_user(user)

    def login(self, email: str, password: str):
        user = self.repository.find_by_email(email)

        if not user:
            return False

        return self._verify_password(password,user["password_hash"])

    def request_password_reset(self, email: str):
        user = self.repository.find_by_email(email)

        # Avoid revealing whether an account exists.
        if not user:
            return None

        otp = f"{secrets.randbelow(1_000_000):06d}"

        self.reset_otps[email.lower()] = {
            "otp": otp,
            "expires_at": time.time() + 300,
            "attempts": 0
        }

        # Demo only. Production should send this via an email/SMS provider.
        return otp

    def reset_password(self, email: str, otp: str, new_password: str):
        key = email.lower()
        record = self.reset_otps.get(key)

        if not record:
            return False

        if time.time() >= record["expires_at"]:
            self.reset_otps.pop(key, None)
            return False

        if record["attempts"] >= 5:
            self.reset_otps.pop(key, None)
            return False

        if not secrets.compare_digest(record["otp"], otp):
            record["attempts"] += 1
            return False

        updated = self.repository.update_password(key,self._hash_password(new_password))

        self.reset_otps.pop(key, None)
        return updated