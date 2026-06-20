from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleDeltaPayload")


@_attrs_define
class RuleDeltaPayload:
    """
    Attributes:
        before (Any | Unset):
        after (Any | Unset):
    """

    before: Any | Unset = UNSET
    after: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        before = self.before

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        rule_delta_payload = cls(
            before=before,
            after=after,
        )

        return rule_delta_payload
