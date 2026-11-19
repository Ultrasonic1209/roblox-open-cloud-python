from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_marketplace_item_licensing_info_state import (
    RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfoState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo:
    """Licensing info for the collectible item.

    Attributes:
        state (RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfoState | Unset): The licensing state. See
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState. ['Invalid' = 0, 'NotLicensed' = 1,
            'Licensed' = 2, 'Expired' = 3, 'Terminated' = 4]
        license_id (str | Unset): The id of the license backing the agreement. Empty unless
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingInfo.State is
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Licensed,
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Expired, or
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Terminated.
        agreement_id (str | Unset): The id of the agreement backing the license. Empty unless
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingInfo.State is
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Licensed,
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Expired, or
            Roblox.ItemConfiguration.Api.Models.MarketplaceItem.LicensingState.Terminated.
    """

    state: RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfoState | Unset = UNSET
    license_id: str | Unset = UNSET
    agreement_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        state: int | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        license_id = self.license_id

        agreement_id = self.agreement_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if agreement_id is not UNSET:
            field_dict["agreementId"] = agreement_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfoState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfoState(_state)

        license_id = d.pop("licenseId", UNSET)

        agreement_id = d.pop("agreementId", UNSET)

        roblox_item_configuration_api_models_marketplace_item_licensing_info = cls(
            state=state,
            license_id=license_id,
            agreement_id=agreement_id,
        )

        return roblox_item_configuration_api_models_marketplace_item_licensing_info
