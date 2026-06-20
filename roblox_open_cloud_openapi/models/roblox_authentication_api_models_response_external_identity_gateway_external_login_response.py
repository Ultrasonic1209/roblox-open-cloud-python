from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse:
    """
    Attributes:
        success (bool | Unset):
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
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        roblox_authentication_api_models_response_external_identity_gateway_external_login_response = cls(
            success=success,
        )

        return roblox_authentication_api_models_response_external_identity_gateway_external_login_response
