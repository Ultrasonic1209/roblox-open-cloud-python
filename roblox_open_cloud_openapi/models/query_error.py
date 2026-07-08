from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryError")


@_attrs_define
class QueryError:
    """The error returned from a query request.

    Attributes:
        message (str): The message associated with the query error.
        code (int | Unset): The error code.
    """

    message: str
    code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        message = d.pop("message")

        code = d.pop("code", UNSET)

        query_error = cls(
            message=message,
            code=code,
        )

        return query_error
