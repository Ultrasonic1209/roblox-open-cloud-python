from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiUniverseResponse")


@_attrs_define
class RobloxBadgesApiUniverseResponse:
    """A response containing universe information.

    Attributes:
        id (int | Unset): The universe Id.
        name (str | Unset): The universe name.
        root_place_id (int | Unset): The description of the universe.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    root_place_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        root_place_id = self.root_place_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        root_place_id = d.pop("rootPlaceId", UNSET)

        roblox_badges_api_universe_response = cls(
            id=id,
            name=name,
            root_place_id=root_place_id,
        )

        return roblox_badges_api_universe_response
