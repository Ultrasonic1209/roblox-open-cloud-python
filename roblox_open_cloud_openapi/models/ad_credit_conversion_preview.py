from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_credit_conversion_tier_breakdown import AdCreditConversionTierBreakdown
    from ..models.reason import Reason


T = TypeVar("T", bound="AdCreditConversionPreview")


@_attrs_define
class AdCreditConversionPreview:
    """
    Attributes:
        ad_credit_amount_micros (str): Ad credit that would be granted, in micro-USD.
        robux_amount (str): Robux that would be charged.
        valid (bool): False when the account can't afford the amount or it's outside the allowed range.
        effective_o18_robux (str | Unset): Portion of robuxAmount drawn from 18+ eligible Robux, which converts at the
            higher rate first.
        effective_standard_robux (str | Unset): Portion of robuxAmount drawn from standard Robux.
        reason (Reason | Unset):
        tier_breakdown (list[AdCreditConversionTierBreakdown] | Unset): One entry per rate tier used, in the order Robux
            are drawn.
    """

    ad_credit_amount_micros: str
    robux_amount: str
    valid: bool
    effective_o18_robux: str | Unset = UNSET
    effective_standard_robux: str | Unset = UNSET
    reason: Reason | Unset = UNSET
    tier_breakdown: list[AdCreditConversionTierBreakdown] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_credit_amount_micros = self.ad_credit_amount_micros

        robux_amount = self.robux_amount

        valid = self.valid

        effective_o18_robux = self.effective_o18_robux

        effective_standard_robux = self.effective_standard_robux

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        tier_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier_breakdown, Unset):
            tier_breakdown = []
            for tier_breakdown_item_data in self.tier_breakdown:
                tier_breakdown_item = tier_breakdown_item_data.to_dict()
                tier_breakdown.append(tier_breakdown_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adCreditAmountMicros": ad_credit_amount_micros,
                "robuxAmount": robux_amount,
                "valid": valid,
            }
        )
        if effective_o18_robux is not UNSET:
            field_dict["effectiveO18Robux"] = effective_o18_robux
        if effective_standard_robux is not UNSET:
            field_dict["effectiveStandardRobux"] = effective_standard_robux
        if reason is not UNSET:
            field_dict["reason"] = reason
        if tier_breakdown is not UNSET:
            field_dict["tierBreakdown"] = tier_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_credit_conversion_tier_breakdown import AdCreditConversionTierBreakdown  # noqa: PLC0415
        from ..models.reason import Reason  # noqa: PLC0415

        d = dict(src_dict)
        ad_credit_amount_micros = d.pop("adCreditAmountMicros")

        robux_amount = d.pop("robuxAmount")

        valid = d.pop("valid")

        effective_o18_robux = d.pop("effectiveO18Robux", UNSET)

        effective_standard_robux = d.pop("effectiveStandardRobux", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Reason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = Reason.from_dict(_reason)

        _tier_breakdown = d.pop("tierBreakdown", UNSET)
        tier_breakdown: list[AdCreditConversionTierBreakdown] | Unset = UNSET
        if _tier_breakdown is not UNSET:
            tier_breakdown = []
            for tier_breakdown_item_data in _tier_breakdown:
                tier_breakdown_item = AdCreditConversionTierBreakdown.from_dict(tier_breakdown_item_data)

                tier_breakdown.append(tier_breakdown_item)

        ad_credit_conversion_preview = cls(
            ad_credit_amount_micros=ad_credit_amount_micros,
            robux_amount=robux_amount,
            valid=valid,
            effective_o18_robux=effective_o18_robux,
            effective_standard_robux=effective_standard_robux,
            reason=reason,
            tier_breakdown=tier_breakdown,
        )

        ad_credit_conversion_preview.additional_properties = d
        return ad_credit_conversion_preview

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
