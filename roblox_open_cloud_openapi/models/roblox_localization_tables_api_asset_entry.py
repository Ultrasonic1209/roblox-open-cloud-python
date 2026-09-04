from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_in_game_content_tables_client_game_location import RobloxInGameContentTablesClientGameLocation
    from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation
    from ..models.roblox_localization_tables_api_translator import RobloxLocalizationTablesApiTranslator


T = TypeVar("T", bound="RobloxLocalizationTablesApiAssetEntry")


@_attrs_define
class RobloxLocalizationTablesApiAssetEntry:
    """A source asset (image) entry in a localization table, along with its per-locale asset
    translations. Unlike Roblox.LocalizationTables.Api.Entry, an asset entry is identified by its source asset
    id and has no key/context/source; each translation's Roblox.LocalizationTables.Api.Translation.TranslationText
    holds the translated asset id.

        Attributes:
            source_asset_id (int | Unset):
            asset_type (int | Unset):
            asset_class (int | Unset):
            asset_prop (int | Unset):
            translations (list[RobloxLocalizationTablesApiTranslation] | Unset):
            creator (RobloxLocalizationTablesApiTranslator | Unset):
            game_locations (list[RobloxInGameContentTablesClientGameLocation] | Unset):
            created_time (datetime.datetime | Unset):
    """

    source_asset_id: int | Unset = UNSET
    asset_type: int | Unset = UNSET
    asset_class: int | Unset = UNSET
    asset_prop: int | Unset = UNSET
    translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET
    creator: RobloxLocalizationTablesApiTranslator | Unset = UNSET
    game_locations: list[RobloxInGameContentTablesClientGameLocation] | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_asset_id = self.source_asset_id

        asset_type = self.asset_type

        asset_class = self.asset_class

        asset_prop = self.asset_prop

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        game_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.game_locations, Unset):
            game_locations = []
            for game_locations_item_data in self.game_locations:
                game_locations_item = game_locations_item_data.to_dict()
                game_locations.append(game_locations_item)

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_asset_id is not UNSET:
            field_dict["sourceAssetId"] = source_asset_id
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if asset_prop is not UNSET:
            field_dict["assetProp"] = asset_prop
        if translations is not UNSET:
            field_dict["translations"] = translations
        if creator is not UNSET:
            field_dict["creator"] = creator
        if game_locations is not UNSET:
            field_dict["gameLocations"] = game_locations
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_in_game_content_tables_client_game_location import (
            RobloxInGameContentTablesClientGameLocation,
        )
        from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation
        from ..models.roblox_localization_tables_api_translator import RobloxLocalizationTablesApiTranslator

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        source_asset_id = d.pop("sourceAssetId", UNSET)

        asset_type = d.pop("assetType", UNSET)

        asset_class = d.pop("assetClass", UNSET)

        asset_prop = d.pop("assetProp", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = RobloxLocalizationTablesApiTranslation.from_dict(translations_item_data)

                translations.append(translations_item)

        _creator = d.pop("creator", UNSET)
        creator: RobloxLocalizationTablesApiTranslator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxLocalizationTablesApiTranslator.from_dict(_creator)

        _game_locations = d.pop("gameLocations", UNSET)
        game_locations: list[RobloxInGameContentTablesClientGameLocation] | Unset = UNSET
        if _game_locations is not UNSET:
            game_locations = []
            for game_locations_item_data in _game_locations:
                game_locations_item = RobloxInGameContentTablesClientGameLocation.from_dict(game_locations_item_data)

                game_locations.append(game_locations_item)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        roblox_localization_tables_api_asset_entry = cls(
            source_asset_id=source_asset_id,
            asset_type=asset_type,
            asset_class=asset_class,
            asset_prop=asset_prop,
            translations=translations,
            creator=creator,
            game_locations=game_locations,
            created_time=created_time,
        )

        return roblox_localization_tables_api_asset_entry
