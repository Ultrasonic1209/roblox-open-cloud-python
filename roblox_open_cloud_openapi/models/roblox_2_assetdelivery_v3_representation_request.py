from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_representation_item import Roblox2AssetdeliveryV3RepresentationItem


T = TypeVar("T", bound="Roblox2AssetdeliveryV3RepresentationRequest")


@_attrs_define
class Roblox2AssetdeliveryV3RepresentationRequest:
    """
    Attributes:
        priority_list (list[Roblox2AssetdeliveryV3RepresentationItem] | Unset):
        do_not_fallback_to_baseline (bool | Unset):
    """

    priority_list: list[Roblox2AssetdeliveryV3RepresentationItem] | Unset = UNSET
    do_not_fallback_to_baseline: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        priority_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.priority_list, Unset):
            priority_list = []
            for priority_list_item_data in self.priority_list:
                priority_list_item = priority_list_item_data.to_dict()
                priority_list.append(priority_list_item)

        do_not_fallback_to_baseline = self.do_not_fallback_to_baseline

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if priority_list is not UNSET:
            field_dict["priorityList"] = priority_list
        if do_not_fallback_to_baseline is not UNSET:
            field_dict["doNotFallbackToBaseline"] = do_not_fallback_to_baseline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_representation_item import Roblox2AssetdeliveryV3RepresentationItem  # noqa: PLC0415

        d = dict(src_dict)
        _priority_list = d.pop("priorityList", UNSET)
        priority_list: list[Roblox2AssetdeliveryV3RepresentationItem] | Unset = UNSET
        if _priority_list is not UNSET:
            priority_list = []
            for priority_list_item_data in _priority_list:
                priority_list_item = Roblox2AssetdeliveryV3RepresentationItem.from_dict(priority_list_item_data)

                priority_list.append(priority_list_item)

        do_not_fallback_to_baseline = d.pop("doNotFallbackToBaseline", UNSET)

        roblox_2_assetdelivery_v3_representation_request = cls(
            priority_list=priority_list,
            do_not_fallback_to_baseline=do_not_fallback_to_baseline,
        )

        return roblox_2_assetdelivery_v3_representation_request
