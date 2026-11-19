from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_revenue_split import RobloxItemConfigurationApiRevenueSplit


T = TypeVar("T", bound="RobloxItemConfigurationApiRevenueSplitTier")


@_attrs_define
class RobloxItemConfigurationApiRevenueSplitTier:
    """Tiered revenue split model.

    Attributes:
        price_floor_multiplier_lower_bound (float | Unset): Lower bound of the price floor multiplier for which this
            tier is applicable.
        price_floor_multiplier_upper_bound (float | Unset): Upper bound of the price floor multiplier for which this
            tier is applicable.
        revenue_splits (RobloxItemConfigurationApiRevenueSplit | Unset): Revenue split model.
    """

    price_floor_multiplier_lower_bound: float | Unset = UNSET
    price_floor_multiplier_upper_bound: float | Unset = UNSET
    revenue_splits: RobloxItemConfigurationApiRevenueSplit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_floor_multiplier_lower_bound = self.price_floor_multiplier_lower_bound

        price_floor_multiplier_upper_bound = self.price_floor_multiplier_upper_bound

        revenue_splits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revenue_splits, Unset):
            revenue_splits = self.revenue_splits.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_floor_multiplier_lower_bound is not UNSET:
            field_dict["priceFloorMultiplierLowerBound"] = price_floor_multiplier_lower_bound
        if price_floor_multiplier_upper_bound is not UNSET:
            field_dict["priceFloorMultiplierUpperBound"] = price_floor_multiplier_upper_bound
        if revenue_splits is not UNSET:
            field_dict["revenueSplits"] = revenue_splits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_revenue_split import RobloxItemConfigurationApiRevenueSplit  # noqa: PLC0415

        d = dict(src_dict)
        price_floor_multiplier_lower_bound = d.pop("priceFloorMultiplierLowerBound", UNSET)

        price_floor_multiplier_upper_bound = d.pop("priceFloorMultiplierUpperBound", UNSET)

        _revenue_splits = d.pop("revenueSplits", UNSET)
        revenue_splits: RobloxItemConfigurationApiRevenueSplit | Unset
        if isinstance(_revenue_splits, Unset):
            revenue_splits = UNSET
        else:
            revenue_splits = RobloxItemConfigurationApiRevenueSplit.from_dict(_revenue_splits)

        roblox_item_configuration_api_revenue_split_tier = cls(
            price_floor_multiplier_lower_bound=price_floor_multiplier_lower_bound,
            price_floor_multiplier_upper_bound=price_floor_multiplier_upper_bound,
            revenue_splits=revenue_splits,
        )

        return roblox_item_configuration_api_revenue_split_tier
