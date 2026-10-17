from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiEnableVerifySecurityKeyRequest")


@_attrs_define
class RobloxTwoStepVerificationApiEnableVerifySecurityKeyRequest:
    """Request information needed to complete the registration of a security key.

    Attributes:
        session_id (str | Unset): The session of the registration attempt.
        credential_nickname (str | Unset): The nickname of the new credential.
        attestation_response (str | Unset): The hardware key's response.
    """

    session_id: str | Unset = UNSET
    credential_nickname: str | Unset = UNSET
    attestation_response: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        credential_nickname = self.credential_nickname

        attestation_response = self.attestation_response

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if credential_nickname is not UNSET:
            field_dict["credentialNickname"] = credential_nickname
        if attestation_response is not UNSET:
            field_dict["attestationResponse"] = attestation_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        credential_nickname = d.pop("credentialNickname", UNSET)

        attestation_response = d.pop("attestationResponse", UNSET)

        roblox_two_step_verification_api_enable_verify_security_key_request = cls(
            session_id=session_id,
            credential_nickname=credential_nickname,
            attestation_response=attestation_response,
        )

        return roblox_two_step_verification_api_enable_verify_security_key_request
