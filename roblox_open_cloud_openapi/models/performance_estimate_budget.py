from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.performance_estimate_money_range import PerformanceEstimateMoneyRange


T = TypeVar("T", bound="PerformanceEstimateBudget")


@_attrs_define
class PerformanceEstimateBudget:
    """
    Attributes:
        daily_amount_micro_usd (str | Unset): Daily budget in micro-USD, as a decimal string.
        daily_amount_micro_usd_range (PerformanceEstimateMoneyRange | Unset):
        lifetime_amount_micro_usd (str | Unset): Lifetime budget in micro-USD, as a decimal string. Omitted for a daily
            budget.
        lifetime_amount_micro_usd_range (PerformanceEstimateMoneyRange | Unset):
    """

    daily_amount_micro_usd: str | Unset = UNSET
    daily_amount_micro_usd_range: PerformanceEstimateMoneyRange | Unset = UNSET
    lifetime_amount_micro_usd: str | Unset = UNSET
    lifetime_amount_micro_usd_range: PerformanceEstimateMoneyRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_amount_micro_usd = self.daily_amount_micro_usd

        daily_amount_micro_usd_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_amount_micro_usd_range, Unset):
            daily_amount_micro_usd_range = self.daily_amount_micro_usd_range.to_dict()

        lifetime_amount_micro_usd = self.lifetime_amount_micro_usd

        lifetime_amount_micro_usd_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lifetime_amount_micro_usd_range, Unset):
            lifetime_amount_micro_usd_range = self.lifetime_amount_micro_usd_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_amount_micro_usd is not UNSET:
            field_dict["dailyAmountMicroUsd"] = daily_amount_micro_usd
        if daily_amount_micro_usd_range is not UNSET:
            field_dict["dailyAmountMicroUsdRange"] = daily_amount_micro_usd_range
        if lifetime_amount_micro_usd is not UNSET:
            field_dict["lifetimeAmountMicroUsd"] = lifetime_amount_micro_usd
        if lifetime_amount_micro_usd_range is not UNSET:
            field_dict["lifetimeAmountMicroUsdRange"] = lifetime_amount_micro_usd_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_money_range import PerformanceEstimateMoneyRange  # noqa: PLC0415

        d = dict(src_dict)
        daily_amount_micro_usd = d.pop("dailyAmountMicroUsd", UNSET)

        _daily_amount_micro_usd_range = d.pop("dailyAmountMicroUsdRange", UNSET)
        daily_amount_micro_usd_range: PerformanceEstimateMoneyRange | Unset
        if isinstance(_daily_amount_micro_usd_range, Unset):
            daily_amount_micro_usd_range = UNSET
        else:
            daily_amount_micro_usd_range = PerformanceEstimateMoneyRange.from_dict(_daily_amount_micro_usd_range)

        lifetime_amount_micro_usd = d.pop("lifetimeAmountMicroUsd", UNSET)

        _lifetime_amount_micro_usd_range = d.pop("lifetimeAmountMicroUsdRange", UNSET)
        lifetime_amount_micro_usd_range: PerformanceEstimateMoneyRange | Unset
        if isinstance(_lifetime_amount_micro_usd_range, Unset):
            lifetime_amount_micro_usd_range = UNSET
        else:
            lifetime_amount_micro_usd_range = PerformanceEstimateMoneyRange.from_dict(_lifetime_amount_micro_usd_range)

        performance_estimate_budget = cls(
            daily_amount_micro_usd=daily_amount_micro_usd,
            daily_amount_micro_usd_range=daily_amount_micro_usd_range,
            lifetime_amount_micro_usd=lifetime_amount_micro_usd,
            lifetime_amount_micro_usd_range=lifetime_amount_micro_usd_range,
        )

        performance_estimate_budget.additional_properties = d
        return performance_estimate_budget

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
