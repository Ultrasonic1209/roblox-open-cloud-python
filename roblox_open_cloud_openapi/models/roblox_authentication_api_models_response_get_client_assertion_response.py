from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseGetClientAssertionResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseGetClientAssertionResponse:
    """
    Attributes:
        client_assertion (str | Unset):
    """

    client_assertion: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_assertion = self.client_assertion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_assertion is not UNSET:
            field_dict["clientAssertion"] = client_assertion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        client_assertion = d.pop("clientAssertion", UNSET)

        roblox_authentication_api_models_response_get_client_assertion_response = cls(
            client_assertion=client_assertion,
        )

        return roblox_authentication_api_models_response_get_client_assertion_response
