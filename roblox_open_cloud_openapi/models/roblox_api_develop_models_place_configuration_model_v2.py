from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaceConfigurationModelV2")


@_attrs_define
class RobloxApiDevelopModelsPlaceConfigurationModelV2:
    """A model containing information about a place to be configured

    Attributes:
        name (str | Unset): The name for the place.
        description (str | Unset): The new description for the place.
        max_player_count (int | Unset): The max number of players for the place.
        social_slot_type (str | Unset): The social slot type for the place. Determines how users are placed into
            servers.
             Examples:
                 Automatic,
                 Empty,
                 Custom
        custom_social_slots_count (int | Unset): The number of social slots for the place when the slot type is custom.
        allow_copying (bool | Unset): Determines if copying of the place is allowed.
        allowed_gear_types (list[str] | Unset): List of allowed gear types
        is_all_genres_allowed (bool | Unset): If all genres are allowed, or only the experience type
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    max_player_count: int | Unset = UNSET
    social_slot_type: str | Unset = UNSET
    custom_social_slots_count: int | Unset = UNSET
    allow_copying: bool | Unset = UNSET
    allowed_gear_types: list[str] | Unset = UNSET
    is_all_genres_allowed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        max_player_count = self.max_player_count

        social_slot_type = self.social_slot_type

        custom_social_slots_count = self.custom_social_slots_count

        allow_copying = self.allow_copying

        allowed_gear_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_gear_types, Unset):
            allowed_gear_types = self.allowed_gear_types

        is_all_genres_allowed = self.is_all_genres_allowed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if max_player_count is not UNSET:
            field_dict["maxPlayerCount"] = max_player_count
        if social_slot_type is not UNSET:
            field_dict["socialSlotType"] = social_slot_type
        if custom_social_slots_count is not UNSET:
            field_dict["customSocialSlotsCount"] = custom_social_slots_count
        if allow_copying is not UNSET:
            field_dict["allowCopying"] = allow_copying
        if allowed_gear_types is not UNSET:
            field_dict["allowedGearTypes"] = allowed_gear_types
        if is_all_genres_allowed is not UNSET:
            field_dict["isAllGenresAllowed"] = is_all_genres_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        max_player_count = d.pop("maxPlayerCount", UNSET)

        social_slot_type = d.pop("socialSlotType", UNSET)

        custom_social_slots_count = d.pop("customSocialSlotsCount", UNSET)

        allow_copying = d.pop("allowCopying", UNSET)

        allowed_gear_types = cast(list[str], d.pop("allowedGearTypes", UNSET))

        is_all_genres_allowed = d.pop("isAllGenresAllowed", UNSET)

        roblox_api_develop_models_place_configuration_model_v2 = cls(
            name=name,
            description=description,
            max_player_count=max_player_count,
            social_slot_type=social_slot_type,
            custom_social_slots_count=custom_social_slots_count,
            allow_copying=allow_copying,
            allowed_gear_types=allowed_gear_types,
            is_all_genres_allowed=is_all_genres_allowed,
        )

        return roblox_api_develop_models_place_configuration_model_v2
