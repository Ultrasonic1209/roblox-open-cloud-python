from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_trade_response_status import RobloxTradesApiTradeResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse


T = TypeVar("T", bound="RobloxTradesApiTradeResponse")


@_attrs_define
class RobloxTradesApiTradeResponse:
    """
    Attributes:
        id (int | Unset):
        user (RobloxWebResponsesUsersSkinnyUserResponse | Unset):
        created (datetime.datetime | Unset):
        expiration (datetime.datetime | Unset):
        is_active (bool | Unset):
        status (RobloxTradesApiTradeResponseStatus | Unset):  ['Unknown' = 1, 'Open' = 2, 'Pending' = 3, 'Completed' =
            4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered' = 8, 'Processing' = 9,
            'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11]
    """

    id: int | Unset = UNSET
    user: RobloxWebResponsesUsersSkinnyUserResponse | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    expiration: datetime.datetime | Unset = UNSET
    is_active: bool | Unset = UNSET
    status: RobloxTradesApiTradeResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        expiration: str | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.isoformat()

        is_active = self.is_active

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user
        if created is not UNSET:
            field_dict["created"] = created
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _user = d.pop("user", UNSET)
        user: RobloxWebResponsesUsersSkinnyUserResponse | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxWebResponsesUsersSkinnyUserResponse.from_dict(_user)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _expiration = d.pop("expiration", UNSET)
        expiration: datetime.datetime | Unset
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = datetime.datetime.fromisoformat(_expiration)

        is_active = d.pop("isActive", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxTradesApiTradeResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxTradesApiTradeResponseStatus(_status)

        roblox_trades_api_trade_response = cls(
            id=id,
            user=user,
            created=created,
            expiration=expiration,
            is_active=is_active,
            status=status,
        )

        return roblox_trades_api_trade_response
