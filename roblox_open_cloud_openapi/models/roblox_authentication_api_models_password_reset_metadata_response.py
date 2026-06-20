from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_users_legacy_user_response import RobloxWebResponsesUsersLegacyUserResponse


T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordResetMetadataResponse")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordResetMetadataResponse:
    """
    Attributes:
        users (list[RobloxWebResponsesUsersLegacyUserResponse] | Unset):
    """

    users: list[RobloxWebResponsesUsersLegacyUserResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_users_legacy_user_response import RobloxWebResponsesUsersLegacyUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _users = d.pop("users", UNSET)
        users: list[RobloxWebResponsesUsersLegacyUserResponse] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = RobloxWebResponsesUsersLegacyUserResponse.from_dict(users_item_data)

                users.append(users_item)

        roblox_authentication_api_models_password_reset_metadata_response = cls(
            users=users,
        )

        return roblox_authentication_api_models_password_reset_metadata_response
