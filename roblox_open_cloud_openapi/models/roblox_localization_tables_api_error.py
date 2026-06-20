from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiError")


@_attrs_define
class RobloxLocalizationTablesApiError:
    """
    Attributes:
        error_code (int | Unset):
        error_message (str | Unset):
    """

    error_code: int | Unset = UNSET
    error_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        error_code = d.pop("errorCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        roblox_localization_tables_api_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        return roblox_localization_tables_api_error
