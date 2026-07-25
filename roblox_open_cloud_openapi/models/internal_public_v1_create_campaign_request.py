from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_create_campaign_request_objective import InternalPublicV1CreateCampaignRequestObjective
from ..models.internal_public_v1_create_campaign_request_payment_type import (
    InternalPublicV1CreateCampaignRequestPaymentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_bid import InternalPublicV1Bid
    from ..models.internal_public_v1_budget import InternalPublicV1Budget
    from ..models.internal_public_v1_schedule import InternalPublicV1Schedule
    from ..models.internal_public_v1_targeting import InternalPublicV1Targeting


T = TypeVar("T", bound="InternalPublicV1CreateCampaignRequest")


@_attrs_define
class InternalPublicV1CreateCampaignRequest:
    """
    Attributes:
        bid (InternalPublicV1Bid | Unset):
        budget (InternalPublicV1Budget | Unset):
        creative_asset_ids (list[str] | Unset): The Open Cloud image asset IDs to advertise, as decimal strings.
            Required. The
            assets must already exist and be usable by the caller.
        name (str | Unset): The display name of the campaign. Required.
        objective (InternalPublicV1CreateCampaignRequestObjective | Unset): The advertising goal. Required. Only
            `ENGAGEMENT` is supported in v1.
        payment_type (InternalPublicV1CreateCampaignRequestPaymentType | Unset): How the campaign is paid for. Required.
            Can be `CREDIT_CARD`, `ADS_CREDIT`, or
            `INVOICE`, subject to what the billing account supports.
        schedule (InternalPublicV1Schedule | Unset):
        target_universe_id (str | Unset): The identifier of the experience to advertise. Required.
        targeting (InternalPublicV1Targeting | Unset):
    """

    bid: InternalPublicV1Bid | Unset = UNSET
    budget: InternalPublicV1Budget | Unset = UNSET
    creative_asset_ids: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    objective: InternalPublicV1CreateCampaignRequestObjective | Unset = UNSET
    payment_type: InternalPublicV1CreateCampaignRequestPaymentType | Unset = UNSET
    schedule: InternalPublicV1Schedule | Unset = UNSET
    target_universe_id: str | Unset = UNSET
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

        objective: str | Unset = UNSET
        if not isinstance(self.objective, Unset):
            objective = self.objective.value

        payment_type: str | Unset = UNSET
        if not isinstance(self.payment_type, Unset):
            payment_type = self.payment_type.value

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        target_universe_id = self.target_universe_id

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
        if objective is not UNSET:
            field_dict["objective"] = objective
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if target_universe_id is not UNSET:
            field_dict["targetUniverseId"] = target_universe_id
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

        _objective = d.pop("objective", UNSET)
        objective: InternalPublicV1CreateCampaignRequestObjective | Unset
        if isinstance(_objective, Unset):
            objective = UNSET
        else:
            objective = InternalPublicV1CreateCampaignRequestObjective(_objective)

        _payment_type = d.pop("paymentType", UNSET)
        payment_type: InternalPublicV1CreateCampaignRequestPaymentType | Unset
        if isinstance(_payment_type, Unset):
            payment_type = UNSET
        else:
            payment_type = InternalPublicV1CreateCampaignRequestPaymentType(_payment_type)

        _schedule = d.pop("schedule", UNSET)
        schedule: InternalPublicV1Schedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = InternalPublicV1Schedule.from_dict(_schedule)

        target_universe_id = d.pop("targetUniverseId", UNSET)

        _targeting = d.pop("targeting", UNSET)
        targeting: InternalPublicV1Targeting | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = InternalPublicV1Targeting.from_dict(_targeting)

        internal_public_v1_create_campaign_request = cls(
            bid=bid,
            budget=budget,
            creative_asset_ids=creative_asset_ids,
            name=name,
            objective=objective,
            payment_type=payment_type,
            schedule=schedule,
            target_universe_id=target_universe_id,
            targeting=targeting,
        )

        internal_public_v1_create_campaign_request.additional_properties = d
        return internal_public_v1_create_campaign_request

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
