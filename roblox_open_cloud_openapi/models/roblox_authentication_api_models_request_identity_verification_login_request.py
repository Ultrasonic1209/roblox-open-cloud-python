from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestIdentityVerificationLoginRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestIdentityVerificationLoginRequest:
    """
    Attributes:
        login_ticket (str | Unset):
        result_token (str | Unset):
    """

    login_ticket: str | Unset = UNSET
    result_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        login_ticket = self.login_ticket

        result_token = self.result_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if login_ticket is not UNSET:
            field_dict["loginTicket"] = login_ticket
        if result_token is not UNSET:
            field_dict["resultToken"] = result_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_ticket = d.pop("loginTicket", UNSET)

        result_token = d.pop("resultToken", UNSET)

        roblox_authentication_api_models_request_identity_verification_login_request = cls(
            login_ticket=login_ticket,
            result_token=result_token,
        )

        return roblox_authentication_api_models_request_identity_verification_login_request
