from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestFinishPasskeyPreauthRegistrationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestFinishPasskeyPreauthRegistrationRequest:
    """
    Attributes:
        session_id (str | Unset):
        registration_response (str | Unset):
    """

    session_id: str | Unset = UNSET
    registration_response: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        registration_response = self.registration_response

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if registration_response is not UNSET:
            field_dict["registrationResponse"] = registration_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        registration_response = d.pop("registrationResponse", UNSET)

        roblox_authentication_api_models_request_finish_passkey_preauth_registration_request = cls(
            session_id=session_id,
            registration_response=registration_response,
        )

        return roblox_authentication_api_models_request_finish_passkey_preauth_registration_request
