from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)

from app.schemas.policy_schema import (
    PolicyCreate,
    PolicyUpdate,
    PolicyResponse
)

from app.services.policy_service import PolicyService


router = APIRouter(
    prefix="/api/policies",
    tags=["Policies"]
)


def get_policy_service(request: Request) -> PolicyService:
    return request.app.state.policy_service


@router.get("/")
def get_all_policies(
    service: PolicyService = Depends(get_policy_service)
):
    policies = service.get_all_policies()

    return {
        "message": "Policies retrieved successfully",
        "count": len(policies),
        "data": policies
    }


@router.get(
    "/{policy_id}",
    response_model=PolicyResponse
)
def get_policy(
    policy_id: int,
    service: PolicyService = Depends(get_policy_service)
):
    policy = service.get_policy(policy_id)

    if policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return policy


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PolicyResponse
)
def create_policy(
    policy: PolicyCreate,
    service: PolicyService = Depends(get_policy_service)
):
    try:
        return service.create_policy(
            policy.model_dump()
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/{policy_id}", response_model=PolicyResponse)
def update_policy( policy_id: int,policy: PolicyUpdate,service: PolicyService = Depends(get_policy_service)):
    updated = service.update_policy( policy_id,policy.model_dump())

    if updated is None:
        raise HTTPException(status_code=404,detail="Policy not found")

    return updated


@router.delete("/{policy_id}")
def delete_policy(policy_id: int,service: PolicyService = Depends(get_policy_service)):
    deleted = service.delete_policy(policy_id)

    if deleted is None:
        raise HTTPException(status_code=404,detail="Policy not found")

    return {
        "message": "Policy deleted successfully",
        "deleted_policy": deleted
    }