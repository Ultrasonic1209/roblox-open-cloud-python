from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.fetch_status import FetchStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_one_time_payout import PublicOneTimePayout


T = TypeVar("T", bound="PublicOneTimePayoutResponseModel")


@_attrs_define
class PublicOneTimePayoutResponseModel:
    """A one-time payout result in the public groups API contract.

    Attributes:
        recipient_user_id (int | Unset):
        status (FetchStatus | Unset): Describes whether a fetch operation failed or succeeded.
        one_time_payout (PublicOneTimePayout | Unset): One-time payout details in the public groups API contract.
    """

    recipient_user_id: int | Unset = UNSET
    status: FetchStatus | Unset = UNSET
    one_time_payout: PublicOneTimePayout | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recipient_user_id = self.recipient_user_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        one_time_payout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.one_time_payout, Unset):
            one_time_payout = self.one_time_payout.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recipient_user_id is not UNSET:
            field_dict["recipientUserId"] = recipient_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if one_time_payout is not UNSET:
            field_dict["oneTimePayout"] = one_time_payout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_one_time_payout import PublicOneTimePayout

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        recipient_user_id = d.pop("recipientUserId", UNSET)

        _status = d.pop("status", UNSET)
        status: FetchStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FetchStatus(_status)

        _one_time_payout = d.pop("oneTimePayout", UNSET)
        one_time_payout: PublicOneTimePayout | Unset
        if isinstance(_one_time_payout, Unset):
            one_time_payout = UNSET
        else:
            one_time_payout = PublicOneTimePayout.from_dict(_one_time_payout)

        public_one_time_payout_response_model = cls(
            recipient_user_id=recipient_user_id,
            status=status,
            one_time_payout=one_time_payout,
        )

        return public_one_time_payout_response_model
