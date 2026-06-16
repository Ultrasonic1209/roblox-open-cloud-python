from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiModelsUniverseModel")


@_attrs_define
class RobloxAdConfigurationApiModelsUniverseModel:
    """Represents a universe in API endpoint results.

    Attributes:
        id (int | Unset): The universe Id.
        name (str | Unset): The name of the universe
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        roblox_ad_configuration_api_models_universe_model = cls(
            id=id,
            name=name,
        )

        return roblox_ad_configuration_api_models_universe_model
