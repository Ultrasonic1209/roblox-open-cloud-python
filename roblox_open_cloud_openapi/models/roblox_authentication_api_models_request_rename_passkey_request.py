from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestRenamePasskeyRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestRenamePasskeyRequest:
    """
    Attributes:
        credential_id (str | Unset):
        new_nickname (str | Unset):
    """

    credential_id: str | Unset = UNSET
    new_nickname: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        new_nickname = self.new_nickname

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credential_id is not UNSET:
            field_dict["credentialID"] = credential_id
        if new_nickname is not UNSET:
            field_dict["newNickname"] = new_nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        credential_id = d.pop("credentialID", UNSET)

        new_nickname = d.pop("newNickname", UNSET)

        roblox_authentication_api_models_request_rename_passkey_request = cls(
            credential_id=credential_id,
            new_nickname=new_nickname,
        )

        return roblox_authentication_api_models_request_rename_passkey_request
