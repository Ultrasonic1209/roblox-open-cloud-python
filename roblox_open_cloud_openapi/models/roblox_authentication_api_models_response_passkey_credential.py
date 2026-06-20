from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponsePasskeyCredential")


@_attrs_define
class RobloxAuthenticationApiModelsResponsePasskeyCredential:
    """
    Attributes:
        nickname (str | Unset):
    """

    nickname: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nickname = self.nickname

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if nickname is not UNSET:
            field_dict["nickname"] = nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        nickname = d.pop("nickname", UNSET)

        roblox_authentication_api_models_response_passkey_credential = cls(
            nickname=nickname,
        )

        return roblox_authentication_api_models_response_passkey_credential
