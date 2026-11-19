from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_collectibles_bulk_update_targets_asset_type_item import (
    RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargetsAssetTypeItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_target_model import RobloxItemConfigurationApiTargetModel


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets:
    """Targets model for bulk update.

    Attributes:
        asset_type (list[RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargetsAssetTypeItem] | Unset):
            The asset type for which we should update all items.
        target (list[RobloxItemConfigurationApiTargetModel] | Unset): A specific target to update.
    """

    asset_type: list[RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargetsAssetTypeItem] | Unset = UNSET
    target: list[RobloxItemConfigurationApiTargetModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_type: list[int] | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = []
            for asset_type_item_data in self.asset_type:
                asset_type_item = asset_type_item_data.value
                asset_type.append(asset_type_item)

        target: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = []
            for target_item_data in self.target:
                target_item = target_item_data.to_dict()
                target.append(target_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_target_model import RobloxItemConfigurationApiTargetModel  # noqa: PLC0415

        d = dict(src_dict)
        _asset_type = d.pop("assetType", UNSET)
        asset_type: list[RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargetsAssetTypeItem] | Unset = (
            UNSET
        )
        if _asset_type is not UNSET:
            asset_type = []
            for asset_type_item_data in _asset_type:
                asset_type_item = RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargetsAssetTypeItem(
                    asset_type_item_data
                )

                asset_type.append(asset_type_item)

        _target = d.pop("target", UNSET)
        target: list[RobloxItemConfigurationApiTargetModel] | Unset = UNSET
        if _target is not UNSET:
            target = []
            for target_item_data in _target:
                target_item = RobloxItemConfigurationApiTargetModel.from_dict(target_item_data)

                target.append(target_item)

        roblox_item_configuration_api_models_request_collectibles_bulk_update_targets = cls(
            asset_type=asset_type,
            target=target,
        )

        return roblox_item_configuration_api_models_request_collectibles_bulk_update_targets
