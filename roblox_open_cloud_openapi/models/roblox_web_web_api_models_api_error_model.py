from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebWebAPIModelsApiErrorModel")


@_attrs_define
class RobloxWebWebAPIModelsApiErrorModel:
    """
    Attributes:
        code (int | Unset):
        message (str | Unset):
        user_facing_message (str | Unset):
        field (str | Unset):
        field_data (Any | Unset):
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    user_facing_message: str | Unset = UNSET
    field: str | Unset = UNSET
    field_data: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        user_facing_message = self.user_facing_message

        field = self.field

        field_data = self.field_data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if user_facing_message is not UNSET:
            field_dict["userFacingMessage"] = user_facing_message
        if field is not UNSET:
            field_dict["field"] = field
        if field_data is not UNSET:
            field_dict["fieldData"] = field_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        user_facing_message = d.pop("userFacingMessage", UNSET)

        field = d.pop("field", UNSET)

        field_data = d.pop("fieldData", UNSET)

        roblox_web_web_api_models_api_error_model = cls(
            code=code,
            message=message,
            user_facing_message=user_facing_message,
            field=field,
            field_data=field_data,
        )

        return roblox_web_web_api_models_api_error_model
