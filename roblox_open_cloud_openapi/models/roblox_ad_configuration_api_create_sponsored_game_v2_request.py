from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_create_sponsored_game_v2_request_target_age_bracket import (
    RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetAgeBracket,
)
from ..models.roblox_ad_configuration_api_create_sponsored_game_v2_request_target_device_type import (
    RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetDeviceType,
)
from ..models.roblox_ad_configuration_api_create_sponsored_game_v2_request_target_gender import (
    RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetGender,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiCreateSponsoredGameV2Request")


@_attrs_define
class RobloxAdConfigurationApiCreateSponsoredGameV2Request:
    """A request model for creating a sponsored game

    Attributes:
        universe_id (int | Unset): The target universe id
        target_gender (RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetGender | Unset): Targeting gender(s) of
            the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4]
        target_age_bracket (RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetAgeBracket | Unset): Targeting age
            bracket(s) of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8, 'Age17OrOver' =
            16]
        budget_in_robux (int | Unset): The budget in Robux
        start_date (datetime.datetime | Unset): The start date of the ad set
        end_date (datetime.datetime | Unset): The end date of the ad set
        target_device_type (RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetDeviceType | Unset): Targeting
            device type(s) of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' = 16, 'VR' =
            32]
        ad_name (str | Unset): The name of the Ad
        bid_amount_in_robux (int | Unset): The bid amount of the Ad in Robux
    """

    universe_id: int | Unset = UNSET
    target_gender: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetGender | Unset = UNSET
    target_age_bracket: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetAgeBracket | Unset = UNSET
    budget_in_robux: int | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    target_device_type: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetDeviceType | Unset = UNSET
    ad_name: str | Unset = UNSET
    bid_amount_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        target_gender: int | Unset = UNSET
        if not isinstance(self.target_gender, Unset):
            target_gender = self.target_gender.value

        target_age_bracket: int | Unset = UNSET
        if not isinstance(self.target_age_bracket, Unset):
            target_age_bracket = self.target_age_bracket.value

        budget_in_robux = self.budget_in_robux

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        target_device_type: int | Unset = UNSET
        if not isinstance(self.target_device_type, Unset):
            target_device_type = self.target_device_type.value

        ad_name = self.ad_name

        bid_amount_in_robux = self.bid_amount_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if target_gender is not UNSET:
            field_dict["targetGender"] = target_gender
        if target_age_bracket is not UNSET:
            field_dict["targetAgeBracket"] = target_age_bracket
        if budget_in_robux is not UNSET:
            field_dict["budgetInRobux"] = budget_in_robux
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if target_device_type is not UNSET:
            field_dict["targetDeviceType"] = target_device_type
        if ad_name is not UNSET:
            field_dict["adName"] = ad_name
        if bid_amount_in_robux is not UNSET:
            field_dict["bidAmountInRobux"] = bid_amount_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        _target_gender = d.pop("targetGender", UNSET)
        target_gender: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetGender | Unset
        if isinstance(_target_gender, Unset):
            target_gender = UNSET
        else:
            target_gender = RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetGender(_target_gender)

        _target_age_bracket = d.pop("targetAgeBracket", UNSET)
        target_age_bracket: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetAgeBracket | Unset
        if isinstance(_target_age_bracket, Unset):
            target_age_bracket = UNSET
        else:
            target_age_bracket = RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetAgeBracket(
                _target_age_bracket
            )

        budget_in_robux = d.pop("budgetInRobux", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        _target_device_type = d.pop("targetDeviceType", UNSET)
        target_device_type: RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetDeviceType | Unset
        if isinstance(_target_device_type, Unset):
            target_device_type = UNSET
        else:
            target_device_type = RobloxAdConfigurationApiCreateSponsoredGameV2RequestTargetDeviceType(
                _target_device_type
            )

        ad_name = d.pop("adName", UNSET)

        bid_amount_in_robux = d.pop("bidAmountInRobux", UNSET)

        roblox_ad_configuration_api_create_sponsored_game_v2_request = cls(
            universe_id=universe_id,
            target_gender=target_gender,
            target_age_bracket=target_age_bracket,
            budget_in_robux=budget_in_robux,
            start_date=start_date,
            end_date=end_date,
            target_device_type=target_device_type,
            ad_name=ad_name,
            bid_amount_in_robux=bid_amount_in_robux,
        )

        return roblox_ad_configuration_api_create_sponsored_game_v2_request
