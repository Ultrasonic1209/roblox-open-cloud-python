from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiSecurityKeyCredential")


@_attrs_define
class RobloxTwoStepVerificationApiSecurityKeyCredential:
    """Credential information that includes its nickname and any additional metadata.

    Attributes:
        nickname (str | Unset): Nickname the user has chosen for this credential.
        credential_id (str | Unset): Foreign key reference for this credential in the security-key-credentials database
    """

    nickname: str | Unset = UNSET
    credential_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nickname = self.nickname

        credential_id = self.credential_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if credential_id is not UNSET:
            field_dict["credentialID"] = credential_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        nickname = d.pop("nickname", UNSET)

        credential_id = d.pop("credentialID", UNSET)

        roblox_two_step_verification_api_security_key_credential = cls(
            nickname=nickname,
            credential_id=credential_id,
        )

        return roblox_two_step_verification_api_security_key_credential
