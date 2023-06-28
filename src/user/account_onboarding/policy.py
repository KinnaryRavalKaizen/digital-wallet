import re
from src.common.policy import Policy

class UserOnboardingPolicy(Policy):
    def __init__(
        self,
        email:str,
        proof_of_address:str,
        uk_user_identity:str):
        super().__init__()
        self.email = email
        self.proof_of_address = proof_of_address
        self.uk_user_identity = uk_user_identity

    @staticmethod
    def validate_email_address(email) -> bool:
        return bool(re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email))

    @staticmethod
    def validate_proof_of_address(proof_of_address) -> bool:
        return bool(re.match("^[a-zA-Z0-9]{5,6}$", proof_of_address))

    @staticmethod
    def validate_uk_user_identity(uk_user_identity) -> bool:
        return bool(re.match("[a-zA-Z0-9]{9}", uk_user_identity))

    def validate_all_rules(self) -> dict:
        response = {"policy_check_status":True}
        if not self.validate_email_address(self.email):
            raise ValueError(f"Policy check failed for email {self.email}")
        if not self.validate_proof_of_address(self.proof_of_address):
            raise ValueError(f"Policy check failed for proof_of_address {self.proof_of_address}")
        if not self.validate_uk_user_identity(self.uk_user_identity):
            raise ValueError(f"Policy check failed for uk_user_identity {self.uk_user_identity}")
        return response
