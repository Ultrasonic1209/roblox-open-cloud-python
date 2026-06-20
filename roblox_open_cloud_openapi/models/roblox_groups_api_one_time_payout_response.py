from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_one_time_payout_response_status import RobloxGroupsApiOneTimePayoutResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiOneTimePayoutResponse")


@_attrs_define
class RobloxGroupsApiOneTimePayoutResponse:
    """Response model for one-time payout requests.

    Attributes:
        status (RobloxGroupsApiOneTimePayoutResponseStatus | Unset): One-time payout status. ['NotHeld' = 0, 'Held' = 1]
    """

    status: RobloxGroupsApiOneTimePayoutResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _status = d.pop("status", UNSET)
        status: RobloxGroupsApiOneTimePayoutResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxGroupsApiOneTimePayoutResponseStatus(_status)

        roblox_groups_api_one_time_payout_response = cls(
            status=status,
        )

        return roblox_groups_api_one_time_payout_response
