from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_watermark_contribution_request_balance_key import (
    RobloxGroupsApiWatermarkContributionRequestBalanceKey,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiWatermarkContributionRequest")


@_attrs_define
class RobloxGroupsApiWatermarkContributionRequest:
    """
    Attributes:
        balance_key (RobloxGroupsApiWatermarkContributionRequestBalanceKey | Unset):  ['Standard' = 1, 'O18Boosted' = 2]
        amount (int | Unset):
    """

    balance_key: RobloxGroupsApiWatermarkContributionRequestBalanceKey | Unset = UNSET
    amount: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        balance_key: str | Unset = UNSET
        if not isinstance(self.balance_key, Unset):
            balance_key = self.balance_key.value

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if balance_key is not UNSET:
            field_dict["balanceKey"] = balance_key
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _balance_key = d.pop("balanceKey", UNSET)
        balance_key: RobloxGroupsApiWatermarkContributionRequestBalanceKey | Unset
        if isinstance(_balance_key, Unset):
            balance_key = UNSET
        else:
            balance_key = RobloxGroupsApiWatermarkContributionRequestBalanceKey(_balance_key)

        amount = d.pop("amount", UNSET)

        roblox_groups_api_watermark_contribution_request = cls(
            balance_key=balance_key,
            amount=amount,
        )

        return roblox_groups_api_watermark_contribution_request
