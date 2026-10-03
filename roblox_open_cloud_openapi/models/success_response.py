from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SuccessResponse")


@_attrs_define
class SuccessResponse:
    """Standard success response model.

    Attributes:
        success (bool): Whether or not the request was successfully executed.
    """

    success: bool

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        success = d.pop("success")

        success_response = cls(
            success=success,
        )

        return success_response
