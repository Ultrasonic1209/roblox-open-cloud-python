from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsXboxTranslateRequest")


@_attrs_define
class RobloxAuthenticationApiModelsXboxTranslateRequest:
    """
    Attributes:
        ids (list[str] | Unset):
    """

    ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids", UNSET))

        roblox_authentication_api_models_xbox_translate_request = cls(
            ids=ids,
        )

        return roblox_authentication_api_models_xbox_translate_request
