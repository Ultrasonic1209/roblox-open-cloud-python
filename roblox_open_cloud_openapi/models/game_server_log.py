from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.log_severity import LogSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_stack_frame import StructuredStackFrame


T = TypeVar("T", bound="GameServerLog")


@_attrs_define
class GameServerLog:
    """Response model for listing a game server log

    Attributes:
        message_timestamp_ms (datetime.datetime): The timestamp the log was received
        universe_id (int): The universe where the log was created
        place_id (None | str): The place where the log was created
        place_version (None | str): The place version on which the log was created
        job_id (None | str): The Game Server id where the log was created
        severity (LogSeverity): Defines the various log severity types with values:
            Output (0), Info (1), Warning (2), Error (3)
        message (None | str): The log message
        stack_trace (None | str): The stack trace of the log
        skipped_count (int): How many duplicate versions of this message were present in the same time window as this
            log
        rate_limited_count (int): How many more messages were present in the time window beyond our overall rate limits
        message_template (None | str | Unset): Optional message template included with structured logging
        context (None | str | Unset): Optional message context included with structured logging
        logger_full_path (None | str | Unset): The full path of the logger that emitted the log entry
        structured_stack_trace (list[StructuredStackFrame] | None | Unset): A list of
            ServerManagementService.V2.Models.StructuredStackFrame metadata, identifying the script that errored when
            combined
            with the ServerManagementService.V2.Models.GameServerLog.PlaceVersion
    """

    message_timestamp_ms: datetime.datetime
    universe_id: int
    place_id: None | str
    place_version: None | str
    job_id: None | str
    severity: LogSeverity
    message: None | str
    stack_trace: None | str
    skipped_count: int
    rate_limited_count: int
    message_template: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    logger_full_path: None | str | Unset = UNSET
    structured_stack_trace: list[StructuredStackFrame] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_timestamp_ms = self.message_timestamp_ms.isoformat()

        universe_id = self.universe_id

        place_id: None | str
        place_id = self.place_id

        place_version: None | str
        place_version = self.place_version

        job_id: None | str
        job_id = self.job_id

        severity = self.severity.value

        message: None | str
        message = self.message

        stack_trace: None | str
        stack_trace = self.stack_trace

        skipped_count = self.skipped_count

        rate_limited_count = self.rate_limited_count

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

        logger_full_path: None | str | Unset
        if isinstance(self.logger_full_path, Unset):
            logger_full_path = UNSET
        else:
            logger_full_path = self.logger_full_path

        structured_stack_trace: list[dict[str, Any]] | None | Unset
        if isinstance(self.structured_stack_trace, Unset):
            structured_stack_trace = UNSET
        elif isinstance(self.structured_stack_trace, list):
            structured_stack_trace = []
            for structured_stack_trace_type_0_item_data in self.structured_stack_trace:
                structured_stack_trace_type_0_item = structured_stack_trace_type_0_item_data.to_dict()
                structured_stack_trace.append(structured_stack_trace_type_0_item)

        else:
            structured_stack_trace = self.structured_stack_trace

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "messageTimestampMs": message_timestamp_ms,
                "universeId": universe_id,
                "placeId": place_id,
                "placeVersion": place_version,
                "jobId": job_id,
                "severity": severity,
                "message": message,
                "stackTrace": stack_trace,
                "skippedCount": skipped_count,
                "rateLimitedCount": rate_limited_count,
            }
        )
        if message_template is not UNSET:
            field_dict["messageTemplate"] = message_template
        if context is not UNSET:
            field_dict["context"] = context
        if logger_full_path is not UNSET:
            field_dict["loggerFullPath"] = logger_full_path
        if structured_stack_trace is not UNSET:
            field_dict["structuredStackTrace"] = structured_stack_trace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_stack_frame import StructuredStackFrame  # noqa: PLC0415

        d = dict(src_dict)
        message_timestamp_ms = datetime.datetime.fromisoformat(d.pop("messageTimestampMs"))

        universe_id = d.pop("universeId")

        def _parse_place_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        place_id = _parse_place_id(d.pop("placeId"))

        def _parse_place_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        place_version = _parse_place_version(d.pop("placeVersion"))

        def _parse_job_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        job_id = _parse_job_id(d.pop("jobId"))

        severity = LogSeverity(d.pop("severity"))

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_stack_trace(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        stack_trace = _parse_stack_trace(d.pop("stackTrace"))

        skipped_count = d.pop("skippedCount")

        rate_limited_count = d.pop("rateLimitedCount")

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

        def _parse_logger_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logger_full_path = _parse_logger_full_path(d.pop("loggerFullPath", UNSET))

        def _parse_structured_stack_trace(data: object) -> list[StructuredStackFrame] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                structured_stack_trace_type_0 = []
                _structured_stack_trace_type_0 = data
                for structured_stack_trace_type_0_item_data in _structured_stack_trace_type_0:
                    structured_stack_trace_type_0_item = StructuredStackFrame.from_dict(
                        structured_stack_trace_type_0_item_data
                    )

                    structured_stack_trace_type_0.append(structured_stack_trace_type_0_item)

                return structured_stack_trace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StructuredStackFrame] | None | Unset, data)

        structured_stack_trace = _parse_structured_stack_trace(d.pop("structuredStackTrace", UNSET))

        game_server_log = cls(
            message_timestamp_ms=message_timestamp_ms,
            universe_id=universe_id,
            place_id=place_id,
            place_version=place_version,
            job_id=job_id,
            severity=severity,
            message=message,
            stack_trace=stack_trace,
            skipped_count=skipped_count,
            rate_limited_count=rate_limited_count,
            message_template=message_template,
            context=context,
            logger_full_path=logger_full_path,
            structured_stack_trace=structured_stack_trace,
        )

        return game_server_log
