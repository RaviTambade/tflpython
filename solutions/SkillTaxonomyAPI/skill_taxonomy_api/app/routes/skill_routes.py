from app.models.schemas import Skill
from app.routes.catalog_routes import create_catalog_router

router = create_catalog_router("skills.json", "skills", Skill)