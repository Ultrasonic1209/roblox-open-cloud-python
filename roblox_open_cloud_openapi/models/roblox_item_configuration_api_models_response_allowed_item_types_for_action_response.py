from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseAllowedItemTypesForActionResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseAllowedItemTypesForActionResponse:
    """
    Attributes:
        allowed_asset_types (list[str] | Unset): The list of asset types allowed for the user for the given
            Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.
        allowed_bundle_types (list[str] | Unset): The list of bundle types allowed for the user for the given
            Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.
    """

    allowed_asset_types: list[str] | Unset = UNSET
    allowed_bundle_types: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_asset_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_asset_types, Unset):
            allowed_asset_types = self.allowed_asset_types

        allowed_bundle_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_bundle_types, Unset):
            allowed_bundle_types = self.allowed_bundle_types

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_asset_types is not UNSET:
            field_dict["allowedAssetTypes"] = allowed_asset_types
        if allowed_bundle_types is not UNSET:
            field_dict["allowedBundleTypes"] = allowed_bundle_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_asset_types = cast(list[str], d.pop("allowedAssetTypes", UNSET))

        allowed_bundle_types = cast(list[str], d.pop("allowedBundleTypes", UNSET))

        roblox_item_configuration_api_models_response_allowed_item_types_for_action_response = cls(
            allowed_asset_types=allowed_asset_types,
            allowed_bundle_types=allowed_bundle_types,
        )

        return roblox_item_configuration_api_models_response_allowed_item_types_for_action_response
