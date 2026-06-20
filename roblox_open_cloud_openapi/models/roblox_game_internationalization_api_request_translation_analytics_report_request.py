from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_request_translation_analytics_report_request_report_type import (
    RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest")


@_attrs_define
class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest:
    """
    Attributes:
        start_date_time (datetime.datetime | Unset): The inclusive start dateTime of report in UTC
        end_date_time (datetime.datetime | Unset): The exclusive end dateTime of report in UTC
        report_type (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType | Unset): The
            report type ['GameTranslationStatus' = 0, 'GameTranslationStatusForTranslator' = 1,
            'GameTranslationStatusForTranslatorGroup' = 2, 'Test' = 3]
        report_subject_target_id (int | Unset): The report subject target id
    """

    start_date_time: datetime.datetime | Unset = UNSET
    end_date_time: datetime.datetime | Unset = UNSET
    report_type: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType | Unset = UNSET
    report_subject_target_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: str | Unset = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        report_type: str | Unset = UNSET
        if not isinstance(self.report_type, Unset):
            report_type = self.report_type.value

        report_subject_target_id = self.report_subject_target_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if report_subject_target_id is not UNSET:
            field_dict["reportSubjectTargetId"] = report_subject_target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: datetime.datetime | Unset
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = datetime.datetime.fromisoformat(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: datetime.datetime | Unset
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = datetime.datetime.fromisoformat(_end_date_time)

        _report_type = d.pop("reportType", UNSET)
        report_type: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType | Unset
        if isinstance(_report_type, Unset):
            report_type = UNSET
        else:
            report_type = RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType(
                _report_type
            )

        report_subject_target_id = d.pop("reportSubjectTargetId", UNSET)

        roblox_game_internationalization_api_request_translation_analytics_report_request = cls(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            report_type=report_type,
            report_subject_target_id=report_subject_target_id,
        )

        return roblox_game_internationalization_api_request_translation_analytics_report_request
