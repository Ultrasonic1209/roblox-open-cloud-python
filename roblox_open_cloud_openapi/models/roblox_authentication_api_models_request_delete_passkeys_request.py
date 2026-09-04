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
        credential_i_ds (list[str] | Unset):
        credential_nicknames (list[str] | Unset):
    """

    credential_i_ds: list[str] | Unset = UNSET
    credential_nicknames: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_i_ds: list[str] | Unset = UNSET
        if not isinstance(self.credential_i_ds, Unset):
            credential_i_ds = self.credential_i_ds

        credential_nicknames: list[str] | Unset = UNSET
        if not isinstance(self.credential_nicknames, Unset):
            credential_nicknames = self.credential_nicknames

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credential_i_ds is not UNSET:
            field_dict["credentialIDs"] = credential_i_ds
        if credential_nicknames is not UNSET:
            field_dict["credentialNicknames"] = credential_nicknames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        credential_i_ds = cast(list[str], d.pop("credentialIDs", UNSET))

        credential_nicknames = cast(list[str], d.pop("credentialNicknames", UNSET))

        roblox_authentication_api_models_request_delete_passkeys_request = cls(
            credential_i_ds=credential_i_ds,
            credential_nicknames=credential_nicknames,
        )

        return roblox_authentication_api_models_request_delete_passkeys_request
