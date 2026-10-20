from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsReferralDataModel")


@_attrs_define
class RobloxAuthenticationApiModelsReferralDataModel:
    """
    Attributes:
        acquisition_time (datetime.datetime | Unset):
        acquisition_referrer (str | Unset):
        medium (str | Unset):
        source (str | Unset):
        campaign (str | Unset):
        ad_group (str | Unset):
        keyword (str | Unset):
        match_type (str | Unset):
        send_info (bool | Unset):
        request_session_id (str | Unset):
        offer_id (str | Unset):
    """

    acquisition_time: datetime.datetime | Unset = UNSET
    acquisition_referrer: str | Unset = UNSET
    medium: str | Unset = UNSET
    source: str | Unset = UNSET
    campaign: str | Unset = UNSET
    ad_group: str | Unset = UNSET
    keyword: str | Unset = UNSET
    match_type: str | Unset = UNSET
    send_info: bool | Unset = UNSET
    request_session_id: str | Unset = UNSET
    offer_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        acquisition_time: str | Unset = UNSET
        if not isinstance(self.acquisition_time, Unset):
            acquisition_time = self.acquisition_time.isoformat()

        acquisition_referrer = self.acquisition_referrer

        medium = self.medium

        source = self.source

        campaign = self.campaign

        ad_group = self.ad_group

        keyword = self.keyword

        match_type = self.match_type

        send_info = self.send_info

        request_session_id = self.request_session_id

        offer_id = self.offer_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if acquisition_time is not UNSET:
            field_dict["acquisitionTime"] = acquisition_time
        if acquisition_referrer is not UNSET:
            field_dict["acquisitionReferrer"] = acquisition_referrer
        if medium is not UNSET:
            field_dict["medium"] = medium
        if source is not UNSET:
            field_dict["source"] = source
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if ad_group is not UNSET:
            field_dict["adGroup"] = ad_group
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if match_type is not UNSET:
            field_dict["matchType"] = match_type
        if send_info is not UNSET:
            field_dict["sendInfo"] = send_info
        if request_session_id is not UNSET:
            field_dict["requestSessionId"] = request_session_id
        if offer_id is not UNSET:
            field_dict["offerId"] = offer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _acquisition_time = d.pop("acquisitionTime", UNSET)
        acquisition_time: datetime.datetime | Unset
        if isinstance(_acquisition_time, Unset):
            acquisition_time = UNSET
        else:
            acquisition_time = datetime.datetime.fromisoformat(_acquisition_time)

        acquisition_referrer = d.pop("acquisitionReferrer", UNSET)

        medium = d.pop("medium", UNSET)

        source = d.pop("source", UNSET)

        campaign = d.pop("campaign", UNSET)

        ad_group = d.pop("adGroup", UNSET)

        keyword = d.pop("keyword", UNSET)

        match_type = d.pop("matchType", UNSET)

        send_info = d.pop("sendInfo", UNSET)

        request_session_id = d.pop("requestSessionId", UNSET)

        offer_id = d.pop("offerId", UNSET)

        roblox_authentication_api_models_referral_data_model = cls(
            acquisition_time=acquisition_time,
            acquisition_referrer=acquisition_referrer,
            medium=medium,
            source=source,
            campaign=campaign,
            ad_group=ad_group,
            keyword=keyword,
            match_type=match_type,
            send_info=send_info,
            request_session_id=request_session_id,
            offer_id=offer_id,
        )

        return roblox_authentication_api_models_referral_data_model
