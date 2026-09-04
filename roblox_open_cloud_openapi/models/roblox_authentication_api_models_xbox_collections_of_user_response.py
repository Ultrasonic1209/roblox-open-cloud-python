from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_xbox_user_model import RobloxAuthenticationApiModelsXboxUserModel


T = TypeVar("T", bound="RobloxAuthenticationApiModelsXboxCollectionsOfUserResponse")


@_attrs_define
class RobloxAuthenticationApiModelsXboxCollectionsOfUserResponse:
    """
    Attributes:
        users (list[RobloxAuthenticationApiModelsXboxUserModel] | Unset):
    """

    users: list[RobloxAuthenticationApiModelsXboxUserModel] | Unset = UNSET

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
            field_dict["Users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_xbox_user_model import RobloxAuthenticationApiModelsXboxUserModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _users = d.pop("Users", UNSET)
        users: list[RobloxAuthenticationApiModelsXboxUserModel] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = RobloxAuthenticationApiModelsXboxUserModel.from_dict(users_item_data)

                users.append(users_item)

        roblox_authentication_api_models_xbox_collections_of_user_response = cls(
            users=users,
        )

        return roblox_authentication_api_models_xbox_collections_of_user_response
