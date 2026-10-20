from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_profile import PaymentProfile


T = TypeVar("T", bound="GetServiceEfficiencyPaymentMethodResponse")


@_attrs_define
class GetServiceEfficiencyPaymentMethodResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.GetServiceEfficiencyPaymentMethodOperation

    Attributes:
        payment_profile (None | PaymentProfile | Unset): Gets or sets the payment profile set for Service Efficiency use
            for the provided creator.
    """

    payment_profile: None | PaymentProfile | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_profile import PaymentProfile  # noqa: PLC0415

        payment_profile: dict[str, Any] | None | Unset
        if isinstance(self.payment_profile, Unset):
            payment_profile = UNSET
        elif isinstance(self.payment_profile, PaymentProfile):
            payment_profile = self.payment_profile.to_dict()
        else:
            payment_profile = self.payment_profile

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payment_profile is not UNSET:
            field_dict["paymentProfile"] = payment_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_profile import PaymentProfile  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_payment_profile(data: object) -> None | PaymentProfile | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_profile_type_1 = PaymentProfile.from_dict(data)

                return payment_profile_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaymentProfile | Unset, data)

        payment_profile = _parse_payment_profile(d.pop("paymentProfile", UNSET))

        get_service_efficiency_payment_method_response = cls(
            payment_profile=payment_profile,
        )

        return get_service_efficiency_payment_method_response
