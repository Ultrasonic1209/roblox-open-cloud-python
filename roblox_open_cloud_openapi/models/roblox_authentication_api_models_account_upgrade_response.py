from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAccountUpgradeResponse")


@_attrs_define
class RobloxAuthenticationApiModelsAccountUpgradeResponse:
    """
    Attributes:
        user_id (int | Unset):
        username (str | Unset):
    """

    user_id: int | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        roblox_authentication_api_models_account_upgrade_response = cls(
            user_id=user_id,
            username=username,
        )

        return roblox_authentication_api_models_account_upgrade_response
