from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesBadgesBadgeAwardStatisticsResponse")


@_attrs_define
class RobloxWebResponsesBadgesBadgeAwardStatisticsResponse:
    """
    Attributes:
        past_day_awarded_count (int | Unset):
        awarded_count (int | Unset):
        win_rate_percentage (float | Unset):
    """

    past_day_awarded_count: int | Unset = UNSET
    awarded_count: int | Unset = UNSET
    win_rate_percentage: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        past_day_awarded_count = self.past_day_awarded_count

        awarded_count = self.awarded_count

        win_rate_percentage = self.win_rate_percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if past_day_awarded_count is not UNSET:
            field_dict["pastDayAwardedCount"] = past_day_awarded_count
        if awarded_count is not UNSET:
            field_dict["awardedCount"] = awarded_count
        if win_rate_percentage is not UNSET:
            field_dict["winRatePercentage"] = win_rate_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        past_day_awarded_count = d.pop("pastDayAwardedCount", UNSET)

        awarded_count = d.pop("awardedCount", UNSET)

        win_rate_percentage = d.pop("winRatePercentage", UNSET)

        roblox_web_responses_badges_badge_award_statistics_response = cls(
            past_day_awarded_count=past_day_awarded_count,
            awarded_count=awarded_count,
            win_rate_percentage=win_rate_percentage,
        )

        return roblox_web_responses_badges_badge_award_statistics_response
