from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationAnalyticsMetadataResponse")


@_attrs_define
class RobloxGameInternationalizationApiTranslationAnalyticsMetadataResponse:
    """
    Attributes:
        is_feature_enabled_on_ui (bool | Unset): Is Translation Analytics feature enabled on UI
        report_request_polling_interval_seconds (int | Unset): Number of seconds to poll the server for report
            availability
        minimum_date_time_for_analytics_report (datetime.datetime | Unset): Date-Time since the Analytics Reports can be
            downloaded
    """

    is_feature_enabled_on_ui: bool | Unset = UNSET
    report_request_polling_interval_seconds: int | Unset = UNSET
    minimum_date_time_for_analytics_report: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_feature_enabled_on_ui = self.is_feature_enabled_on_ui

        report_request_polling_interval_seconds = self.report_request_polling_interval_seconds

        minimum_date_time_for_analytics_report: str | Unset = UNSET
        if not isinstance(self.minimum_date_time_for_analytics_report, Unset):
            minimum_date_time_for_analytics_report = self.minimum_date_time_for_analytics_report.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_feature_enabled_on_ui is not UNSET:
            field_dict["isFeatureEnabledOnUI"] = is_feature_enabled_on_ui
        if report_request_polling_interval_seconds is not UNSET:
            field_dict["reportRequestPollingIntervalSeconds"] = report_request_polling_interval_seconds
        if minimum_date_time_for_analytics_report is not UNSET:
            field_dict["minimumDateTimeForAnalyticsReport"] = minimum_date_time_for_analytics_report

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_feature_enabled_on_ui = d.pop("isFeatureEnabledOnUI", UNSET)

        report_request_polling_interval_seconds = d.pop("reportRequestPollingIntervalSeconds", UNSET)

        _minimum_date_time_for_analytics_report = d.pop("minimumDateTimeForAnalyticsReport", UNSET)
        minimum_date_time_for_analytics_report: datetime.datetime | Unset
        if isinstance(_minimum_date_time_for_analytics_report, Unset):
            minimum_date_time_for_analytics_report = UNSET
        else:
            minimum_date_time_for_analytics_report = datetime.datetime.fromisoformat(
                _minimum_date_time_for_analytics_report
            )

        roblox_game_internationalization_api_translation_analytics_metadata_response = cls(
            is_feature_enabled_on_ui=is_feature_enabled_on_ui,
            report_request_polling_interval_seconds=report_request_polling_interval_seconds,
            minimum_date_time_for_analytics_report=minimum_date_time_for_analytics_report,
        )

        return roblox_game_internationalization_api_translation_analytics_metadata_response
