from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsTwoStepVerificationV3LoginResponse")


@_attrs_define
class RobloxAuthenticationApiModelsTwoStepVerificationV3LoginResponse:
    """
    Attributes:
        identity_verification_login_ticket (str | Unset):
        account_blob (str | Unset):
    """

    identity_verification_login_ticket: str | Unset = UNSET
    account_blob: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity_verification_login_ticket = self.identity_verification_login_ticket

        account_blob = self.account_blob

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identity_verification_login_ticket is not UNSET:
            field_dict["identityVerificationLoginTicket"] = identity_verification_login_ticket
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_verification_login_ticket = d.pop("identityVerificationLoginTicket", UNSET)

        account_blob = d.pop("accountBlob", UNSET)

        roblox_authentication_api_models_two_step_verification_v3_login_response = cls(
            identity_verification_login_ticket=identity_verification_login_ticket,
            account_blob=account_blob,
        )

        return roblox_authentication_api_models_two_step_verification_v3_login_response
