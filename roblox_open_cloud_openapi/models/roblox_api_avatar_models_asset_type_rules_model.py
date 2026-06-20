from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAssetTypeRulesModel")


@_attrs_define
class RobloxApiAvatarModelsAssetTypeRulesModel:
    """A model containing details about an asset type and its business rules

    Attributes:
        max_number (int | Unset): The max number of this asset type that can be worn
        id (int | Unset): The id
        name (str | Unset): The name
    """

    max_number: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_number = self.max_number

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_number is not UNSET:
            field_dict["maxNumber"] = max_number
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        max_number = d.pop("maxNumber", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        roblox_api_avatar_models_asset_type_rules_model = cls(
            max_number=max_number,
            id=id,
            name=name,
        )

        return roblox_api_avatar_models_asset_type_rules_model
