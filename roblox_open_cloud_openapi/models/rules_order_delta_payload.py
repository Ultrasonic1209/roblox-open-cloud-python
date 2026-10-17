from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RulesOrderDeltaPayload")


@_attrs_define
class RulesOrderDeltaPayload:
    """
    Attributes:
        before (list[str] | None | Unset):
        after (list[str] | None | Unset):
    """

    before: list[str] | None | Unset = UNSET
    after: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        before: list[str] | None | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        elif isinstance(self.before, list):
            before = self.before

        else:
            before = self.before

        after: list[str] | None | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        elif isinstance(self.after, list):
            after = self.after

        else:
            after = self.after

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_before(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                before_type_0 = cast(list[str], data)

                return before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        before = _parse_before(d.pop("before", UNSET))

        def _parse_after(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                after_type_0 = cast(list[str], data)

                return after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        after = _parse_after(d.pop("after", UNSET))

        rules_order_delta_payload = cls(
            before=before,
            after=after,
        )

        return rules_order_delta_payload
