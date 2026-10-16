from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobuxRateBreakdown")


@_attrs_define
class RobuxRateBreakdown:
    """
    Attributes:
        o18 (float | None | Unset):
        standard (float | None | Unset):
    """

    o18: float | None | Unset = UNSET
    standard: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        o18: float | None | Unset
        if isinstance(self.o18, Unset):
            o18 = UNSET
        else:
            o18 = self.o18

        standard: float | None | Unset
        if isinstance(self.standard, Unset):
            standard = UNSET
        else:
            standard = self.standard

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if o18 is not UNSET:
            field_dict["o18"] = o18
        if standard is not UNSET:
            field_dict["standard"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_o18(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        o18 = _parse_o18(d.pop("o18", UNSET))

        def _parse_standard(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        standard = _parse_standard(d.pop("standard", UNSET))

        robux_rate_breakdown = cls(
            o18=o18,
            standard=standard,
        )

        return robux_rate_breakdown
