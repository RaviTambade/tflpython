from fastapi import FastAPI

from app.routes import ( job_role_routes, proficiency_routes, skill_category_routes, skill_routes,
                            skill_taxonomy_routes, technology_routes,
)

app = FastAPI(title="Skill Taxonomy API",  description="A JSON-backed API for skill taxonomies, skills, technologies, and job roles.",
    version="1.0.0",
)

app.include_router(skill_taxonomy_routes.router, prefix="/api/v1")
app.include_router(skill_category_routes.router, prefix="/api/v1")
app.include_router(skill_routes.router, prefix="/api/v1")
app.include_router(proficiency_routes.router, prefix="/api/v1")
app.include_router(technology_routes.router, prefix="/api/v1")
app.include_router(job_role_routes.router, prefix="/api/v1")


@app.get("/", tags=["health"])
def read_root() -> dict[str, str]:
    return {"name": "Skill Taxonomy API", "docs": "/docs"}