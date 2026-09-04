from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRevertAccountSubmitRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRevertAccountSubmitRequest:
    """
    Attributes:
        user_id (int | Unset):
        new_password (str | Unset):
        new_password_repeated (str | Unset):
        ticket (str | Unset):
        two_step_verification_challenge_id (str | Unset):
        two_step_verification_token (str | Unset):
    """

    user_id: int | Unset = UNSET
    new_password: str | Unset = UNSET
    new_password_repeated: str | Unset = UNSET
    ticket: str | Unset = UNSET
    two_step_verification_challenge_id: str | Unset = UNSET
    two_step_verification_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        new_password = self.new_password

        new_password_repeated = self.new_password_repeated

        ticket = self.ticket

        two_step_verification_challenge_id = self.two_step_verification_challenge_id

        two_step_verification_token = self.two_step_verification_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if new_password is not UNSET:
            field_dict["NewPassword"] = new_password
        if new_password_repeated is not UNSET:
            field_dict["NewPasswordRepeated"] = new_password_repeated
        if ticket is not UNSET:
            field_dict["Ticket"] = ticket
        if two_step_verification_challenge_id is not UNSET:
            field_dict["TwoStepVerificationChallengeId"] = two_step_verification_challenge_id
        if two_step_verification_token is not UNSET:
            field_dict["TwoStepVerificationToken"] = two_step_verification_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("UserId", UNSET)

        new_password = d.pop("NewPassword", UNSET)

        new_password_repeated = d.pop("NewPasswordRepeated", UNSET)

        ticket = d.pop("Ticket", UNSET)

        two_step_verification_challenge_id = d.pop("TwoStepVerificationChallengeId", UNSET)

        two_step_verification_token = d.pop("TwoStepVerificationToken", UNSET)

        roblox_authentication_api_models_revert_account_submit_request = cls(
            user_id=user_id,
            new_password=new_password,
            new_password_repeated=new_password_repeated,
            ticket=ticket,
            two_step_verification_challenge_id=two_step_verification_challenge_id,
            two_step_verification_token=two_step_verification_token,
        )

        return roblox_authentication_api_models_revert_account_submit_request
