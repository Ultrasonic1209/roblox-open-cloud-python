from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SubmitManualPaymentResponse")


@_attrs_define
class SubmitManualPaymentResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.SubmitManualPaymentOperation"""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        submit_manual_payment_response = cls()

        return submit_manual_payment_response
