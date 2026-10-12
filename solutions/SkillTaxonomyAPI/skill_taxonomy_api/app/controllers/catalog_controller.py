from typing import Any

from app.models.schemas import CatalogModel
from app.services.catalog_service import CatalogService


class CatalogController:
    def __init__(self, service: CatalogService, model: type[CatalogModel]):
        self.service = service
        self.model = model

    def list(self) -> list[dict[str, Any]]:
        return self.service.list()

    def get(self, record_id: str) -> dict[str, Any]:
        return self.service.get(record_id)

    def create(self, record: CatalogModel) -> dict[str, Any]:
        return self.service.create(record.model_dump())

    def update(self, record_id: str, record: CatalogModel) -> dict[str, Any]:
        return self.service.update(record_id, record.model_dump())

    def delete(self, record_id: str) -> None:
        self.service.delete(record_id)