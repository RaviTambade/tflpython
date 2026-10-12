from app.models.schemas import SkillCategory
from app.routes.catalog_routes import create_catalog_router

router = create_catalog_router("categories.json", "categories", SkillCategory)