from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_attribute_value_type import MatchmakingAttributeValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchmakingAttributeValue")


@_attrs_define
class MatchmakingAttributeValue:
    """Matchmaking attribute value object for matchmaking rules.

    Attributes:
        bool_value (bool | None | Unset): Bool value of the attribute. One of BoolValue, NumericValue, or StringValue
            must be set.
        numeric_value (float | None | Unset): Double value of the attribute. One of BoolValue, NumericValue, or
            StringValue must be set.
        string_value (None | str | Unset): String value of the attribute. One of BoolValue, NumericValue, or StringValue
            must be set.
        type_ (MatchmakingAttributeValueType | Unset): Matchmaking attribute value type.
    """

    bool_value: bool | None | Unset = UNSET
    numeric_value: float | None | Unset = UNSET
    string_value: None | str | Unset = UNSET
    type_: MatchmakingAttributeValueType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bool_value: bool | None | Unset
        if isinstance(self.bool_value, Unset):
            bool_value = UNSET
        else:
            bool_value = self.bool_value

        numeric_value: float | None | Unset
        if isinstance(self.numeric_value, Unset):
            numeric_value = UNSET
        else:
            numeric_value = self.numeric_value

        string_value: None | str | Unset
        if isinstance(self.string_value, Unset):
            string_value = UNSET
        else:
            string_value = self.string_value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bool_value is not UNSET:
            field_dict["boolValue"] = bool_value
        if numeric_value is not UNSET:
            field_dict["numericValue"] = numeric_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_bool_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        bool_value = _parse_bool_value(d.pop("boolValue", UNSET))

        def _parse_numeric_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        numeric_value = _parse_numeric_value(d.pop("numericValue", UNSET))

        def _parse_string_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        string_value = _parse_string_value(d.pop("stringValue", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: MatchmakingAttributeValueType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MatchmakingAttributeValueType(_type_)

        matchmaking_attribute_value = cls(
            bool_value=bool_value,
            numeric_value=numeric_value,
            string_value=string_value,
            type_=type_,
        )

        return matchmaking_attribute_value
