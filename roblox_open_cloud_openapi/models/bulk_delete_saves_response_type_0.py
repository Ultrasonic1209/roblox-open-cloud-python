from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkDeleteSavesResponseType0")


@_attrs_define
class BulkDeleteSavesResponseType0:
    """Response model for bulk delete saves operation

    Attributes:
        deleted_count (int | Unset): Number of saves that were successfully deleted
    """

    deleted_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        deleted_count = self.deleted_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if deleted_count is not UNSET:
            field_dict["deletedCount"] = deleted_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted_count = d.pop("deletedCount", UNSET)

        bulk_delete_saves_response_type_0 = cls(
            deleted_count=deleted_count,
        )

        return bulk_delete_saves_response_type_0
