from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePaymentProfileResponse")


@_attrs_define
class CreatePaymentProfileResponse:
    """Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.CreatePaymentProfileOperation

    Attributes:
        client_secret (None | str | Unset): Gets or sets the client secret to complete payment profile creation.
    """

    client_secret: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("clientSecret", UNSET))

        create_payment_profile_response = cls(
            client_secret=client_secret,
        )

        return create_payment_profile_response
