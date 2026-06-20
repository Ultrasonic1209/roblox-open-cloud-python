from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxEngagementPayoutsApiPayoutResponseModel")


@_attrs_define
class RobloxEngagementPayoutsApiPayoutResponseModel:
    """A model for payout responses

    Attributes:
        engagement_score (float | Unset): Gets the engagement score
        payout_in_robux (int | Unset): Gets the payout in Robux
        payout_type (str | Unset): Gets the payout type
        eligibility_type (str | Unset): Gets the eligibility type
    """

    engagement_score: float | Unset = UNSET
    payout_in_robux: int | Unset = UNSET
    payout_type: str | Unset = UNSET
    eligibility_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        engagement_score = self.engagement_score

        payout_in_robux = self.payout_in_robux

        payout_type = self.payout_type

        eligibility_type = self.eligibility_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if engagement_score is not UNSET:
            field_dict["engagementScore"] = engagement_score
        if payout_in_robux is not UNSET:
            field_dict["payoutInRobux"] = payout_in_robux
        if payout_type is not UNSET:
            field_dict["payoutType"] = payout_type
        if eligibility_type is not UNSET:
            field_dict["eligibilityType"] = eligibility_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        engagement_score = d.pop("engagementScore", UNSET)

        payout_in_robux = d.pop("payoutInRobux", UNSET)

        payout_type = d.pop("payoutType", UNSET)

        eligibility_type = d.pop("eligibilityType", UNSET)

        roblox_engagement_payouts_api_payout_response_model = cls(
            engagement_score=engagement_score,
            payout_in_robux=payout_in_robux,
            payout_type=payout_type,
            eligibility_type=eligibility_type,
        )

        return roblox_engagement_payouts_api_payout_response_model
