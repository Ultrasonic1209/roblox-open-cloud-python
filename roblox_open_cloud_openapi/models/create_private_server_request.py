from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePrivateServerRequest")


@_attrs_define
class CreatePrivateServerRequest:
    """
    Attributes:
        name (None | str | Unset):
        expected_price (int | Unset):
        is_purchase_confirmed (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    expected_price: int | Unset = UNSET
    is_purchase_confirmed: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        expected_price = self.expected_price

        is_purchase_confirmed: bool | None | Unset
        if isinstance(self.is_purchase_confirmed, Unset):
            is_purchase_confirmed = UNSET
        else:
            is_purchase_confirmed = self.is_purchase_confirmed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if expected_price is not UNSET:
            field_dict["expectedPrice"] = expected_price
        if is_purchase_confirmed is not UNSET:
            field_dict["isPurchaseConfirmed"] = is_purchase_confirmed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        expected_price = d.pop("expectedPrice", UNSET)

        def _parse_is_purchase_confirmed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_purchase_confirmed = _parse_is_purchase_confirmed(d.pop("isPurchaseConfirmed", UNSET))

        create_private_server_request = cls(
            name=name,
            expected_price=expected_price,
            is_purchase_confirmed=is_purchase_confirmed,
        )

        return create_private_server_request
