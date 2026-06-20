from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsPromotionChannelsResponse")


@_attrs_define
class RobloxAccountInformationApiModelsPromotionChannelsResponse:
    """The promotion channels response

    Attributes:
        promotion_channels_visibility_privacy (str | Unset): The promotion channels visibility privacy level
        facebook (str | Unset): The Facebook channel
        twitter (str | Unset): The Twitter channel
        youtube (str | Unset): The YouTube channel
        twitch (str | Unset): The Twitch channel
    """

    promotion_channels_visibility_privacy: str | Unset = UNSET
    facebook: str | Unset = UNSET
    twitter: str | Unset = UNSET
    youtube: str | Unset = UNSET
    twitch: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        promotion_channels_visibility_privacy = self.promotion_channels_visibility_privacy

        facebook = self.facebook

        twitter = self.twitter

        youtube = self.youtube

        twitch = self.twitch

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if promotion_channels_visibility_privacy is not UNSET:
            field_dict["promotionChannelsVisibilityPrivacy"] = promotion_channels_visibility_privacy
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if youtube is not UNSET:
            field_dict["youtube"] = youtube
        if twitch is not UNSET:
            field_dict["twitch"] = twitch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        promotion_channels_visibility_privacy = d.pop("promotionChannelsVisibilityPrivacy", UNSET)

        facebook = d.pop("facebook", UNSET)

        twitter = d.pop("twitter", UNSET)

        youtube = d.pop("youtube", UNSET)

        twitch = d.pop("twitch", UNSET)

        roblox_account_information_api_models_promotion_channels_response = cls(
            promotion_channels_visibility_privacy=promotion_channels_visibility_privacy,
            facebook=facebook,
            twitter=twitter,
            youtube=youtube,
            twitch=twitch,
        )

        return roblox_account_information_api_models_promotion_channels_response
