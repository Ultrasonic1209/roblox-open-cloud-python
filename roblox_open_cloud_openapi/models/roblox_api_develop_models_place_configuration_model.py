from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaceConfigurationModel")


@_attrs_define
class RobloxApiDevelopModelsPlaceConfigurationModel:
    """A model containing information about a place to be configured

    Attributes:
        name (str | Unset): The name for the place.
        description (str | Unset): The new description for the place.
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

        roblox_api_develop_models_place_configuration_model = cls(
            name=name,
            description=description,
        )

        return roblox_api_develop_models_place_configuration_model
