from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_request_translation_analytics_report_response_report_generation_status import (
    RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse")


@_attrs_define
class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse:
    """
    Attributes:
        report_generation_status
            (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus | Unset):
            ['InProgress' = 0, 'Ready' = 1, 'Unavailable' = 2]
    """

    report_generation_status: (
        RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        report_generation_status: str | Unset = UNSET
        if not isinstance(self.report_generation_status, Unset):
            report_generation_status = self.report_generation_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if report_generation_status is not UNSET:
            field_dict["reportGenerationStatus"] = report_generation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _report_generation_status = d.pop("reportGenerationStatus", UNSET)
        report_generation_status: (
            RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus | Unset
        )
        if isinstance(_report_generation_status, Unset):
            report_generation_status = UNSET
        else:
            report_generation_status = (
                RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus(
                    _report_generation_status
                )
            )

        roblox_game_internationalization_api_request_translation_analytics_report_response = cls(
            report_generation_status=report_generation_status,
        )

        return roblox_game_internationalization_api_request_translation_analytics_report_response
