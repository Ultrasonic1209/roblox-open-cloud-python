from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_login_method_model import (
        RobloxAuthenticationApiModelsLoginMethodModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseInitializeLoginResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseInitializeLoginResponse:
    """
    Attributes:
        login_methods (list[RobloxAuthenticationApiModelsLoginMethodModel] | Unset):
    """

    login_methods: list[RobloxAuthenticationApiModelsLoginMethodModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        login_methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.login_methods, Unset):
            login_methods = []
            for login_methods_item_data in self.login_methods:
                login_methods_item = login_methods_item_data.to_dict()
                login_methods.append(login_methods_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if login_methods is not UNSET:
            field_dict["loginMethods"] = login_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_login_method_model import (
            RobloxAuthenticationApiModelsLoginMethodModel,
        )

        d = dict(src_dict)
        _login_methods = d.pop("loginMethods", UNSET)
        login_methods: list[RobloxAuthenticationApiModelsLoginMethodModel] | Unset = UNSET
        if _login_methods is not UNSET:
            login_methods = []
            for login_methods_item_data in _login_methods:
                login_methods_item = RobloxAuthenticationApiModelsLoginMethodModel.from_dict(login_methods_item_data)

                login_methods.append(login_methods_item)

        roblox_authentication_api_models_response_initialize_login_response = cls(
            login_methods=login_methods,
        )

        return roblox_authentication_api_models_response_initialize_login_response
