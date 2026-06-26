from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.log_severity import LogSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="GameServerLog")


@_attrs_define
class GameServerLog:
    """Response model for listing a game server log

    Attributes:
        message_timestamp_ms (datetime.datetime | Unset): The timestamp the log was received
        universe_id (int | Unset): The universe where the log was created
        place_id (None | str | Unset): The place where the log was created
        place_version (None | str | Unset): The place version on which the log was created
        job_id (None | str | Unset): The Game Server id where the log was created
        severity (LogSeverity | Unset): Defines the various log severity types with values:
            Output (0), Info (1), Warning (2), Error (3)
        message (None | str | Unset): The log message
        stack_trace (None | str | Unset): The stack trace of the log
        message_template (None | str | Unset): Optional message template included with structured logging
        context (None | str | Unset): Optional message context included with structured logging
        skipped_count (int | Unset): How many duplicate versions of this message were present in the same time window as
            this log
        rate_limited_count (int | Unset): How many more messages were present in the time window beyond our overall rate
            limits
    """

    message_timestamp_ms: datetime.datetime | Unset = UNSET
    universe_id: int | Unset = UNSET
    place_id: None | str | Unset = UNSET
    place_version: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    severity: LogSeverity | Unset = UNSET
    message: None | str | Unset = UNSET
    stack_trace: None | str | Unset = UNSET
    message_template: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    skipped_count: int | Unset = UNSET
    rate_limited_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_timestamp_ms: str | Unset = UNSET
        if not isinstance(self.message_timestamp_ms, Unset):
            message_timestamp_ms = self.message_timestamp_ms.isoformat()

        universe_id = self.universe_id

        place_id: None | str | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        place_version: None | str | Unset
        if isinstance(self.place_version, Unset):
            place_version = UNSET
        else:
            place_version = self.place_version

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        severity: int | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        stack_trace: None | str | Unset
        if isinstance(self.stack_trace, Unset):
            stack_trace = UNSET
        else:
            stack_trace = self.stack_trace

        message_template: None | str | Unset
        if isinstance(self.message_template, Unset):
            message_template = UNSET
        else:
            message_template = self.message_template

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        skipped_count = self.skipped_count

        rate_limited_count = self.rate_limited_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message_timestamp_ms is not UNSET:
            field_dict["messageTimestampMs"] = message_timestamp_ms
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if place_version is not UNSET:
            field_dict["placeVersion"] = place_version
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if message is not UNSET:
            field_dict["message"] = message
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace
        if message_template is not UNSET:
            field_dict["messageTemplate"] = message_template
        if context is not UNSET:
            field_dict["context"] = context
        if skipped_count is not UNSET:
            field_dict["skippedCount"] = skipped_count
        if rate_limited_count is not UNSET:
            field_dict["rateLimitedCount"] = rate_limited_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _message_timestamp_ms = d.pop("messageTimestampMs", UNSET)
        message_timestamp_ms: datetime.datetime | Unset
        if isinstance(_message_timestamp_ms, Unset):
            message_timestamp_ms = UNSET
        else:
            message_timestamp_ms = datetime.datetime.fromisoformat(_message_timestamp_ms)

        universe_id = d.pop("universeId", UNSET)

        def _parse_place_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_place_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_version = _parse_place_version(d.pop("placeVersion", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("jobId", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: LogSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = LogSeverity(_severity)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_stack_trace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_trace = _parse_stack_trace(d.pop("stackTrace", UNSET))

        def _parse_message_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_template = _parse_message_template(d.pop("messageTemplate", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        skipped_count = d.pop("skippedCount", UNSET)

        rate_limited_count = d.pop("rateLimitedCount", UNSET)

        game_server_log = cls(
            message_timestamp_ms=message_timestamp_ms,
            universe_id=universe_id,
            place_id=place_id,
            place_version=place_version,
            job_id=job_id,
            severity=severity,
            message=message,
            stack_trace=stack_trace,
            message_template=message_template,
            context=context,
            skipped_count=skipped_count,
            rate_limited_count=rate_limited_count,
        )

        return game_server_log
