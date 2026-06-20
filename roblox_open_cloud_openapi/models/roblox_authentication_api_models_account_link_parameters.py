from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_account_link_parameters_linking_platform import (
    RobloxAuthenticationApiModelsAccountLinkParametersLinkingPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAccountLinkParameters")


@_attrs_define
class RobloxAuthenticationApiModelsAccountLinkParameters:
    """
    Attributes:
        linking_platform (RobloxAuthenticationApiModelsAccountLinkParametersLinkingPlatform | Unset):  ['Invalid' = 0,
            'Xbox' = 1, 'Qq' = 2, 'WeChat' = 3, 'Facebook' = 4, 'RobloxDeveloper' = 5, 'RobloxGroupCreator' = 6,
            'Playstation' = 7, 'ExternalProvider' = 8, 'Example' = 999]
    """

    linking_platform: RobloxAuthenticationApiModelsAccountLinkParametersLinkingPlatform | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        linking_platform: int | Unset = UNSET
        if not isinstance(self.linking_platform, Unset):
            linking_platform = self.linking_platform.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if linking_platform is not UNSET:
            field_dict["LinkingPlatform"] = linking_platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _linking_platform = d.pop("LinkingPlatform", UNSET)
        linking_platform: RobloxAuthenticationApiModelsAccountLinkParametersLinkingPlatform | Unset
        if isinstance(_linking_platform, Unset):
            linking_platform = UNSET
        else:
            linking_platform = RobloxAuthenticationApiModelsAccountLinkParametersLinkingPlatform(_linking_platform)

        roblox_authentication_api_models_account_link_parameters = cls(
            linking_platform=linking_platform,
        )

        return roblox_authentication_api_models_account_link_parameters
