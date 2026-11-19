from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_campaign_request_status import UpdateCampaignRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_video import CampaignVideo
    from ..models.targeting import Targeting
    from ..models.update_budget import UpdateBudget
    from ..models.update_schedule import UpdateSchedule


T = TypeVar("T", bound="UpdateCampaignRequest")


@_attrs_define
class UpdateCampaignRequest:
    """
    Attributes:
        auto_reload_ad_credit_enabled (bool | Unset): Turns automatic ad credit reload on or off.
        budget (UpdateBudget | Unset):
        creative_asset_ids (list[str] | Unset): New assets are appended to the campaign. Existing asset IDs are ignored.
            These are Roblox asset IDs, the same values as Creative.assetId.
        name (str | Unset): A new display name for the campaign.
        schedule (UpdateSchedule | Unset):
        status (UpdateCampaignRequestStatus | Unset): A lifecycle transition: `ACTIVE` to run or resume, `PAUSED` to
            pause, or
            `CANCELLED` to cancel permanently.
        targeting (Targeting | Unset):
        video (CampaignVideo | Unset):
    """

    auto_reload_ad_credit_enabled: bool | Unset = UNSET
    budget: UpdateBudget | Unset = UNSET
    creative_asset_ids: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    schedule: UpdateSchedule | Unset = UNSET
    status: UpdateCampaignRequestStatus | Unset = UNSET
    targeting: Targeting | Unset = UNSET
    video: CampaignVideo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_reload_ad_credit_enabled = self.auto_reload_ad_credit_enabled

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

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_reload_ad_credit_enabled is not UNSET:
            field_dict["autoReloadAdCreditEnabled"] = auto_reload_ad_credit_enabled
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
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_video import CampaignVideo  # noqa: PLC0415
        from ..models.targeting import Targeting  # noqa: PLC0415
        from ..models.update_budget import UpdateBudget  # noqa: PLC0415
        from ..models.update_schedule import UpdateSchedule  # noqa: PLC0415

        d = dict(src_dict)
        auto_reload_ad_credit_enabled = d.pop("autoReloadAdCreditEnabled", UNSET)

        _budget = d.pop("budget", UNSET)
        budget: UpdateBudget | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = UpdateBudget.from_dict(_budget)

        creative_asset_ids = cast(list[str], d.pop("creativeAssetIds", UNSET))

        name = d.pop("name", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: UpdateSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = UpdateSchedule.from_dict(_schedule)

        _status = d.pop("status", UNSET)
        status: UpdateCampaignRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateCampaignRequestStatus(_status)

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

        update_campaign_request = cls(
            auto_reload_ad_credit_enabled=auto_reload_ad_credit_enabled,
            budget=budget,
            creative_asset_ids=creative_asset_ids,
            name=name,
            schedule=schedule,
            status=status,
            targeting=targeting,
            video=video,
        )

        update_campaign_request.additional_properties = d
        return update_campaign_request

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
