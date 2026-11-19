from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3PrewarmPlaceTarget")


@_attrs_define
class Roblox2AssetdeliveryV3PrewarmPlaceTarget:
    """
    Attributes:
        place_id (int | Unset):
    """

    place_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("placeId", UNSET)

        roblox_2_assetdelivery_v3_prewarm_place_target = cls(
            place_id=place_id,
        )

        return roblox_2_assetdelivery_v3_prewarm_place_target
