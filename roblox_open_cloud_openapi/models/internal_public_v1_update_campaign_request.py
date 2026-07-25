from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_update_campaign_request_status import InternalPublicV1UpdateCampaignRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_bid import InternalPublicV1Bid
    from ..models.internal_public_v1_budget import InternalPublicV1Budget
    from ..models.internal_public_v1_schedule import InternalPublicV1Schedule
    from ..models.internal_public_v1_targeting import InternalPublicV1Targeting


T = TypeVar("T", bound="InternalPublicV1UpdateCampaignRequest")


@_attrs_define
class InternalPublicV1UpdateCampaignRequest:
    """
    Attributes:
        bid (InternalPublicV1Bid | Unset):
        budget (InternalPublicV1Budget | Unset):
        creative_asset_ids (list[str] | Unset): Immutable in v1; including it returns 400.
        name (str | Unset): A new display name for the campaign.
        schedule (InternalPublicV1Schedule | Unset):
        status (InternalPublicV1UpdateCampaignRequestStatus | Unset): A lifecycle transition: `ACTIVE` to run or resume,
            `PAUSED` to pause, or
            `CANCELLED` to cancel permanently.
        targeting (InternalPublicV1Targeting | Unset):
    """

    bid: InternalPublicV1Bid | Unset = UNSET
    budget: InternalPublicV1Budget | Unset = UNSET
    creative_asset_ids: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    schedule: InternalPublicV1Schedule | Unset = UNSET
    status: InternalPublicV1UpdateCampaignRequestStatus | Unset = UNSET
    targeting: InternalPublicV1Targeting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bid, Unset):
            bid = self.bid.to_dict()

        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        creative_asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.creative_asset_ids, Unset):
            creative_asset_ids = self.creative_asset_ids

        name = self.name

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        targeting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bid is not UNSET:
            field_dict["bid"] = bid
        if budget is not UNSET:
            field_dict["budget"] = budget
        if creative_asset_ids is not UNSET:
            field_dict["creativeAssetIds"] = creative_asset_ids
        if name is not UNSET:
            field_dict["name"] = name
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if status is not UNSET:
            field_dict["status"] = status
        if targeting is not UNSET:
            field_dict["targeting"] = targeting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_bid import InternalPublicV1Bid
        from ..models.internal_public_v1_budget import InternalPublicV1Budget
        from ..models.internal_public_v1_schedule import InternalPublicV1Schedule
        from ..models.internal_public_v1_targeting import InternalPublicV1Targeting

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _bid = d.pop("bid", UNSET)
        bid: InternalPublicV1Bid | Unset
        if isinstance(_bid, Unset):
            bid = UNSET
        else:
            bid = InternalPublicV1Bid.from_dict(_bid)

        _budget = d.pop("budget", UNSET)
        budget: InternalPublicV1Budget | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = InternalPublicV1Budget.from_dict(_budget)

        creative_asset_ids = cast(list[str], d.pop("creativeAssetIds", UNSET))

        name = d.pop("name", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: InternalPublicV1Schedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = InternalPublicV1Schedule.from_dict(_schedule)

        _status = d.pop("status", UNSET)
        status: InternalPublicV1UpdateCampaignRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InternalPublicV1UpdateCampaignRequestStatus(_status)

        _targeting = d.pop("targeting", UNSET)
        targeting: InternalPublicV1Targeting | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = InternalPublicV1Targeting.from_dict(_targeting)

        internal_public_v1_update_campaign_request = cls(
            bid=bid,
            budget=budget,
            creative_asset_ids=creative_asset_ids,
            name=name,
            schedule=schedule,
            status=status,
            targeting=targeting,
        )

        internal_public_v1_update_campaign_request.additional_properties = d
        return internal_public_v1_update_campaign_request

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
