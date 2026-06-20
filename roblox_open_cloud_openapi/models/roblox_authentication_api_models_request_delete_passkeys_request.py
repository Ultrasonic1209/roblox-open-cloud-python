from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestDeletePasskeysRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestDeletePasskeysRequest:
    """
    Attributes:
        credential_nicknames (list[str] | Unset):
    """

    credential_nicknames: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_nicknames: list[str] | Unset = UNSET
        if not isinstance(self.credential_nicknames, Unset):
            credential_nicknames = self.credential_nicknames

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credential_nicknames is not UNSET:
            field_dict["credentialNicknames"] = credential_nicknames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_nicknames = cast(list[str], d.pop("credentialNicknames", UNSET))

        roblox_authentication_api_models_request_delete_passkeys_request = cls(
            credential_nicknames=credential_nicknames,
        )

        return roblox_authentication_api_models_request_delete_passkeys_request
