from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiteralValueDto")


@_attrs_define
class LiteralValueDto:
    """Literal constant for an RPN operand (proto `LiteralValue` oneof as independent fields for JSON).

    Attributes:
        boolean_value (None | str | Unset):
        integer_value (None | str | Unset):
        double_value (None | str | Unset):
        string_value (None | str | Unset):
    """

    boolean_value: None | str | Unset = UNSET
    integer_value: None | str | Unset = UNSET
    double_value: None | str | Unset = UNSET
    string_value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        boolean_value: None | str | Unset
        if isinstance(self.boolean_value, Unset):
            boolean_value = UNSET
        else:
            boolean_value = self.boolean_value

        integer_value: None | str | Unset
        if isinstance(self.integer_value, Unset):
            integer_value = UNSET
        else:
            integer_value = self.integer_value

        double_value: None | str | Unset
        if isinstance(self.double_value, Unset):
            double_value = UNSET
        else:
            double_value = self.double_value

        string_value: None | str | Unset
        if isinstance(self.string_value, Unset):
            string_value = UNSET
        else:
            string_value = self.string_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if integer_value is not UNSET:
            field_dict["integerValue"] = integer_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_boolean_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boolean_value = _parse_boolean_value(d.pop("booleanValue", UNSET))

        def _parse_integer_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integer_value = _parse_integer_value(d.pop("integerValue", UNSET))

        def _parse_double_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        double_value = _parse_double_value(d.pop("doubleValue", UNSET))

        def _parse_string_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        string_value = _parse_string_value(d.pop("stringValue", UNSET))

        literal_value_dto = cls(
            boolean_value=boolean_value,
            integer_value=integer_value,
            double_value=double_value,
            string_value=string_value,
        )

        return literal_value_dto
