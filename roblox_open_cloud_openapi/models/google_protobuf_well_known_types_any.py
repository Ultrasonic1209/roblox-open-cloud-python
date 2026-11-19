from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleProtobufWellKnownTypesAny")


@_attrs_define
class GoogleProtobufWellKnownTypesAny:
    """
    Attributes:
        type_url (None | str | Unset):
        value (list[int] | None | Unset):
    """

    type_url: None | str | Unset = UNSET
    value: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_url: None | str | Unset
        if isinstance(self.type_url, Unset):
            type_url = UNSET
        else:
            type_url = self.type_url

        value: list[int] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_url is not UNSET:
            field_dict["typeUrl"] = type_url
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_url = _parse_type_url(d.pop("typeUrl", UNSET))

        def _parse_value(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = cast(list[int], data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        google_protobuf_well_known_types_any = cls(
            type_url=type_url,
            value=value,
        )

        return google_protobuf_well_known_types_any
