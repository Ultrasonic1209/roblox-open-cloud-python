from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebWebAPIModelsApiArrayResponseSystemString")


@_attrs_define
class RobloxWebWebAPIModelsApiArrayResponseSystemString:
    """
    Attributes:
        data (list[str] | Unset):
    """

    data: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[str] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = cast(list[str], d.pop("data", UNSET))

        roblox_web_web_api_models_api_array_response_system_string = cls(
            data=data,
        )

        return roblox_web_web_api_models_api_array_response_system_string
