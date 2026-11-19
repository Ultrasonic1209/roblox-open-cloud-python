from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_prewarm_place_target import Roblox2AssetdeliveryV3PrewarmPlaceTarget


T = TypeVar("T", bound="Roblox2AssetdeliveryV3PrewarmTarget")


@_attrs_define
class Roblox2AssetdeliveryV3PrewarmTarget:
    """
    Attributes:
        place (Roblox2AssetdeliveryV3PrewarmPlaceTarget | Unset):
    """

    place: Roblox2AssetdeliveryV3PrewarmPlaceTarget | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place is not UNSET:
            field_dict["place"] = place

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_prewarm_place_target import Roblox2AssetdeliveryV3PrewarmPlaceTarget  # noqa: PLC0415

        d = dict(src_dict)
        _place = d.pop("place", UNSET)
        place: Roblox2AssetdeliveryV3PrewarmPlaceTarget | Unset
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = Roblox2AssetdeliveryV3PrewarmPlaceTarget.from_dict(_place)

        roblox_2_assetdelivery_v3_prewarm_target = cls(
            place=place,
        )

        return roblox_2_assetdelivery_v3_prewarm_target
