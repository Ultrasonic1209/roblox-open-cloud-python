from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_campaign_request_objective import CreateCampaignRequestObjective
from ..models.create_campaign_request_payment_type import CreateCampaignRequestPaymentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget import Budget
    from ..models.campaign_video import CampaignVideo
    from ..models.schedule import Schedule
    from ..models.targeting import Targeting


T = TypeVar("T", bound="CreateCampaignRequest")


@_attrs_define
class CreateCampaignRequest:
    """
    Attributes:
        budget (Budget):
        creative_asset_ids (list[str]): The Open Cloud image asset IDs to advertise, as decimal strings. Required. The
            assets must already exist and be usable by the caller.
            These are Roblox asset IDs, the same values as Creative.assetId.
        name (str): The display name of the campaign. Required.
        objective (CreateCampaignRequestObjective): The advertising goal. Required. Can be `PLAYS`, `ENGAGEMENT`, or
            `ROBUX_SPEND`. `ENGAGEMENT` does not support targeting; `ENGAGEMENT` and
            `ROBUX_SPEND` are not available for every experience.
        payment_type (CreateCampaignRequestPaymentType): How the campaign is paid for. Required. Can be `CREDIT_CARD`,
            `ADS_CREDIT`, or
            `INVOICE`, subject to what the billing account supports. A group's billing
            account accepts only `ADS_CREDIT`.
        schedule (Schedule):
        target_universe_id (str): The identifier of the experience to advertise. Required.
        auto_reload_ad_credit_enabled (bool | Unset): Whether ad credit is reloaded automatically when it runs low.
            Defaults to false.
        billing_account_id (str | Unset): The billing account to create the campaign in: your own, or one owned by a
            group
            where you have advertising permission. Optional; defaults to your own account,
            also for a group-owned experience. To pay with the group's ad credit, pass the
            group's account from campaign-options `billingAccounts`.
            For a group's account, targetUniverseId must be an experience the group owns.
        idempotency_key (UUID | Unset): Optional UUID for retry deduplication within 24 hours. Omit it or send an
            empty string to create without deduplication; retries can create duplicates.
            Use a new key for each new campaign or changed request body. Reuse a key only
            to retry the same body. A completed replay returns the original campaign
            (200) and ignores body changes; an in-progress replay returns 429.
        targeting (Targeting | Unset):
        video (CampaignVideo | Unset):
    """

    budget: Budget
    creative_asset_ids: list[str]
    name: str
    objective: CreateCampaignRequestObjective
    payment_type: CreateCampaignRequestPaymentType
    schedule: Schedule
    target_universe_id: str
    auto_reload_ad_credit_enabled: bool | Unset = UNSET
    billing_account_id: str | Unset = UNSET
    idempotency_key: UUID | Unset = UNSET
    targeting: Targeting | Unset = UNSET
    video: CampaignVideo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget = self.budget.to_dict()

        creative_asset_ids = self.creative_asset_ids

        name = self.name

        objective = self.objective.value

        payment_type = self.payment_type.value

        schedule = self.schedule.to_dict()

        target_universe_id = self.target_universe_id

        auto_reload_ad_credit_enabled = self.auto_reload_ad_credit_enabled

        billing_account_id = self.billing_account_id

        idempotency_key: str | Unset = UNSET
        if not isinstance(self.idempotency_key, Unset):
            idempotency_key = str(self.idempotency_key)

        targeting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting, Unset):
            targeting = self.targeting.to_dict()

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

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
        if auto_reload_ad_credit_enabled is not UNSET:
            field_dict["autoReloadAdCreditEnabled"] = auto_reload_ad_credit_enabled
        if billing_account_id is not UNSET:
            field_dict["billingAccountId"] = billing_account_id
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key
        if targeting is not UNSET:
            field_dict["targeting"] = targeting
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget import Budget  # noqa: PLC0415
        from ..models.campaign_video import CampaignVideo  # noqa: PLC0415
        from ..models.schedule import Schedule  # noqa: PLC0415
        from ..models.targeting import Targeting  # noqa: PLC0415

        d = dict(src_dict)
        budget = Budget.from_dict(d.pop("budget"))

        creative_asset_ids = cast(list[str], d.pop("creativeAssetIds"))

        name = d.pop("name")

        objective = CreateCampaignRequestObjective(d.pop("objective"))

        payment_type = CreateCampaignRequestPaymentType(d.pop("paymentType"))

        schedule = Schedule.from_dict(d.pop("schedule"))

        target_universe_id = d.pop("targetUniverseId")

        auto_reload_ad_credit_enabled = d.pop("autoReloadAdCreditEnabled", UNSET)

        billing_account_id = d.pop("billingAccountId", UNSET)

        _idempotency_key = d.pop("idempotencyKey", UNSET)
        idempotency_key: UUID | Unset
        if isinstance(_idempotency_key, Unset):
            idempotency_key = UNSET
        else:
            idempotency_key = UUID(_idempotency_key)

        _targeting = d.pop("targeting", UNSET)
        targeting: Targeting | Unset
        if isinstance(_targeting, Unset):
            targeting = UNSET
        else:
            targeting = Targeting.from_dict(_targeting)

        _video = d.pop("video", UNSET)
        video: CampaignVideo | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = CampaignVideo.from_dict(_video)

        create_campaign_request = cls(
            budget=budget,
            creative_asset_ids=creative_asset_ids,
            name=name,
            objective=objective,
            payment_type=payment_type,
            schedule=schedule,
            target_universe_id=target_universe_id,
            auto_reload_ad_credit_enabled=auto_reload_ad_credit_enabled,
            billing_account_id=billing_account_id,
            idempotency_key=idempotency_key,
            targeting=targeting,
            video=video,
        )

        create_campaign_request.additional_properties = d
        return create_campaign_request

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
