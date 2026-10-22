from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class Policy(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    maturity: str = Field(min_length=1)
    premium: float = Field(gt=0)


def create_app() -> FastAPI:
    app = FastAPI(
        title="TFLInsurance API",
        description="Simple Insurance Policy Management REST API",
        version="1.0",
    )
    policies = [
        {
            "id": 1,
            "name": "Jeevan Labh",
            "description": "Life insurance savings plan",
            "maturity": "10 years",
            "premium": 15000.0,
        },
        {
            "id": 2,
            "name": "Jeevan Arogya",
            "description": "Health insurance plan",
            "maturity": "5 years",
            "premium": 12000.0,
        },
        {
            "id": 3,
            "name": "Jeevan Suraksha",
            "description": "Family protection plan",
            "maturity": "15 years",
            "premium": 20000.0,
        },
    ]

    def find_policy(policy_id: int) -> dict | None:
        return next(
            (policy for policy in policies if policy["id"] == policy_id),
            None,
        )

    @app.get("/")
    def home() -> dict[str, str]:
        return {
            "application": "TFLInsurance",
            "message": "Welcome to TFLInsurance REST API",
            "docs": "/docs",
        }

    @app.get("/api/policies")
    def get_all_policies() -> dict[str, object]:
        return {
            "message": "Policies retrieved successfully",
            "count": len(policies),
            "data": policies,
        }

    @app.get("/api/policies/{policy_id}")
    def get_policy(policy_id: int) -> dict[str, object]:
        policy = find_policy(policy_id)
        if policy is None:
            raise HTTPException(status_code=404, detail="Policy not found")
        return policy

    @app.post("/api/policies", status_code=201)
    def create_policy(policy: Policy) -> dict[str, object]:
        new_id = max((item["id"] for item in policies), default=0) + 1
        new_policy = {"id": new_id, **policy.model_dump()}
        policies.append(new_policy)
        return {
            "message": "Policy created successfully",
            "data": new_policy,
        }

    @app.put("/api/policies/{policy_id}")
    def update_policy(
        policy_id: int,
        updated_policy: Policy,
    ) -> dict[str, object]:
        policy = find_policy(policy_id)
        if policy is None:
            raise HTTPException(status_code=404, detail="Policy not found")

        policy.update(updated_policy.model_dump())
        return {
            "message": "Policy updated successfully",
            "data": policy,
        }

    @app.delete("/api/policies/{policy_id}")
    def delete_policy(policy_id: int) -> dict[str, object]:
        policy = find_policy(policy_id)
        if policy is None:
            raise HTTPException(status_code=404, detail="Policy not found")

        policies.remove(policy)
        return {
            "message": "Policy deleted successfully",
            "deleted_policy": policy,
        }

    return app


app = create_app()
