from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_ad_configuration_api_models_universe_model import RobloxAdConfigurationApiModelsUniverseModel


T = TypeVar("T", bound="RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse")


@_attrs_define
class RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse:
    """The response model for getting a list of recent-ads-ranked universes.

    Attributes:
        universes (list[RobloxAdConfigurationApiModelsUniverseModel] | Unset): Gets or sets a list of
            Roblox.AdConfiguration.Api.Models.UniverseModel.
    """

    universes: list[RobloxAdConfigurationApiModelsUniverseModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.universes, Unset):
            universes = []
            for universes_item_data in self.universes:
                universes_item = universes_item_data.to_dict()
                universes.append(universes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universes is not UNSET:
            field_dict["universes"] = universes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_ad_configuration_api_models_universe_model import (
            RobloxAdConfigurationApiModelsUniverseModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _universes = d.pop("universes", UNSET)
        universes: list[RobloxAdConfigurationApiModelsUniverseModel] | Unset = UNSET
        if _universes is not UNSET:
            universes = []
            for universes_item_data in _universes:
                universes_item = RobloxAdConfigurationApiModelsUniverseModel.from_dict(universes_item_data)

                universes.append(universes_item)

        roblox_ad_configuration_api_models_get_recent_ads_ranked_universes_response = cls(
            universes=universes,
        )

        return roblox_ad_configuration_api_models_get_recent_ads_ranked_universes_response
