from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaceModel")


@_attrs_define
class RobloxApiDevelopModelsPlaceModel:
    """A model containing information about a place

    Attributes:
        id (int | Unset): Returns the place id.
        universe_id (int | Unset): Returns the id of the place's universe, or null - if the place is not part of a
            universe.
        name (str | Unset): Returns the place name.
        description (str | Unset): Returns the place description.
    """

    id: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        universe_id = self.universe_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        universe_id = d.pop("universeId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        roblox_api_develop_models_place_model = cls(
            id=id,
            universe_id=universe_id,
            name=name,
            description=description,
        )

        return roblox_api_develop_models_place_model
