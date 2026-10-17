from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsOutfitModel")


@_attrs_define
class RobloxApiAvatarModelsOutfitModel:
    """A slim model for user outfits.

    Attributes:
        id (int | Unset): The id.
        name (str | Unset): The name.
        is_editable (bool | Unset): Whether the outfit can be modified by the user.
        outfit_type (str | Unset): The type of the Outfit.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    is_editable: bool | Unset = UNSET
    outfit_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_editable = self.is_editable

        outfit_type = self.outfit_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if outfit_type is not UNSET:
            field_dict["outfitType"] = outfit_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_editable = d.pop("isEditable", UNSET)

        outfit_type = d.pop("outfitType", UNSET)

        roblox_api_avatar_models_outfit_model = cls(
            id=id,
            name=name,
            is_editable=is_editable,
            outfit_type=outfit_type,
        )

        return roblox_api_avatar_models_outfit_model
