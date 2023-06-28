from __future__ import annotations

from dataclasses import dataclass

from src.common.aggregate import Aggregate
from src.common.action import Action
from src.common.event import Event
from src.common.policy import Policy
import re


class AccountCreationInitialisedEvent(Event):
    ...


def validate_email_address(email: str) -> bool:
    return bool(re.match("[a-z0-9\.-]*@[a-z0-9\.-]\.[a-z]{5}", email))


class UserOnboardingAction(Action):
    def user_onboard(self, details: AccountDetails):
        if not validate_email_address(details.email):
            raise ValueError("Invalid Email.")

class AccountAggregate(Aggregate):
    ...

class AccountCreationPolicy(Policy):
    ...


@dataclass
class AccountDetails:
    email: str
    address: str
    proof_of_address: str