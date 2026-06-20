from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsResponseTeamCreateSettingsResponse")


@_attrs_define
class RobloxApiDevelopModelsResponseTeamCreateSettingsResponse:
    """Team create settings

    Attributes:
        is_enabled (bool | Unset): Whether or not the universe should be enabled for team create
    """

    is_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_enabled = d.pop("isEnabled", UNSET)

        roblox_api_develop_models_response_team_create_settings_response = cls(
            is_enabled=is_enabled,
        )

        return roblox_api_develop_models_response_team_create_settings_response
