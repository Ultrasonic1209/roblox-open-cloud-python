from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_provider_info_model import (
        RobloxAuthenticationApiModelsProviderInfoModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsSocialProvidersResponse")


@_attrs_define
class RobloxAuthenticationApiModelsSocialProvidersResponse:
    """
    Attributes:
        providers (list[RobloxAuthenticationApiModelsProviderInfoModel] | Unset):
    """

    providers: list[RobloxAuthenticationApiModelsProviderInfoModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_provider_info_model import (
            RobloxAuthenticationApiModelsProviderInfoModel,
        )

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: list[RobloxAuthenticationApiModelsProviderInfoModel] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = RobloxAuthenticationApiModelsProviderInfoModel.from_dict(providers_item_data)

                providers.append(providers_item)

        roblox_authentication_api_models_social_providers_response = cls(
            providers=providers,
        )

        return roblox_authentication_api_models_social_providers_response
