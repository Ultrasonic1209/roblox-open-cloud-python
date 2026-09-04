from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiDisableSecurityKeyRequest")


@_attrs_define
class RobloxTwoStepVerificationApiDisableSecurityKeyRequest:
    """Request information needed to disable a list of security keys.

    Attributes:
        credential_nicknames (list[str] | Unset): An array of nicknames of credentials to be deleted.
        credential_i_ds (list[str] | Unset): An array of IDs of credentials to be deleted.
            Preferred over nicknames.
    """

    credential_nicknames: list[str] | Unset = UNSET
    credential_i_ds: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_nicknames: list[str] | Unset = UNSET
        if not isinstance(self.credential_nicknames, Unset):
            credential_nicknames = self.credential_nicknames

        credential_i_ds: list[str] | Unset = UNSET
        if not isinstance(self.credential_i_ds, Unset):
            credential_i_ds = self.credential_i_ds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credential_nicknames is not UNSET:
            field_dict["credentialNicknames"] = credential_nicknames
        if credential_i_ds is not UNSET:
            field_dict["credentialIDs"] = credential_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        credential_nicknames = cast(list[str], d.pop("credentialNicknames", UNSET))

        credential_i_ds = cast(list[str], d.pop("credentialIDs", UNSET))

        roblox_two_step_verification_api_disable_security_key_request = cls(
            credential_nicknames=credential_nicknames,
            credential_i_ds=credential_i_ds,
        )

        return roblox_two_step_verification_api_disable_security_key_request
