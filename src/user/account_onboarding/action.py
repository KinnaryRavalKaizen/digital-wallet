from src.common.action import Action
from src.user.account_onboarding.event import UserOnboardingEvent
class UserOnboardingAction(Action):

    def __init__(self) -> None:
        super().__init__()
        self.event = UserOnboardingEvent
        self.request_data = {
            "email":"valid@email.com",
            "proof_of_address":"VALID1",
            "uk_user_identity":"validUK01",
        }

    def get_status(self) -> dict:
        results = self.event(self.request_data).get_outcome()
        if results.get('status'):
            results['message'] = "Account creation is successfully done."
        return results

    # def user_onboard(self, details: AccountDetails):
    #     if not validate_email_address(details.email):
    #         raise ValueError()
