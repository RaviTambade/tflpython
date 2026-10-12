from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ProficiencyLevel(StrEnum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"


class CatalogModel(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: str = Field(min_length=1, description="Stable identifier for this record")
    name: str = Field(min_length=1)
    description: str = ""


class SkillTaxonomy(CatalogModel):
    version: str = "1.0"


class SkillCategory(CatalogModel):
    taxonomy_id: str


class Skill(CatalogModel):
    category_id: str
    proficiency: ProficiencyLevel = ProficiencyLevel.INTERMEDIATE
    technology_ids: list[str] = Field(default_factory=list)


class Technology(CatalogModel):
    skill_ids: list[str] = Field(default_factory=list)


class JobRole(CatalogModel):
    skill_ids: list[str] = Field(default_factory=list)