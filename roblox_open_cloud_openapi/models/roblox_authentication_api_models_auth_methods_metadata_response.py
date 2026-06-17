from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAuthMethodsMetadataResponse")


@_attrs_define
class RobloxAuthenticationApiModelsAuthMethodsMetadataResponse:
    """
    Attributes:
        is_eligible_for_al_signup (bool | Unset):
    """

    is_eligible_for_al_signup: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_eligible_for_al_signup = self.is_eligible_for_al_signup

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_eligible_for_al_signup is not UNSET:
            field_dict["isEligibleForALSignup"] = is_eligible_for_al_signup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_eligible_for_al_signup = d.pop("isEligibleForALSignup", UNSET)

        roblox_authentication_api_models_auth_methods_metadata_response = cls(
            is_eligible_for_al_signup=is_eligible_for_al_signup,
        )

        return roblox_authentication_api_models_auth_methods_metadata_response
