from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsProviderInfoModel")


@_attrs_define
class RobloxAuthenticationApiModelsProviderInfoModel:
    """
    Attributes:
        provider (str | Unset):
        identifier (str | Unset):
    """

    provider: str | Unset = UNSET
    identifier: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        identifier = self.identifier

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        provider = d.pop("provider", UNSET)

        identifier = d.pop("identifier", UNSET)

        roblox_authentication_api_models_provider_info_model = cls(
            provider=provider,
            identifier=identifier,
        )

        return roblox_authentication_api_models_provider_info_model
