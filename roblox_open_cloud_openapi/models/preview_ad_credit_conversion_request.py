from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewAdCreditConversionRequest")


@_attrs_define
class PreviewAdCreditConversionRequest:
    """
    Attributes:
        ad_credit_amount_micros (str | Unset): Ad credit wanted, at most cent precision; the preview returns the Robux
            it costs.
        robux_amount (str | Unset): Robux to spend; the preview returns the ad credit it buys.
    """

    ad_credit_amount_micros: str | Unset = UNSET
    robux_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_credit_amount_micros = self.ad_credit_amount_micros

        robux_amount = self.robux_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_credit_amount_micros is not UNSET:
            field_dict["adCreditAmountMicros"] = ad_credit_amount_micros
        if robux_amount is not UNSET:
            field_dict["robuxAmount"] = robux_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_credit_amount_micros = d.pop("adCreditAmountMicros", UNSET)

        robux_amount = d.pop("robuxAmount", UNSET)

        preview_ad_credit_conversion_request = cls(
            ad_credit_amount_micros=ad_credit_amount_micros,
            robux_amount=robux_amount,
        )

        preview_ad_credit_conversion_request.additional_properties = d
        return preview_ad_credit_conversion_request

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
