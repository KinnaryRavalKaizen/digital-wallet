from src.common.event import Event
from src.user.account_onboarding.policy import UserOnboardingPolicy

class UserOnboardingEvent(Event):

    def __init__(self,action_request_data:dict) -> None:
        super().__init__()
        self.policy = UserOnboardingPolicy
        self.email = action_request_data.get("email")
        self.proof_of_address = action_request_data.get("proof_of_address")
        self.uk_user_identity = action_request_data.get("uk_user_identity")

    def get_outcome(self) -> dict:
        # [we can check if user already exists]
        # get model data :

        # check for policy and apply if relevant
        is_policy_check_success = self.policy(
            self.email,self.proof_of_address,self.uk_user_identity
        ).validate_all_rules()

        # apply business logic
        if is_policy_check_success:
            return {"event_status":True}
        else:
            return {"event_status":False}
