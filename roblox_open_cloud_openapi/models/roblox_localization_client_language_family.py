from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationClientLanguageFamily")


@_attrs_define
class RobloxLocalizationClientLanguageFamily:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        native_name (str | Unset):
        language_code (str | Unset):
        is_right_to_left (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    native_name: str | Unset = UNSET
    language_code: str | Unset = UNSET
    is_right_to_left: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        native_name = self.native_name

        language_code = self.language_code

        is_right_to_left = self.is_right_to_left

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if is_right_to_left is not UNSET:
            field_dict["isRightToLeft"] = is_right_to_left

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        native_name = d.pop("nativeName", UNSET)

        language_code = d.pop("languageCode", UNSET)

        is_right_to_left = d.pop("isRightToLeft", UNSET)

        roblox_localization_client_language_family = cls(
            id=id,
            name=name,
            native_name=native_name,
            language_code=language_code,
            is_right_to_left=is_right_to_left,
        )

        return roblox_localization_client_language_family
