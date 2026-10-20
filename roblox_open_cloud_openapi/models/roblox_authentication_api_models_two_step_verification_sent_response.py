from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_two_step_verification_sent_response_media_type import (
    RobloxAuthenticationApiModelsTwoStepVerificationSentResponseMediaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsTwoStepVerificationSentResponse")


@_attrs_define
class RobloxAuthenticationApiModelsTwoStepVerificationSentResponse:
    """
    Attributes:
        media_type (RobloxAuthenticationApiModelsTwoStepVerificationSentResponseMediaType | Unset):  ['Email' = 0, 'SMS'
            = 1, 'Authenticator' = 2, 'RecoveryCode' = 3, 'SecurityKey' = 4, 'CrossDevice' = 5, 'Password' = 6, 'Passkey' =
            7]
        ticket (str | Unset):
    """

    media_type: RobloxAuthenticationApiModelsTwoStepVerificationSentResponseMediaType | Unset = UNSET
    ticket: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_type: int | Unset = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        ticket = self.ticket

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _media_type = d.pop("mediaType", UNSET)
        media_type: RobloxAuthenticationApiModelsTwoStepVerificationSentResponseMediaType | Unset
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = RobloxAuthenticationApiModelsTwoStepVerificationSentResponseMediaType(_media_type)

        ticket = d.pop("ticket", UNSET)

        roblox_authentication_api_models_two_step_verification_sent_response = cls(
            media_type=media_type,
            ticket=ticket,
        )

        return roblox_authentication_api_models_two_step_verification_sent_response
