from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiVerifyStartSecurityKeyResponse")


@_attrs_define
class RobloxTwoStepVerificationApiVerifyStartSecurityKeyResponse:
    """Result for a successful verification.

    Attributes:
        authentication_options (str | Unset): The authentication options for the hardware key.
        session_id (str | Unset): The session of the authentication attempt.
    """

    authentication_options: str | Unset = UNSET
    session_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        authentication_options = self.authentication_options

        session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if authentication_options is not UNSET:
            field_dict["authenticationOptions"] = authentication_options
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        authentication_options = d.pop("authenticationOptions", UNSET)

        session_id = d.pop("sessionId", UNSET)

        roblox_two_step_verification_api_verify_start_security_key_response = cls(
            authentication_options=authentication_options,
            session_id=session_id,
        )

        return roblox_two_step_verification_api_verify_start_security_key_response
