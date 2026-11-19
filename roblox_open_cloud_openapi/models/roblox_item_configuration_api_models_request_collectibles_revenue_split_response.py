from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_revenue_split import RobloxItemConfigurationApiRevenueSplit


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse:
    """Response model for Revenue Split.

    Attributes:
        revenue_split (RobloxItemConfigurationApiRevenueSplit | Unset): Revenue split model.
    """

    revenue_split: RobloxItemConfigurationApiRevenueSplit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        revenue_split: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revenue_split, Unset):
            revenue_split = self.revenue_split.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if revenue_split is not UNSET:
            field_dict["RevenueSplit"] = revenue_split

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_revenue_split import RobloxItemConfigurationApiRevenueSplit  # noqa: PLC0415

        d = dict(src_dict)
        _revenue_split = d.pop("RevenueSplit", UNSET)
        revenue_split: RobloxItemConfigurationApiRevenueSplit | Unset
        if isinstance(_revenue_split, Unset):
            revenue_split = UNSET
        else:
            revenue_split = RobloxItemConfigurationApiRevenueSplit.from_dict(_revenue_split)

        roblox_item_configuration_api_models_request_collectibles_revenue_split_response = cls(
            revenue_split=revenue_split,
        )

        return roblox_item_configuration_api_models_request_collectibles_revenue_split_response
