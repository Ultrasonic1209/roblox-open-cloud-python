from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiBadgeAwardResponse")


@_attrs_define
class RobloxBadgesApiBadgeAwardResponse:
    """The result of being awarded a badge.

    Attributes:
        badge_id (int | Unset): The badge Id.
        awarded_date (datetime.datetime | Unset): When the badge was awarded.
    """

    badge_id: int | Unset = UNSET
    awarded_date: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        badge_id = self.badge_id

        awarded_date: str | Unset = UNSET
        if not isinstance(self.awarded_date, Unset):
            awarded_date = self.awarded_date.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if badge_id is not UNSET:
            field_dict["badgeId"] = badge_id
        if awarded_date is not UNSET:
            field_dict["awardedDate"] = awarded_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_id = d.pop("badgeId", UNSET)

        _awarded_date = d.pop("awardedDate", UNSET)
        awarded_date: datetime.datetime | Unset
        if isinstance(_awarded_date, Unset):
            awarded_date = UNSET
        else:
            awarded_date = datetime.datetime.fromisoformat(_awarded_date)

        roblox_badges_api_badge_award_response = cls(
            badge_id=badge_id,
            awarded_date=awarded_date,
        )

        return roblox_badges_api_badge_award_response
