from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_ad_delivery_status import CampaignAdDeliveryStatus
from ..models.campaign_ad_review_status import CampaignAdReviewStatus
from ..models.campaign_ad_status import CampaignAdStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reason import Reason


T = TypeVar("T", bound="CampaignAd")


@_attrs_define
class CampaignAd:
    """
    Attributes:
        creative_asset_id (str): The Roblox image asset ID this ad serves, as a decimal string.
            This is the same value as Creative.assetId.
        delivery_status (CampaignAdDeliveryStatus): Per-ad serving state (`SERVING`, `IN_REVIEW`, `NOT_SERVING`, or
            `REJECTED`).
        id (str): Stable ad ID; matches the ad ID in analytics-query-api.
        review_status (CampaignAdReviewStatus): Combined result of the creative's review and the experience's review
            (`IN_REVIEW`, `APPROVED`, or `REJECTED`).
        status (CampaignAdStatus): Lifecycle intent for this ad (`ACTIVE`, `PAUSED`, or `REMOVED`).
        remove_time (datetime.datetime | Unset): Set when status is `REMOVED`, as an RFC 3339 UTC timestamp.
        review_issues (list[Reason] | Unset): Structured review issues, when applicable.
    """

    creative_asset_id: str
    delivery_status: CampaignAdDeliveryStatus
    id: str
    review_status: CampaignAdReviewStatus
    status: CampaignAdStatus
    remove_time: datetime.datetime | Unset = UNSET
    review_issues: list[Reason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creative_asset_id = self.creative_asset_id

        delivery_status = self.delivery_status.value

        id = self.id

        review_status = self.review_status.value

        status = self.status.value

        remove_time: str | Unset = UNSET
        if not isinstance(self.remove_time, Unset):
            remove_time = self.remove_time.isoformat()

        review_issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.review_issues, Unset):
            review_issues = []
            for review_issues_item_data in self.review_issues:
                review_issues_item = review_issues_item_data.to_dict()
                review_issues.append(review_issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creativeAssetId": creative_asset_id,
                "deliveryStatus": delivery_status,
                "id": id,
                "reviewStatus": review_status,
                "status": status,
            }
        )
        if remove_time is not UNSET:
            field_dict["removeTime"] = remove_time
        if review_issues is not UNSET:
            field_dict["reviewIssues"] = review_issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason import Reason  # noqa: PLC0415

        d = dict(src_dict)
        creative_asset_id = d.pop("creativeAssetId")

        delivery_status = CampaignAdDeliveryStatus(d.pop("deliveryStatus"))

        id = d.pop("id")

        review_status = CampaignAdReviewStatus(d.pop("reviewStatus"))

        status = CampaignAdStatus(d.pop("status"))

        _remove_time = d.pop("removeTime", UNSET)
        remove_time: datetime.datetime | Unset
        if isinstance(_remove_time, Unset):
            remove_time = UNSET
        else:
            remove_time = datetime.datetime.fromisoformat(_remove_time)

        _review_issues = d.pop("reviewIssues", UNSET)
        review_issues: list[Reason] | Unset = UNSET
        if _review_issues is not UNSET:
            review_issues = []
            for review_issues_item_data in _review_issues:
                review_issues_item = Reason.from_dict(review_issues_item_data)

                review_issues.append(review_issues_item)

        campaign_ad = cls(
            creative_asset_id=creative_asset_id,
            delivery_status=delivery_status,
            id=id,
            review_status=review_status,
            status=status,
            remove_time=remove_time,
            review_issues=review_issues,
        )

        campaign_ad.additional_properties = d
        return campaign_ad

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
