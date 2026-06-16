from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiModelsStopSponsoredGameV2Request")


@_attrs_define
class RobloxAdConfigurationApiModelsStopSponsoredGameV2Request:
    """A model represents a request to stop a sponsored game ad.

    Attributes:
        ad_set_id (int | Unset): Gets the ID of the ad set to stop.
    """

    ad_set_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ad_set_id = self.ad_set_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ad_set_id is not UNSET:
            field_dict["adSetId"] = ad_set_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ad_set_id = d.pop("adSetId", UNSET)

        roblox_ad_configuration_api_models_stop_sponsored_game_v2_request = cls(
            ad_set_id=ad_set_id,
        )

        return roblox_ad_configuration_api_models_stop_sponsored_game_v2_request
