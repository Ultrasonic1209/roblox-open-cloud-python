from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.regex_operation import RegexOperation
from ..models.regex_status import RegexStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UniverseRegexHttpResponse")


@_attrs_define
class UniverseRegexHttpResponse:
    """
    Attributes:
        id (int | Unset):
        universe_id (int | Unset):
        regex_status (RegexStatus | Unset):
        pattern (None | str | Unset):
        output (None | str | Unset):
        order (int | Unset):
        regex_operation (RegexOperation | Unset):
        created_time (datetime.datetime | Unset):
        updated_time (datetime.datetime | Unset):
        matched_count (int | None | Unset):
        sample_message (None | str | Unset):
    """

    id: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    regex_status: RegexStatus | Unset = UNSET
    pattern: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    order: int | Unset = UNSET
    regex_operation: RegexOperation | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET
    matched_count: int | None | Unset = UNSET
    sample_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        universe_id = self.universe_id

        regex_status: str | Unset = UNSET
        if not isinstance(self.regex_status, Unset):
            regex_status = self.regex_status.value

        pattern: None | str | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        else:
            pattern = self.pattern

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        order = self.order

        regex_operation: str | Unset = UNSET
        if not isinstance(self.regex_operation, Unset):
            regex_operation = self.regex_operation.value

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        matched_count: int | None | Unset
        if isinstance(self.matched_count, Unset):
            matched_count = UNSET
        else:
            matched_count = self.matched_count

        sample_message: None | str | Unset
        if isinstance(self.sample_message, Unset):
            sample_message = UNSET
        else:
            sample_message = self.sample_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if regex_status is not UNSET:
            field_dict["regexStatus"] = regex_status
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if output is not UNSET:
            field_dict["output"] = output
        if order is not UNSET:
            field_dict["order"] = order
        if regex_operation is not UNSET:
            field_dict["regexOperation"] = regex_operation
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if matched_count is not UNSET:
            field_dict["matchedCount"] = matched_count
        if sample_message is not UNSET:
            field_dict["sampleMessage"] = sample_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        universe_id = d.pop("universeId", UNSET)

        _regex_status = d.pop("regexStatus", UNSET)
        regex_status: RegexStatus | Unset
        if isinstance(_regex_status, Unset):
            regex_status = UNSET
        else:
            regex_status = RegexStatus(_regex_status)

        def _parse_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        order = d.pop("order", UNSET)

        _regex_operation = d.pop("regexOperation", UNSET)
        regex_operation: RegexOperation | Unset
        if isinstance(_regex_operation, Unset):
            regex_operation = UNSET
        else:
            regex_operation = RegexOperation(_regex_operation)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = datetime.datetime.fromisoformat(_updated_time)

        def _parse_matched_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        matched_count = _parse_matched_count(d.pop("matchedCount", UNSET))

        def _parse_sample_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_message = _parse_sample_message(d.pop("sampleMessage", UNSET))

        universe_regex_http_response = cls(
            id=id,
            universe_id=universe_id,
            regex_status=regex_status,
            pattern=pattern,
            output=output,
            order=order,
            regex_operation=regex_operation,
            created_time=created_time,
            updated_time=updated_time,
            matched_count=matched_count,
            sample_message=sample_message,
        )

        return universe_regex_http_response
