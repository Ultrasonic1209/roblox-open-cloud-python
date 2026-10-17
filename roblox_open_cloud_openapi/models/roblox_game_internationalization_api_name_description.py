from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_name_description_update_type import (
    RobloxGameInternationalizationApiNameDescriptionUpdateType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiNameDescription")


@_attrs_define
class RobloxGameInternationalizationApiNameDescription:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        update_type (RobloxGameInternationalizationApiNameDescriptionUpdateType | Unset):
        language_code (str | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    update_type: RobloxGameInternationalizationApiNameDescriptionUpdateType | Unset = UNSET
    language_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        update_type: str | Unset = UNSET
        if not isinstance(self.update_type, Unset):
            update_type = self.update_type.value

        language_code = self.language_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if update_type is not UNSET:
            field_dict["updateType"] = update_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _update_type = d.pop("updateType", UNSET)
        update_type: RobloxGameInternationalizationApiNameDescriptionUpdateType | Unset
        if isinstance(_update_type, Unset):
            update_type = UNSET
        else:
            update_type = RobloxGameInternationalizationApiNameDescriptionUpdateType(_update_type)

        language_code = d.pop("languageCode", UNSET)

        roblox_game_internationalization_api_name_description = cls(
            name=name,
            description=description,
            update_type=update_type,
            language_code=language_code,
        )

        return roblox_game_internationalization_api_name_description
