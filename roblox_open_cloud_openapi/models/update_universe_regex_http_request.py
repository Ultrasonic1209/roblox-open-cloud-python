from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.regex_operation import RegexOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUniverseRegexHttpRequest")


@_attrs_define
class UpdateUniverseRegexHttpRequest:
    """
    Attributes:
        pattern (None | str | Unset):
        output (None | str | Unset):
        regex_operation (RegexOperation | Unset):
    """

    pattern: None | str | Unset = UNSET
    output: None | str | Unset = UNSET
    regex_operation: RegexOperation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        regex_operation: str | Unset = UNSET
        if not isinstance(self.regex_operation, Unset):
            regex_operation = self.regex_operation.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if output is not UNSET:
            field_dict["output"] = output
        if regex_operation is not UNSET:
            field_dict["regexOperation"] = regex_operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        _regex_operation = d.pop("regexOperation", UNSET)
        regex_operation: RegexOperation | Unset
        if isinstance(_regex_operation, Unset):
            regex_operation = UNSET
        else:
            regex_operation = RegexOperation(_regex_operation)

        update_universe_regex_http_request = cls(
            pattern=pattern,
            output=output,
            regex_operation=regex_operation,
        )

        return update_universe_regex_http_request
