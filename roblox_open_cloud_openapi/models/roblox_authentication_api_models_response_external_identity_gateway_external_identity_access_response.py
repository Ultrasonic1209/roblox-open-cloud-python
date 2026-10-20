from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse:
    """
    Attributes:
        place_id (int | Unset):
        isolation_context (str | Unset):
        launch_data (str | Unset):
    """

    place_id: int | Unset = UNSET
    isolation_context: str | Unset = UNSET
    launch_data: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        isolation_context = self.isolation_context

        launch_data = self.launch_data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if isolation_context is not UNSET:
            field_dict["isolationContext"] = isolation_context
        if launch_data is not UNSET:
            field_dict["launchData"] = launch_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("placeId", UNSET)

        isolation_context = d.pop("isolationContext", UNSET)

        launch_data = d.pop("launchData", UNSET)

        roblox_authentication_api_models_response_external_identity_gateway_external_identity_access_response = cls(
            place_id=place_id,
            isolation_context=isolation_context,
            launch_data=launch_data,
        )

        return roblox_authentication_api_models_response_external_identity_gateway_external_identity_access_response
