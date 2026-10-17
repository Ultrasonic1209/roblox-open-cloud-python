from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_profile import PaymentProfile


T = TypeVar("T", bound="ListPaymentProfilesResponse")


@_attrs_define
class ListPaymentProfilesResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.ListPaymentProfilesOperation.

    Attributes:
        payment_profiles (list[PaymentProfile] | None | Unset): Gets or sets the payment profiles owned by the provided
            creator.
    """

    payment_profiles: list[PaymentProfile] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payment_profiles: list[dict[str, Any]] | None | Unset
        if isinstance(self.payment_profiles, Unset):
            payment_profiles = UNSET
        elif isinstance(self.payment_profiles, list):
            payment_profiles = []
            for payment_profiles_type_0_item_data in self.payment_profiles:
                payment_profiles_type_0_item = payment_profiles_type_0_item_data.to_dict()
                payment_profiles.append(payment_profiles_type_0_item)

        else:
            payment_profiles = self.payment_profiles

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payment_profiles is not UNSET:
            field_dict["paymentProfiles"] = payment_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_profile import PaymentProfile

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_payment_profiles(data: object) -> list[PaymentProfile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_profiles_type_0 = []
                _payment_profiles_type_0 = data
                for payment_profiles_type_0_item_data in _payment_profiles_type_0:
                    payment_profiles_type_0_item = PaymentProfile.from_dict(payment_profiles_type_0_item_data)

                    payment_profiles_type_0.append(payment_profiles_type_0_item)

                return payment_profiles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PaymentProfile] | None | Unset, data)

        payment_profiles = _parse_payment_profiles(d.pop("paymentProfiles", UNSET))

        list_payment_profiles_response = cls(
            payment_profiles=payment_profiles,
        )

        return list_payment_profiles_response
