from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_inventory_api_models_user_model import RobloxInventoryApiModelsUserModel


T = TypeVar("T", bound="RobloxInventoryApiModelsInventoryItemModel")


@_attrs_define
class RobloxInventoryApiModelsInventoryItemModel:
    """A model containing information about an inventory item.

    Attributes:
        expire_at (datetime.datetime | Unset): Expiration timestamp for transient items
        user_asset_id (int | Unset): The user asset id
        asset_id (int | Unset): The asset id of the user asset
        asset_name (str | Unset): The asset name of the user asset
        collectible_item_id (str | Unset): The id of the corresponding collectible item
        collectible_item_instance_id (str | Unset): The id of the corresponding collectible item instance
        serial_number (int | Unset): The serial number of the user asset
        owner (RobloxInventoryApiModelsUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        created (datetime.datetime | Unset): The creation date of the user asset
        updated (datetime.datetime | Unset): The updated date of the user asset
    """

    expire_at: datetime.datetime | Unset = UNSET
    user_asset_id: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    asset_name: str | Unset = UNSET
    collectible_item_id: str | Unset = UNSET
    collectible_item_instance_id: str | Unset = UNSET
    serial_number: int | Unset = UNSET
    owner: RobloxInventoryApiModelsUserModel | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expire_at: str | Unset = UNSET
        if not isinstance(self.expire_at, Unset):
            expire_at = self.expire_at.isoformat()

        user_asset_id = self.user_asset_id

        asset_id = self.asset_id

        asset_name = self.asset_name

        collectible_item_id = self.collectible_item_id

        collectible_item_instance_id = self.collectible_item_instance_id

        serial_number = self.serial_number

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expire_at is not UNSET:
            field_dict["expireAt"] = expire_at
        if user_asset_id is not UNSET:
            field_dict["userAssetId"] = user_asset_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if collectible_item_id is not UNSET:
            field_dict["collectibleItemId"] = collectible_item_id
        if collectible_item_instance_id is not UNSET:
            field_dict["collectibleItemInstanceId"] = collectible_item_instance_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if owner is not UNSET:
            field_dict["owner"] = owner
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_inventory_api_models_user_model import RobloxInventoryApiModelsUserModel

        d = dict(src_dict)
        _expire_at = d.pop("expireAt", UNSET)
        expire_at: datetime.datetime | Unset
        if isinstance(_expire_at, Unset):
            expire_at = UNSET
        else:
            expire_at = datetime.datetime.fromisoformat(_expire_at)

        user_asset_id = d.pop("userAssetId", UNSET)

        asset_id = d.pop("assetId", UNSET)

        asset_name = d.pop("assetName", UNSET)

        collectible_item_id = d.pop("collectibleItemId", UNSET)

        collectible_item_instance_id = d.pop("collectibleItemInstanceId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: RobloxInventoryApiModelsUserModel | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxInventoryApiModelsUserModel.from_dict(_owner)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        roblox_inventory_api_models_inventory_item_model = cls(
            expire_at=expire_at,
            user_asset_id=user_asset_id,
            asset_id=asset_id,
            asset_name=asset_name,
            collectible_item_id=collectible_item_id,
            collectible_item_instance_id=collectible_item_instance_id,
            serial_number=serial_number,
            owner=owner,
            created=created,
            updated=updated,
        )

        return roblox_inventory_api_models_inventory_item_model
