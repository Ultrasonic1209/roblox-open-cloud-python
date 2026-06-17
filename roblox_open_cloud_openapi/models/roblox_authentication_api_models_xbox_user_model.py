from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsXboxUserModel")


@_attrs_define
class RobloxAuthenticationApiModelsXboxUserModel:
    """
    Attributes:
        id (str | Unset):
        user_id (int | Unset):
        username (str | Unset):
    """

    id: str | Unset = UNSET
    user_id: int | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if username is not UNSET:
            field_dict["Username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        user_id = d.pop("UserId", UNSET)

        username = d.pop("Username", UNSET)

        roblox_authentication_api_models_xbox_user_model = cls(
            id=id,
            user_id=user_id,
            username=username,
        )

        return roblox_authentication_api_models_xbox_user_model
