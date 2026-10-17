from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiModelsResponseGameNameDescriptionMetadataResponse")


@_attrs_define
class RobloxGameInternationalizationApiModelsResponseGameNameDescriptionMetadataResponse:
    """
    Attributes:
        is_name_description_migration_enabled (bool | Unset):
    """

    is_name_description_migration_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_name_description_migration_enabled = self.is_name_description_migration_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_name_description_migration_enabled is not UNSET:
            field_dict["isNameDescriptionMigrationEnabled"] = is_name_description_migration_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_name_description_migration_enabled = d.pop("isNameDescriptionMigrationEnabled", UNSET)

        roblox_game_internationalization_api_models_response_game_name_description_metadata_response = cls(
            is_name_description_migration_enabled=is_name_description_migration_enabled,
        )

        return roblox_game_internationalization_api_models_response_game_name_description_metadata_response
