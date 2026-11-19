from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.performance_estimate_campaign_context import PerformanceEstimateCampaignContext
    from ..models.performance_estimate_forecast_input import PerformanceEstimateForecastInput
    from ..models.performance_estimate_scope import PerformanceEstimateScope


T = TypeVar("T", bound="PerformanceEstimateRequest")


@_attrs_define
class PerformanceEstimateRequest:
    """
    Attributes:
        campaign_context (PerformanceEstimateCampaignContext):
        forecast_input (PerformanceEstimateForecastInput):
        forecast_scope (PerformanceEstimateScope):
    """

    campaign_context: PerformanceEstimateCampaignContext
    forecast_input: PerformanceEstimateForecastInput
    forecast_scope: PerformanceEstimateScope
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_context = self.campaign_context.to_dict()

        forecast_input = self.forecast_input.to_dict()

        forecast_scope = self.forecast_scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignContext": campaign_context,
                "forecastInput": forecast_input,
                "forecastScope": forecast_scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.performance_estimate_campaign_context import PerformanceEstimateCampaignContext  # noqa: PLC0415
        from ..models.performance_estimate_forecast_input import PerformanceEstimateForecastInput  # noqa: PLC0415
        from ..models.performance_estimate_scope import PerformanceEstimateScope  # noqa: PLC0415

        d = dict(src_dict)
        campaign_context = PerformanceEstimateCampaignContext.from_dict(d.pop("campaignContext"))

        forecast_input = PerformanceEstimateForecastInput.from_dict(d.pop("forecastInput"))

        forecast_scope = PerformanceEstimateScope.from_dict(d.pop("forecastScope"))

        performance_estimate_request = cls(
            campaign_context=campaign_context,
            forecast_input=forecast_input,
            forecast_scope=forecast_scope,
        )

        performance_estimate_request.additional_properties = d
        return performance_estimate_request

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
