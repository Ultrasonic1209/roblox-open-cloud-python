from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_payout_recipient_request_recipient_type import (
    RobloxGroupsApiPayoutRecipientRequestRecipientType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiPayoutRecipientRequest")


@_attrs_define
class RobloxGroupsApiPayoutRecipientRequest:
    """A request model for paying out Robux.

    Attributes:
        recipient_id (int | Unset): The recipient id.
        recipient_type (RobloxGroupsApiPayoutRecipientRequestRecipientType | Unset): The recipient type. ['User' = 0,
            'Group' = 1]
        amount (int | Unset): The amount to payout.
    """

    recipient_id: int | Unset = UNSET
    recipient_type: RobloxGroupsApiPayoutRecipientRequestRecipientType | Unset = UNSET
    amount: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recipient_id = self.recipient_id

        recipient_type: int | Unset = UNSET
        if not isinstance(self.recipient_type, Unset):
            recipient_type = self.recipient_type.value

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if recipient_type is not UNSET:
            field_dict["recipientType"] = recipient_type
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient_id = d.pop("recipientId", UNSET)

        _recipient_type = d.pop("recipientType", UNSET)
        recipient_type: RobloxGroupsApiPayoutRecipientRequestRecipientType | Unset
        if isinstance(_recipient_type, Unset):
            recipient_type = UNSET
        else:
            recipient_type = RobloxGroupsApiPayoutRecipientRequestRecipientType(_recipient_type)

        amount = d.pop("amount", UNSET)

        roblox_groups_api_payout_recipient_request = cls(
            recipient_id=recipient_id,
            recipient_type=recipient_type,
            amount=amount,
        )

        return roblox_groups_api_payout_recipient_request
