from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ad_credit_conversion_tier_breakdown_tier import AdCreditConversionTierBreakdownTier

T = TypeVar("T", bound="AdCreditConversionTierBreakdown")


@_attrs_define
class AdCreditConversionTierBreakdown:
    """
    Attributes:
        ad_credit_amount_micros (str): Ad credit granted from this tier, in micro-USD.
        ad_credit_per_robux (float): USD of ad credit per Robux in this tier.
        robux_amount (str): Robux converted in this tier.
        tier (AdCreditConversionTierBreakdownTier): Rate tier (`O18_ELIGIBLE_ROBUX` or `STANDARD_ROBUX`).
    """

    ad_credit_amount_micros: str
    ad_credit_per_robux: float
    robux_amount: str
    tier: AdCreditConversionTierBreakdownTier
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_credit_amount_micros = self.ad_credit_amount_micros

        ad_credit_per_robux = self.ad_credit_per_robux

        robux_amount = self.robux_amount

        tier = self.tier.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adCreditAmountMicros": ad_credit_amount_micros,
                "adCreditPerRobux": ad_credit_per_robux,
                "robuxAmount": robux_amount,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_credit_amount_micros = d.pop("adCreditAmountMicros")

        ad_credit_per_robux = d.pop("adCreditPerRobux")

        robux_amount = d.pop("robuxAmount")

        tier = AdCreditConversionTierBreakdownTier(d.pop("tier"))

        ad_credit_conversion_tier_breakdown = cls(
            ad_credit_amount_micros=ad_credit_amount_micros,
            ad_credit_per_robux=ad_credit_per_robux,
            robux_amount=robux_amount,
            tier=tier,
        )

        ad_credit_conversion_tier_breakdown.additional_properties = d
        return ad_credit_conversion_tier_breakdown

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
