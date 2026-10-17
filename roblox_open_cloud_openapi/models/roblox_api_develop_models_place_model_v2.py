from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_place_model_v2_allowed_gear_types_item import (
    RobloxApiDevelopModelsPlaceModelV2AllowedGearTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaceModelV2")


@_attrs_define
class RobloxApiDevelopModelsPlaceModelV2:
    """A model containing information about a place

    Attributes:
        max_player_count (int | Unset): The max number of players for the place.
        social_slot_type (str | Unset): The social slot type for the place. Determines how users are placed into
            servers.
             Examples:
                 Automatic,
                 Empty,
                 Custom
        custom_social_slots_count (int | Unset): The number of social slots for the place when the slot type is custom.
        allow_copying (bool | Unset): Determines if copying of the place is allowed.
        current_saved_version (int | Unset): The current saved version number of the place.
        is_all_genres_allowed (bool | Unset): Whether all genres allowed in the place.
        allowed_gear_types (list[RobloxApiDevelopModelsPlaceModelV2AllowedGearTypesItem] | Unset): Types of Roblox gear
            that are allowed to exist in the place.
            Valid values are from amp::AssetCategory
        max_players_allowed (int | Unset): The maximum allowed number of players for the place that the user can set,
            based on user roleset.
        created (datetime.datetime | Unset): The time place was created.
        updated (datetime.datetime | Unset): The time place was updated.
        id (int | Unset): Returns the place id.
        universe_id (int | Unset): Returns the id of the place's universe, or null - if the place is not part of a
            universe.
        name (str | Unset): Returns the place name.
        description (str | Unset): Returns the place description.
        is_root_place (bool | Unset): Returns whether this place is the root place.
    """

    max_player_count: int | Unset = UNSET
    social_slot_type: str | Unset = UNSET
    custom_social_slots_count: int | Unset = UNSET
    allow_copying: bool | Unset = UNSET
    current_saved_version: int | Unset = UNSET
    is_all_genres_allowed: bool | Unset = UNSET
    allowed_gear_types: list[RobloxApiDevelopModelsPlaceModelV2AllowedGearTypesItem] | Unset = UNSET
    max_players_allowed: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    is_root_place: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_player_count = self.max_player_count

        social_slot_type = self.social_slot_type

        custom_social_slots_count = self.custom_social_slots_count

        allow_copying = self.allow_copying

        current_saved_version = self.current_saved_version

        is_all_genres_allowed = self.is_all_genres_allowed

        allowed_gear_types: list[int] | Unset = UNSET
        if not isinstance(self.allowed_gear_types, Unset):
            allowed_gear_types = []
            for allowed_gear_types_item_data in self.allowed_gear_types:
                allowed_gear_types_item = allowed_gear_types_item_data.value
                allowed_gear_types.append(allowed_gear_types_item)

        max_players_allowed = self.max_players_allowed

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        id = self.id

        universe_id = self.universe_id

        name = self.name

        description = self.description

        is_root_place = self.is_root_place

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_player_count is not UNSET:
            field_dict["maxPlayerCount"] = max_player_count
        if social_slot_type is not UNSET:
            field_dict["socialSlotType"] = social_slot_type
        if custom_social_slots_count is not UNSET:
            field_dict["customSocialSlotsCount"] = custom_social_slots_count
        if allow_copying is not UNSET:
            field_dict["allowCopying"] = allow_copying
        if current_saved_version is not UNSET:
            field_dict["currentSavedVersion"] = current_saved_version
        if is_all_genres_allowed is not UNSET:
            field_dict["isAllGenresAllowed"] = is_all_genres_allowed
        if allowed_gear_types is not UNSET:
            field_dict["allowedGearTypes"] = allowed_gear_types
        if max_players_allowed is not UNSET:
            field_dict["maxPlayersAllowed"] = max_players_allowed
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_root_place is not UNSET:
            field_dict["isRootPlace"] = is_root_place

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_player_count = d.pop("maxPlayerCount", UNSET)

        social_slot_type = d.pop("socialSlotType", UNSET)

        custom_social_slots_count = d.pop("customSocialSlotsCount", UNSET)

        allow_copying = d.pop("allowCopying", UNSET)

        current_saved_version = d.pop("currentSavedVersion", UNSET)

        is_all_genres_allowed = d.pop("isAllGenresAllowed", UNSET)

        _allowed_gear_types = d.pop("allowedGearTypes", UNSET)
        allowed_gear_types: list[RobloxApiDevelopModelsPlaceModelV2AllowedGearTypesItem] | Unset = UNSET
        if _allowed_gear_types is not UNSET:
            allowed_gear_types = []
            for allowed_gear_types_item_data in _allowed_gear_types:
                allowed_gear_types_item = RobloxApiDevelopModelsPlaceModelV2AllowedGearTypesItem(
                    allowed_gear_types_item_data
                )

                allowed_gear_types.append(allowed_gear_types_item)

        max_players_allowed = d.pop("maxPlayersAllowed", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        id = d.pop("id", UNSET)

        universe_id = d.pop("universeId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_root_place = d.pop("isRootPlace", UNSET)

        roblox_api_develop_models_place_model_v2 = cls(
            max_player_count=max_player_count,
            social_slot_type=social_slot_type,
            custom_social_slots_count=custom_social_slots_count,
            allow_copying=allow_copying,
            current_saved_version=current_saved_version,
            is_all_genres_allowed=is_all_genres_allowed,
            allowed_gear_types=allowed_gear_types,
            max_players_allowed=max_players_allowed,
            created=created,
            updated=updated,
            id=id,
            universe_id=universe_id,
            name=name,
            description=description,
            is_root_place=is_root_place,
        )

        return roblox_api_develop_models_place_model_v2
