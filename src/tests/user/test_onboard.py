import pytest

from src.user.account_onboarding.action import UserOnboardingAction
from src.user.account_onboarding.event import UserOnboardingEvent
from src.user.account_onboarding.policy import UserOnboardingPolicy


# ACTION TEST CASES
def test_can_user_onboarding_action_instantiate() -> None:
    # given
    action = UserOnboardingAction()

    # then
    assert isinstance(action, UserOnboardingAction)

def test_can__action__get_status() -> None:
    # given
    action = UserOnboardingAction()

    # when
    results = action.get_status()

    # then
    assert results == {
        "status":True, "message":"Account creation is successfully done."
    }


# EVENT TEST CASES
def test_can_user_onboarding_event_instantiate() -> None:
    # given
    action_request_data = {
        "email" : "valid@email.com",
        "proof_of_address" : "VALID",
        "uk_user_identity" : "Validuk90"
    }
    event = UserOnboardingEvent(action_request_data)

    # then
    assert isinstance(event, UserOnboardingEvent)

def test_can__event__get_outcome():
    # given
    action_request_data = {
        "email" : "valid@email.com",
        "proof_of_address" : "VALID",
        "uk_user_identity" : "Validuk90"
    }
    event = UserOnboardingEvent(action_request_data)
    # when
    event_results = event.get_outcome()

    # then
    assert event_results == {"status":True}


# POLICY TEST CASES
def test_can_user_onboarding_policy_instantiate() -> None:
    # given
    email = "valid@email.com"
    proof_of_address = "VALID"
    uk_user_identity = "Validuk90"
    user_policy = UserOnboardingPolicy(email, proof_of_address, uk_user_identity)

    # then
    assert isinstance(user_policy, UserOnboardingPolicy)

def test_can__policy__validate_email_address() -> None:
    # given
    email = "valid@email.com"

    # then
    assert UserOnboardingPolicy.validate_email_address(email) == True

def test_fails__policy__validate_email_address() -> None:
    # given
    email = "invalid email"

    # then
    assert UserOnboardingPolicy.validate_email_address(email) == False

def test_can__policy__validate_proof_of_address() -> None:
    # given
    zip_code = "B152GJ"

    # then
    assert UserOnboardingPolicy.validate_proof_of_address(zip_code) == True

def test_fails__policy__validate_proof_of_address() -> None:
    # given
    zip_code = "invalid address"

    # then
    assert UserOnboardingPolicy.validate_proof_of_address(zip_code) == False

def test_can__policy__validate_all_rules() -> None:
    # given
    email = "valid@email.com"
    proof_of_address = "Valid1"
    uk_user_identity = "UKValidID1"

    user_policy = UserOnboardingPolicy(email, proof_of_address, uk_user_identity)

    # when
    event_results = user_policy.validate_all_rules()

    # then
    assert event_results == {"policy_check_status":True}


def test_fails_when_invalid_email__policy__validate_all_rules() -> None:
    # given
    email = "invalid email"
    proof_of_address = "Valid1"
    uk_user_identity = "UKValidID1"

    user_policy = UserOnboardingPolicy(email, proof_of_address, uk_user_identity)

    # when
    with pytest.raises(ValueError, match=f"Policy check failed for email {email}"):
        user_policy.validate_all_rules()

def test_fails_when_invalid_proof_of_address__policy__validate_all_rules() -> None:
    # given
    email = "valid@email.com"
    proof_of_address = "Invalid Address"
    uk_user_identity = "UKValidID1"

    user_policy = UserOnboardingPolicy(email, proof_of_address, uk_user_identity)

    # when
    with pytest.raises(ValueError, match=f"Policy check failed for proof_of_address {proof_of_address}"):
        user_policy.validate_all_rules()


def test_fails_when_invalid_uk_id__policy__validate_all_rules() -> None:
    # given
    email = "valid@email.com"
    proof_of_address = "Valid1"
    uk_user_identity = "Invalid ID"

    user_policy = UserOnboardingPolicy(email, proof_of_address, uk_user_identity)

    # when
    with pytest.raises(ValueError, match=f"Policy check failed for uk_user_identity {uk_user_identity}"):
        user_policy.validate_all_rules()
