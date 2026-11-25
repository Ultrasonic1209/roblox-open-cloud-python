from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.ownership_transfer_api_error_code import OwnershipTransferApiErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnershipTransferApiErrorResponse")


@_attrs_define
class OwnershipTransferApiErrorResponse:
    """Standard error response model.

    Attributes:
        code (OwnershipTransferApiErrorCode):
        message (None | str | Unset): The error message.
        field (None | str | Unset): Field on which model validation failed.
    """

    code: OwnershipTransferApiErrorCode
    message: None | str | Unset = UNSET
    field: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = OwnershipTransferApiErrorCode(d.pop("code"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        ownership_transfer_api_error_response = cls(
            code=code,
            message=message,
            field=field,
        )

        return ownership_transfer_api_error_response
