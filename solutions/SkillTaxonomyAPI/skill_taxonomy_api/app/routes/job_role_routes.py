from app.models.schemas import JobRole
from app.routes.catalog_routes import create_catalog_router

router = create_catalog_router("job_roles.json", "job_roles", JobRole)