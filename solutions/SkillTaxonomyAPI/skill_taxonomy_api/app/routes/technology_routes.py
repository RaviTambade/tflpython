from app.models.schemas import Technology
from app.routes.catalog_routes import create_catalog_router

router = create_catalog_router("technologies.json", "technologies", Technology)