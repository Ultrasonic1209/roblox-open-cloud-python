from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReorderUniverseRegexHttpRequest")


@_attrs_define
class ReorderUniverseRegexHttpRequest:
    """
    Attributes:
        order (int | Unset):
    """

    order: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        order = d.pop("order", UNSET)

        reorder_universe_regex_http_request = cls(
            order=order,
        )

        return reorder_universe_regex_http_request
