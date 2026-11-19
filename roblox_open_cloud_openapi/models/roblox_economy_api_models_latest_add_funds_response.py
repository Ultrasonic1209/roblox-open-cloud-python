from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxEconomyApiModelsLatestAddFundsResponse")


@_attrs_define
class RobloxEconomyApiModelsLatestAddFundsResponse:
    """
    Attributes:
        transaction_date (str | Unset): Date of latest transfer
        rate_limit_in_days (int | Unset): Days from the last transfer a new transfer is allowed
    """

    transaction_date: str | Unset = UNSET
    rate_limit_in_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        transaction_date = self.transaction_date

        rate_limit_in_days = self.rate_limit_in_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if rate_limit_in_days is not UNSET:
            field_dict["rateLimitInDays"] = rate_limit_in_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_date = d.pop("transactionDate", UNSET)

        rate_limit_in_days = d.pop("rateLimitInDays", UNSET)

        roblox_economy_api_models_latest_add_funds_response = cls(
            transaction_date=transaction_date,
            rate_limit_in_days=rate_limit_in_days,
        )

        return roblox_economy_api_models_latest_add_funds_response
