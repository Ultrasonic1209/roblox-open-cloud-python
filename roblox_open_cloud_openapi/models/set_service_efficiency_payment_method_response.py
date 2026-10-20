from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetServiceEfficiencyPaymentMethodResponse")


@_attrs_define
class SetServiceEfficiencyPaymentMethodResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.SetServiceEfficiencyPaymentMethodOperation"""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        set_service_efficiency_payment_method_response = cls()

        return set_service_efficiency_payment_method_response
