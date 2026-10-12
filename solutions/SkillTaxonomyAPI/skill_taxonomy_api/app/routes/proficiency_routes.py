from fastapi import APIRouter

from app.models.schemas import ProficiencyLevel

router = APIRouter(prefix="/proficiencies", tags=["proficiencies"])


@router.get("/")
def list_proficiencies() -> list[str]:
    return [level.value for level in ProficiencyLevel]