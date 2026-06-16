from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_economy_creator_stats_api_models_statistics_response_data_granularity import (
    RobloxEconomyCreatorStatsApiModelsStatisticsResponseDataGranularity,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_economy_creator_stats_api_models_statistics_response_data import (
        RobloxEconomyCreatorStatsApiModelsStatisticsResponseData,
    )


T = TypeVar("T", bound="RobloxEconomyCreatorStatsApiModelsStatisticsResponse")


@_attrs_define
class RobloxEconomyCreatorStatsApiModelsStatisticsResponse:
    """The response model

    Attributes:
        data_granularity (RobloxEconomyCreatorStatsApiModelsStatisticsResponseDataGranularity | Unset): The
            Roblox.EconomyCreatorStats.Api.StatisticsDataGranularity. ['Hourly' = 0, 'Daily' = 1, 'Monthly' = 2]
        data (RobloxEconomyCreatorStatsApiModelsStatisticsResponseData | Unset): The actual data.
    """

    data_granularity: RobloxEconomyCreatorStatsApiModelsStatisticsResponseDataGranularity | Unset = UNSET
    data: RobloxEconomyCreatorStatsApiModelsStatisticsResponseData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_granularity: int | Unset = UNSET
        if not isinstance(self.data_granularity, Unset):
            data_granularity = self.data_granularity.value

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data_granularity is not UNSET:
            field_dict["dataGranularity"] = data_granularity
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_economy_creator_stats_api_models_statistics_response_data import (
            RobloxEconomyCreatorStatsApiModelsStatisticsResponseData,
        )

        d = dict(src_dict)
        _data_granularity = d.pop("dataGranularity", UNSET)
        data_granularity: RobloxEconomyCreatorStatsApiModelsStatisticsResponseDataGranularity | Unset
        if isinstance(_data_granularity, Unset):
            data_granularity = UNSET
        else:
            data_granularity = RobloxEconomyCreatorStatsApiModelsStatisticsResponseDataGranularity(_data_granularity)

        _data = d.pop("data", UNSET)
        data: RobloxEconomyCreatorStatsApiModelsStatisticsResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RobloxEconomyCreatorStatsApiModelsStatisticsResponseData.from_dict(_data)

        roblox_economy_creator_stats_api_models_statistics_response = cls(
            data_granularity=data_granularity,
            data=data,
        )

        return roblox_economy_creator_stats_api_models_statistics_response
