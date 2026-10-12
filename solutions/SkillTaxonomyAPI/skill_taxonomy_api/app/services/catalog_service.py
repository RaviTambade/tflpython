from typing import Any

from fastapi import HTTPException, status

from app.repositories.json_repository import JsonRepository


class CatalogService:
    def __init__(self, repository: JsonRepository):
        self.repository = repository

    def list(self) -> list[dict[str, Any]]:
        return self.repository.list()

    def get(self, record_id: str) -> dict[str, Any]:
        record = self.repository.get(record_id)
        if record is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        return record

    def create(self, record: dict[str, Any]) -> dict[str, Any]:
        if self.repository.get(record["id"]) is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Record ID already exists")
        return self.repository.create(record)

    def update(self, record_id: str, record: dict[str, Any]) -> dict[str, Any]:
        if self.repository.get(record_id) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        if record["id"] != record_id:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="ID cannot be changed")
        return self.repository.update(record_id, record)

    def delete(self, record_id: str) -> None:
        if not self.repository.delete(record_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")