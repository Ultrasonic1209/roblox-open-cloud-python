from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarApiSuccessResponse")


@_attrs_define
class RobloxApiAvatarModelsAvatarApiSuccessResponse:
    """Success response class

    Attributes:
        success (bool | Unset): Gets or sets a value indicating whether the request was a success.
    """

    success: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        success = d.pop("success", UNSET)

        roblox_api_avatar_models_avatar_api_success_response = cls(
            success=success,
        )

        return roblox_api_avatar_models_avatar_api_success_response
