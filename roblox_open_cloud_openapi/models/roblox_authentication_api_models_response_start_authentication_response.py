from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseStartAuthenticationResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseStartAuthenticationResponse:
    """
    Attributes:
        authentication_options (str | Unset):
        session_id (str | Unset):
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
        d = dict(src_dict)
        authentication_options = d.pop("authenticationOptions", UNSET)

        session_id = d.pop("sessionId", UNSET)

        roblox_authentication_api_models_response_start_authentication_response = cls(
            authentication_options=authentication_options,
            session_id=session_id,
        )

        return roblox_authentication_api_models_response_start_authentication_response
