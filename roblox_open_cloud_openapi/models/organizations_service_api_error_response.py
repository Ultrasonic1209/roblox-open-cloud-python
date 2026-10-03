from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.organizations_service_api_error_code import OrganizationsServiceApiErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationsServiceApiErrorResponse")


@_attrs_define
class OrganizationsServiceApiErrorResponse:
    """Standard error response model.

    Attributes:
        code (OrganizationsServiceApiErrorCode): Error code for OrganizationsServiceApi.Models.Response.ErrorResponse.
        message (None | str | Unset): The error message.
        field (None | str | Unset): Field on which model validation failed.
    """

    code: OrganizationsServiceApiErrorCode
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        code = OrganizationsServiceApiErrorCode(d.pop("code"))

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

        organizations_service_api_error_response = cls(
            code=code,
            message=message,
            field=field,
        )

        return organizations_service_api_error_response
