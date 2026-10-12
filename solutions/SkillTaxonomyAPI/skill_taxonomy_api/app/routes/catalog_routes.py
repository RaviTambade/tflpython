from typing import TypeVar

from fastapi import APIRouter, Response, status

from app.controllers.catalog_controller import CatalogController
from app.models.schemas import CatalogModel
from app.repositories.json_repository import JsonRepository
from app.services.catalog_service import CatalogService


ModelType = TypeVar("ModelType", bound=CatalogModel)


def create_catalog_router(
    filename: str,
    resource_name: str,
    model: type[ModelType],
) -> APIRouter:
    controller = CatalogController(CatalogService(JsonRepository(filename)), model)
    router = APIRouter(prefix=f"/{resource_name}", tags=[resource_name.replace("_", " ")])

    @router.get("/", response_model=list[model])
    def list_records():
        return controller.list()

    @router.get("/{record_id}", response_model=model)
    def get_record(record_id: str):
        return controller.get(record_id)

    @router.post("/", response_model=model, status_code=status.HTTP_201_CREATED)
    def create_record(record: model):
        return controller.create(record)

    @router.put("/{record_id}", response_model=model)
    def update_record(record_id: str, record: model):
        return controller.update(record_id, record)

    @router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_record(record_id: str):
        controller.delete(record_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router