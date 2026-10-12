import json
import os
import tempfile
from pathlib import Path

class UserRepository:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent / "users.json"

        if not self.file_path.exists():
            self._write_users([])

    def _read_users(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _write_users(self, users):
        # Write to a temporary file before replacing the data file.
        fd, temp_path = tempfile.mkstemp(dir=self.file_path.parent,suffix=".tmp")

        try:
            with os.fdopen(fd, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4)

            os.replace(temp_path, self.file_path)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def find_by_email(self, email: str):
        users = self._read_users()

        for user in users:
            if user["email"].lower() == email.lower():
                return user

        return None

    def create_user(self, user: dict):
        users = self._read_users()

        if any(
            item["email"].lower() == user["email"].lower()
            for item in users
        ):
            return False

        users.append(user)
        self._write_users(users)
        return True

    def update_password(self, email: str, password_hash: str):
        users = self._read_users()

        for user in users:
            if user["email"].lower() == email.lower():
                user["password_hash"] = password_hash
                self._write_users(users)
                return True

        return False