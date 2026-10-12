from app.models.schemas import SkillTaxonomy
from app.routes.catalog_routes import create_catalog_router

router = create_catalog_router("taxonomies.json", "taxonomies", SkillTaxonomy)