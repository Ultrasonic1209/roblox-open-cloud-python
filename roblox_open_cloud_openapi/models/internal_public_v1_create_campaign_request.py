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
        budget (InternalPublicV1Budget):
        creative_asset_ids (list[str]): The Open Cloud image asset IDs to advertise, as decimal strings. Required. The
            assets must already exist and be usable by the caller.
        name (str): The display name of the campaign. Required.
        objective (InternalPublicV1CreateCampaignRequestObjective): The advertising goal. Required. Only `ENGAGEMENT` is
            supported in v1.
        payment_type (InternalPublicV1CreateCampaignRequestPaymentType): How the campaign is paid for. Required. Can be
            `CREDIT_CARD`, `ADS_CREDIT`, or
            `INVOICE`, subject to what the billing account supports.
        schedule (InternalPublicV1Schedule):
        target_universe_id (str): The identifier of the experience to advertise. Required.
        bid (InternalPublicV1Bid | Unset):
        targeting (InternalPublicV1Targeting | Unset):
    """

    budget: InternalPublicV1Budget
    creative_asset_ids: list[str]
    name: str
    objective: InternalPublicV1CreateCampaignRequestObjective
    payment_type: InternalPublicV1CreateCampaignRequestPaymentType
    schedule: InternalPublicV1Schedule
    target_universe_id: str
    bid: InternalPublicV1Bid | Unset = UNSET
    targeting: InternalPublicV1Targeting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget = self.budget.to_dict()

        creative_asset_ids = self.creative_asset_ids

        name = self.name

        objective = self.objective.value

        payment_type = self.payment_type.value

        schedule = self.schedule.to_dict()

        target_universe_id = self.target_universe_id

        bid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bid, Unset):
            bid = self.bid.to_dict()

        targeting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget": budget,
                "creativeAssetIds": creative_asset_ids,
                "name": name,
                "objective": objective,
                "paymentType": payment_type,
                "schedule": schedule,
                "targetUniverseId": target_universe_id,
            }
        )
        if bid is not UNSET:
            field_dict["bid"] = bid
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
        budget = InternalPublicV1Budget.from_dict(d.pop("budget"))

        creative_asset_ids = cast(list[str], d.pop("creativeAssetIds"))

        name = d.pop("name")

        objective = InternalPublicV1CreateCampaignRequestObjective(d.pop("objective"))

        payment_type = InternalPublicV1CreateCampaignRequestPaymentType(d.pop("paymentType"))

        schedule = InternalPublicV1Schedule.from_dict(d.pop("schedule"))

        target_universe_id = d.pop("targetUniverseId")

        _bid = d.pop("bid", UNSET)
        bid: InternalPublicV1Bid | Unset
        if isinstance(_bid, Unset):
            bid = UNSET
        else:
            bid = InternalPublicV1Bid.from_dict(_bid)

        _targeting = d.pop("targeting", UNSET)
        targeting: InternalPublicV1Targeting | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = InternalPublicV1Targeting.from_dict(_targeting)

        internal_public_v1_create_campaign_request = cls(
            budget=budget,
            creative_asset_ids=creative_asset_ids,
            name=name,
            objective=objective,
            payment_type=payment_type,
            schedule=schedule,
            target_universe_id=target_universe_id,
            bid=bid,
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
