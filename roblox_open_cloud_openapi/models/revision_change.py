from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevisionChange")


@_attrs_define
class RevisionChange:
    """Represents a change in a revision, showing before and after values.

    Attributes:
        before (Any | Unset): The value before the change. Null if the key was added.
        after (Any | Unset): The value after the change. Null if the key was deleted.
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
        d = dict(src_dict)
        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        revision_change = cls(
            before=before,
            after=after,
        )

        return revision_change
