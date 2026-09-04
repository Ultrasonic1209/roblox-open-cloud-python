from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_login_method_model_method import (
    RobloxAuthenticationApiModelsLoginMethodModelMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsLoginMethodModel")


@_attrs_define
class RobloxAuthenticationApiModelsLoginMethodModel:
    """
    Attributes:
        method (RobloxAuthenticationApiModelsLoginMethodModelMethod | Unset):  ['EmailOtp' = 0, 'Passkey' = 1,
            'Password' = 2]
        priority (int | Unset):
    """

    method: RobloxAuthenticationApiModelsLoginMethodModelMethod | Unset = UNSET
    priority: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method: int | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        priority = self.priority

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _method = d.pop("method", UNSET)
        method: RobloxAuthenticationApiModelsLoginMethodModelMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = RobloxAuthenticationApiModelsLoginMethodModelMethod(_method)

        priority = d.pop("priority", UNSET)

        roblox_authentication_api_models_login_method_model = cls(
            method=method,
            priority=priority,
        )

        return roblox_authentication_api_models_login_method_model
