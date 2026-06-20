from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolboxServiceDecimalType0")


@_attrs_define
class ToolboxServiceDecimalType0:
    """
    Attributes:
        significand (int | Unset):
        exponent (int | Unset):
    """

    significand: int | Unset = UNSET
    exponent: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        significand = self.significand

        exponent = self.exponent

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if significand is not UNSET:
            field_dict["significand"] = significand
        if exponent is not UNSET:
            field_dict["exponent"] = exponent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        significand = d.pop("significand", UNSET)

        exponent = d.pop("exponent", UNSET)

        toolbox_service_decimal_type_0 = cls(
            significand=significand,
            exponent=exponent,
        )

        return toolbox_service_decimal_type_0
