from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_two_step_verification_api_verify_code_request_action_type import (
    RobloxTwoStepVerificationApiVerifyCodeRequestActionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiVerifyCodeRequest")


@_attrs_define
class RobloxTwoStepVerificationApiVerifyCodeRequest:
    """Request parameters for verifying a two step verification code.

    Attributes:
        challenge_id (str | Unset): The two step verification challenge ID.
        action_type (RobloxTwoStepVerificationApiVerifyCodeRequestActionType | Unset): The
            Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0,
            'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6,
            'Generic' = 7, 'GenericWithRecoveryCodes' = 8]
        code (str | Unset): The two step verification code.
    """

    challenge_id: str | Unset = UNSET
    action_type: RobloxTwoStepVerificationApiVerifyCodeRequestActionType | Unset = UNSET
    code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        action_type: int | Unset = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challengeId", UNSET)

        _action_type = d.pop("actionType", UNSET)
        action_type: RobloxTwoStepVerificationApiVerifyCodeRequestActionType | Unset
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = RobloxTwoStepVerificationApiVerifyCodeRequestActionType(_action_type)

        code = d.pop("code", UNSET)

        roblox_two_step_verification_api_verify_code_request = cls(
            challenge_id=challenge_id,
            action_type=action_type,
            code=code,
        )

        return roblox_two_step_verification_api_verify_code_request
