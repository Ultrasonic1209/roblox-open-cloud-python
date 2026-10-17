from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions")


@_attrs_define
class RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions:
    """
    Attributes:
        is_third_party_teleport_allowed (bool | Unset):
        is_third_party_asset_allowed (bool | Unset):
        is_third_party_purchase_allowed (bool | Unset):
        is_client_teleport_allowed (bool | Unset):
    """

    is_third_party_teleport_allowed: bool | Unset = UNSET
    is_third_party_asset_allowed: bool | Unset = UNSET
    is_third_party_purchase_allowed: bool | Unset = UNSET
    is_client_teleport_allowed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_third_party_teleport_allowed = self.is_third_party_teleport_allowed

        is_third_party_asset_allowed = self.is_third_party_asset_allowed

        is_third_party_purchase_allowed = self.is_third_party_purchase_allowed

        is_client_teleport_allowed = self.is_client_teleport_allowed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_third_party_teleport_allowed is not UNSET:
            field_dict["IsThirdPartyTeleportAllowed"] = is_third_party_teleport_allowed
        if is_third_party_asset_allowed is not UNSET:
            field_dict["IsThirdPartyAssetAllowed"] = is_third_party_asset_allowed
        if is_third_party_purchase_allowed is not UNSET:
            field_dict["IsThirdPartyPurchaseAllowed"] = is_third_party_purchase_allowed
        if is_client_teleport_allowed is not UNSET:
            field_dict["IsClientTeleportAllowed"] = is_client_teleport_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_third_party_teleport_allowed = d.pop("IsThirdPartyTeleportAllowed", UNSET)

        is_third_party_asset_allowed = d.pop("IsThirdPartyAssetAllowed", UNSET)

        is_third_party_purchase_allowed = d.pop("IsThirdPartyPurchaseAllowed", UNSET)

        is_client_teleport_allowed = d.pop("IsClientTeleportAllowed", UNSET)

        roblox_universe_plugin_permission_authority_models_universe_plugin_permissions = cls(
            is_third_party_teleport_allowed=is_third_party_teleport_allowed,
            is_third_party_asset_allowed=is_third_party_asset_allowed,
            is_third_party_purchase_allowed=is_third_party_purchase_allowed,
            is_client_teleport_allowed=is_client_teleport_allowed,
        )

        return roblox_universe_plugin_permission_authority_models_universe_plugin_permissions
