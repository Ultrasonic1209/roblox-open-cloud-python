from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse")


@_attrs_define
class RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse:
    """A response model for updating badge name and description

    Attributes:
        name (str | Unset): Badge name saved
        description (str | Unset): Badge description saved
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        roblox_game_internationalization_api_update_badge_name_description_response = cls(
            name=name,
            description=description,
        )

        return roblox_game_internationalization_api_update_badge_name_description_response
