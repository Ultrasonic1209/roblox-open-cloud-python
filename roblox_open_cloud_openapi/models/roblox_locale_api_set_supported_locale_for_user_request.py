from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocaleApiSetSupportedLocaleForUserRequest")


@_attrs_define
class RobloxLocaleApiSetSupportedLocaleForUserRequest:
    """Request entity to set Supported Locale for user

    Attributes:
        supported_locale_code (str | Unset): SupportedLocale code
    """

    supported_locale_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        supported_locale_code = self.supported_locale_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if supported_locale_code is not UNSET:
            field_dict["supportedLocaleCode"] = supported_locale_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported_locale_code = d.pop("supportedLocaleCode", UNSET)

        roblox_locale_api_set_supported_locale_for_user_request = cls(
            supported_locale_code=supported_locale_code,
        )

        return roblox_locale_api_set_supported_locale_for_user_request
