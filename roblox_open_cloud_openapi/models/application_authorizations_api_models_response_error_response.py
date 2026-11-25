from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.application_authorizations_api_models_enum_error_code import (
    ApplicationAuthorizationsApiModelsEnumErrorCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseErrorResponse")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseErrorResponse:
    """
    Attributes:
        code (ApplicationAuthorizationsApiModelsEnumErrorCode):
        message (None | str | Unset):
        field (None | str | Unset):
    """

    code: ApplicationAuthorizationsApiModelsEnumErrorCode
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
        code = ApplicationAuthorizationsApiModelsEnumErrorCode(d.pop("code"))

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

        application_authorizations_api_models_response_error_response = cls(
            code=code,
            message=message,
            field=field,
        )

        return application_authorizations_api_models_response_error_response
