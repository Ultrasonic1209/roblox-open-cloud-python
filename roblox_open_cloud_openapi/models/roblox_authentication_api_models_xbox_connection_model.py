from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsXboxConnectionModel")


@_attrs_define
class RobloxAuthenticationApiModelsXboxConnectionModel:
    """
    Attributes:
        has_connected_xbox_account (bool | Unset):
        gamertag (str | Unset):
    """

    has_connected_xbox_account: bool | Unset = UNSET
    gamertag: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_connected_xbox_account = self.has_connected_xbox_account

        gamertag = self.gamertag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_connected_xbox_account is not UNSET:
            field_dict["hasConnectedXboxAccount"] = has_connected_xbox_account
        if gamertag is not UNSET:
            field_dict["gamertag"] = gamertag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        has_connected_xbox_account = d.pop("hasConnectedXboxAccount", UNSET)

        gamertag = d.pop("gamertag", UNSET)

        roblox_authentication_api_models_xbox_connection_model = cls(
            has_connected_xbox_account=has_connected_xbox_account,
            gamertag=gamertag,
        )

        return roblox_authentication_api_models_xbox_connection_model
