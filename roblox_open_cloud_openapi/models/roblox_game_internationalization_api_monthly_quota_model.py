from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiMonthlyQuotaModel")


@_attrs_define
class RobloxGameInternationalizationApiMonthlyQuotaModel:
    """
    Attributes:
        previous_refresh_date (datetime.datetime | Unset):
        next_refresh_date (datetime.datetime | Unset):
        remaining (int | Unset):
        capacity (int | Unset):
    """

    previous_refresh_date: datetime.datetime | Unset = UNSET
    next_refresh_date: datetime.datetime | Unset = UNSET
    remaining: int | Unset = UNSET
    capacity: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        previous_refresh_date: str | Unset = UNSET
        if not isinstance(self.previous_refresh_date, Unset):
            previous_refresh_date = self.previous_refresh_date.isoformat()

        next_refresh_date: str | Unset = UNSET
        if not isinstance(self.next_refresh_date, Unset):
            next_refresh_date = self.next_refresh_date.isoformat()

        remaining = self.remaining

        capacity = self.capacity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if previous_refresh_date is not UNSET:
            field_dict["previousRefreshDate"] = previous_refresh_date
        if next_refresh_date is not UNSET:
            field_dict["nextRefreshDate"] = next_refresh_date
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _previous_refresh_date = d.pop("previousRefreshDate", UNSET)
        previous_refresh_date: datetime.datetime | Unset
        if isinstance(_previous_refresh_date, Unset):
            previous_refresh_date = UNSET
        else:
            previous_refresh_date = datetime.datetime.fromisoformat(_previous_refresh_date)

        _next_refresh_date = d.pop("nextRefreshDate", UNSET)
        next_refresh_date: datetime.datetime | Unset
        if isinstance(_next_refresh_date, Unset):
            next_refresh_date = UNSET
        else:
            next_refresh_date = datetime.datetime.fromisoformat(_next_refresh_date)

        remaining = d.pop("remaining", UNSET)

        capacity = d.pop("capacity", UNSET)

        roblox_game_internationalization_api_monthly_quota_model = cls(
            previous_refresh_date=previous_refresh_date,
            next_refresh_date=next_refresh_date,
            remaining=remaining,
            capacity=capacity,
        )

        return roblox_game_internationalization_api_monthly_quota_model
