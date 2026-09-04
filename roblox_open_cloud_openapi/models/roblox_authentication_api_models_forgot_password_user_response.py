from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_users_legacy_user_response import RobloxWebResponsesUsersLegacyUserResponse


T = TypeVar("T", bound="RobloxAuthenticationApiModelsForgotPasswordUserResponse")


@_attrs_define
class RobloxAuthenticationApiModelsForgotPasswordUserResponse:
    """
    Attributes:
        user (RobloxWebResponsesUsersLegacyUserResponse | Unset):
        ticket (str | Unset):
    """

    user: RobloxWebResponsesUsersLegacyUserResponse | Unset = UNSET
    ticket: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        ticket = self.ticket

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_users_legacy_user_response import RobloxWebResponsesUsersLegacyUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user = d.pop("user", UNSET)
        user: RobloxWebResponsesUsersLegacyUserResponse | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxWebResponsesUsersLegacyUserResponse.from_dict(_user)

        ticket = d.pop("ticket", UNSET)

        roblox_authentication_api_models_forgot_password_user_response = cls(
            user=user,
            ticket=ticket,
        )

        return roblox_authentication_api_models_forgot_password_user_response
