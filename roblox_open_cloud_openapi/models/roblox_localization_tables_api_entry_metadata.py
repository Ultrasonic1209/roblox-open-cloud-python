from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_entry_metadata_entry_format import (
    RobloxLocalizationTablesApiEntryMetadataEntryFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_in_game_content_tables_client_game_location import RobloxInGameContentTablesClientGameLocation


T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryMetadata")


@_attrs_define
class RobloxLocalizationTablesApiEntryMetadata:
    """
    Attributes:
        example (str | Unset):
        game_locations (list[RobloxInGameContentTablesClientGameLocation] | Unset):
        entry_format (RobloxLocalizationTablesApiEntryMetadataEntryFormat | Unset):
    """

    example: str | Unset = UNSET
    game_locations: list[RobloxInGameContentTablesClientGameLocation] | Unset = UNSET
    entry_format: RobloxLocalizationTablesApiEntryMetadataEntryFormat | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        example = self.example

        game_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.game_locations, Unset):
            game_locations = []
            for game_locations_item_data in self.game_locations:
                game_locations_item = game_locations_item_data.to_dict()
                game_locations.append(game_locations_item)

        entry_format: str | Unset = UNSET
        if not isinstance(self.entry_format, Unset):
            entry_format = self.entry_format.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if example is not UNSET:
            field_dict["example"] = example
        if game_locations is not UNSET:
            field_dict["gameLocations"] = game_locations
        if entry_format is not UNSET:
            field_dict["entryFormat"] = entry_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_in_game_content_tables_client_game_location import (
            RobloxInGameContentTablesClientGameLocation,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        example = d.pop("example", UNSET)

        _game_locations = d.pop("gameLocations", UNSET)
        game_locations: list[RobloxInGameContentTablesClientGameLocation] | Unset = UNSET
        if _game_locations is not UNSET:
            game_locations = []
            for game_locations_item_data in _game_locations:
                game_locations_item = RobloxInGameContentTablesClientGameLocation.from_dict(game_locations_item_data)

                game_locations.append(game_locations_item)

        _entry_format = d.pop("entryFormat", UNSET)
        entry_format: RobloxLocalizationTablesApiEntryMetadataEntryFormat | Unset
        if isinstance(_entry_format, Unset):
            entry_format = UNSET
        else:
            entry_format = RobloxLocalizationTablesApiEntryMetadataEntryFormat(_entry_format)

        roblox_localization_tables_api_entry_metadata = cls(
            example=example,
            game_locations=game_locations,
            entry_format=entry_format,
        )

        return roblox_localization_tables_api_entry_metadata
