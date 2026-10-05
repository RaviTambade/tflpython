from dataclasses import asdict
from app.repositories.policy_repository import PolicyRepository


class PolicyService:

    def __init__(self, repository: PolicyRepository):
        self.repository = repository

    def get_all_policies(self):
        policies = self.repository.get_all()
        return [asdict(policy) for policy in policies]

    def get_policy(self, policy_id: int):
        policy = self.repository.get_by_id(policy_id)

        if policy is None:
            return None

        return asdict(policy)

    def create_policy(self, policy_data: dict):
        if policy_data["premium"] < 500:
            raise ValueError("Minimum premium must be 500")

        policy = self.repository.create(policy_data)
        return asdict(policy)

    def update_policy(self, policy_id: int, policy_data: dict):
        policy = self.repository.update(policy_id, policy_data)

        if policy is None:
            return None

        return asdict(policy)

    def delete_policy(self, policy_id: int):
        policy = self.repository.delete(policy_id)

        if policy is None:
            return None

        return asdict(policy)