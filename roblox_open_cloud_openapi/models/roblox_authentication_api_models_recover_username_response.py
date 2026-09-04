from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_recover_username_response_transmission_type import (
    RobloxAuthenticationApiModelsRecoverUsernameResponseTransmissionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecoverUsernameResponse")


@_attrs_define
class RobloxAuthenticationApiModelsRecoverUsernameResponse:
    """
    Attributes:
        transmission_type (RobloxAuthenticationApiModelsRecoverUsernameResponseTransmissionType | Unset):
    """

    transmission_type: RobloxAuthenticationApiModelsRecoverUsernameResponseTransmissionType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        transmission_type: int | Unset = UNSET
        if not isinstance(self.transmission_type, Unset):
            transmission_type = self.transmission_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transmission_type is not UNSET:
            field_dict["transmissionType"] = transmission_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _transmission_type = d.pop("transmissionType", UNSET)
        transmission_type: RobloxAuthenticationApiModelsRecoverUsernameResponseTransmissionType | Unset
        if isinstance(_transmission_type, Unset):
            transmission_type = UNSET
        else:
            transmission_type = RobloxAuthenticationApiModelsRecoverUsernameResponseTransmissionType(_transmission_type)

        roblox_authentication_api_models_recover_username_response = cls(
            transmission_type=transmission_type,
        )

        return roblox_authentication_api_models_recover_username_response
