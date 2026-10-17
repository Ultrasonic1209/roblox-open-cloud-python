from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorLogDetail")


@_attrs_define
class ErrorLogDetail:
    """error log detail

    Attributes:
        id (None | str | Unset): The message hash id for this log detail.
        log_severity (None | str | Unset): The logSeverity of the log
        log_source (None | str | Unset): The source of the log
        os (None | str | Unset):
        platform (None | str | Unset):
        message (None | str | Unset): The message of the error log
        stacktrace (None | str | Unset): The stack trace of the error log. This might be not available
        first_seen_utc (datetime.datetime | None | Unset): UTC timestamp when this error was first observed.
            Null when the source document predates this field being populated.
        first_seen_place_version (int | None | Unset): First seen place version for the error.
            NOTE: This value will only be returned when place id is filtered
    """

    id: None | str | Unset = UNSET
    log_severity: None | str | Unset = UNSET
    log_source: None | str | Unset = UNSET
    os: None | str | Unset = UNSET
    platform: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    stacktrace: None | str | Unset = UNSET
    first_seen_utc: datetime.datetime | None | Unset = UNSET
    first_seen_place_version: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        log_severity: None | str | Unset
        if isinstance(self.log_severity, Unset):
            log_severity = UNSET
        else:
            log_severity = self.log_severity

        log_source: None | str | Unset
        if isinstance(self.log_source, Unset):
            log_source = UNSET
        else:
            log_source = self.log_source

        os: None | str | Unset
        if isinstance(self.os, Unset):
            os = UNSET
        else:
            os = self.os

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        stacktrace: None | str | Unset
        if isinstance(self.stacktrace, Unset):
            stacktrace = UNSET
        else:
            stacktrace = self.stacktrace

        first_seen_utc: None | str | Unset
        if isinstance(self.first_seen_utc, Unset):
            first_seen_utc = UNSET
        elif isinstance(self.first_seen_utc, datetime.datetime):
            first_seen_utc = self.first_seen_utc.isoformat()
        else:
            first_seen_utc = self.first_seen_utc

        first_seen_place_version: int | None | Unset
        if isinstance(self.first_seen_place_version, Unset):
            first_seen_place_version = UNSET
        else:
            first_seen_place_version = self.first_seen_place_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if log_severity is not UNSET:
            field_dict["logSeverity"] = log_severity
        if log_source is not UNSET:
            field_dict["logSource"] = log_source
        if os is not UNSET:
            field_dict["os"] = os
        if platform is not UNSET:
            field_dict["platform"] = platform
        if message is not UNSET:
            field_dict["message"] = message
        if stacktrace is not UNSET:
            field_dict["stacktrace"] = stacktrace
        if first_seen_utc is not UNSET:
            field_dict["firstSeenUtc"] = first_seen_utc
        if first_seen_place_version is not UNSET:
            field_dict["firstSeenPlaceVersion"] = first_seen_place_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_log_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        log_severity = _parse_log_severity(d.pop("logSeverity", UNSET))

        def _parse_log_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        log_source = _parse_log_source(d.pop("logSource", UNSET))

        def _parse_os(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os = _parse_os(d.pop("os", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_stacktrace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stacktrace = _parse_stacktrace(d.pop("stacktrace", UNSET))

        def _parse_first_seen_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_seen_utc_type_0 = datetime.datetime.fromisoformat(data)

                return first_seen_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_seen_utc = _parse_first_seen_utc(d.pop("firstSeenUtc", UNSET))

        def _parse_first_seen_place_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_seen_place_version = _parse_first_seen_place_version(d.pop("firstSeenPlaceVersion", UNSET))

        error_log_detail = cls(
            id=id,
            log_severity=log_severity,
            log_source=log_source,
            os=os,
            platform=platform,
            message=message,
            stacktrace=stacktrace,
            first_seen_utc=first_seen_utc,
            first_seen_place_version=first_seen_place_version,
        )

        return error_log_detail
