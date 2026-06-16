from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiFailedNameDescription")


@_attrs_define
class RobloxGameInternationalizationApiFailedNameDescription:
    """
    Attributes:
        language_code (str | Unset):
        error_code (int | Unset):
    """

    language_code: str | Unset = UNSET
    error_code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code = self.language_code

        error_code = self.error_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language_code = d.pop("languageCode", UNSET)

        error_code = d.pop("errorCode", UNSET)

        roblox_game_internationalization_api_failed_name_description = cls(
            language_code=language_code,
            error_code=error_code,
        )

        return roblox_game_internationalization_api_failed_name_description
