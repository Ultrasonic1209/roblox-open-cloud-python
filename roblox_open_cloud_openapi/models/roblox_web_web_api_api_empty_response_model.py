from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxWebWebAPIApiEmptyResponseModel")


@_attrs_define
class RobloxWebWebAPIApiEmptyResponseModel:
    """ """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_web_web_api_api_empty_response_model = cls()

        return roblox_web_web_api_api_empty_response_model
