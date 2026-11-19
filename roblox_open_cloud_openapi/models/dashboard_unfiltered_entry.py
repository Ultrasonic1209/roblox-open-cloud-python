from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardUnfilteredEntry")


@_attrs_define
class DashboardUnfilteredEntry:
    """DashboardUnfilteredEntry defines the unfiltered selector option for a dimension control.

    Attributes:
        text_key (None | str | Unset):  Default: ''.
        breakdown_dimension_keys (list[str] | None | Unset):
    """

    text_key: None | str | Unset = ""
    breakdown_dimension_keys: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text_key: None | str | Unset
        if isinstance(self.text_key, Unset):
            text_key = UNSET
        else:
            text_key = self.text_key

        breakdown_dimension_keys: list[str] | None | Unset
        if isinstance(self.breakdown_dimension_keys, Unset):
            breakdown_dimension_keys = UNSET
        elif isinstance(self.breakdown_dimension_keys, list):
            breakdown_dimension_keys = self.breakdown_dimension_keys

        else:
            breakdown_dimension_keys = self.breakdown_dimension_keys

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if text_key is not UNSET:
            field_dict["textKey"] = text_key
        if breakdown_dimension_keys is not UNSET:
            field_dict["breakdownDimensionKeys"] = breakdown_dimension_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_text_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_key = _parse_text_key(d.pop("textKey", UNSET))

        def _parse_breakdown_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_dimension_keys_type_0 = cast(list[str], data)

                return breakdown_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        breakdown_dimension_keys = _parse_breakdown_dimension_keys(d.pop("breakdownDimensionKeys", UNSET))

        dashboard_unfiltered_entry = cls(
            text_key=text_key,
            breakdown_dimension_keys=breakdown_dimension_keys,
        )

        return dashboard_unfiltered_entry
