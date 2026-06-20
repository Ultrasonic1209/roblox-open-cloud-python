from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.transaction_records_api_currency_type import TransactionRecordsApiCurrencyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenericCurrencyResponse")


@_attrs_define
class GenericCurrencyResponse:
    """
    Attributes:
        amount (int | Unset):
        type_ (TransactionRecordsApiCurrencyType | Unset):
    """

    amount: int | Unset = UNSET
    type_: TransactionRecordsApiCurrencyType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        amount = d.pop("amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TransactionRecordsApiCurrencyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TransactionRecordsApiCurrencyType(_type_)

        generic_currency_response = cls(
            amount=amount,
            type_=type_,
        )

        return generic_currency_response
