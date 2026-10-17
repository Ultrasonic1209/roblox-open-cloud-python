from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseTeamCreateSettingsModel")


@_attrs_define
class RobloxApiDevelopModelsUniverseTeamCreateSettingsModel:
    """Team create settings of a universe

    Attributes:
        id (int | Unset): Id of the universe.
        is_enabled (bool | Unset): Whether or not the universe is enabled for team create
    """

    id: int | Unset = UNSET
    is_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        roblox_api_develop_models_universe_team_create_settings_model = cls(
            id=id,
            is_enabled=is_enabled,
        )

        return roblox_api_develop_models_universe_team_create_settings_model
