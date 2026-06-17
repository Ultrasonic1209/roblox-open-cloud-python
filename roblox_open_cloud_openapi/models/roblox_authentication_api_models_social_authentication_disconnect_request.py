from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsSocialAuthenticationDisconnectRequest")


@_attrs_define
class RobloxAuthenticationApiModelsSocialAuthenticationDisconnectRequest:
    """
    Attributes:
        password (str | Unset):
    """

    password: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("Password", UNSET)

        roblox_authentication_api_models_social_authentication_disconnect_request = cls(
            password=password,
        )

        return roblox_authentication_api_models_social_authentication_disconnect_request
