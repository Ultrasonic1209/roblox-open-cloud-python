from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_item_asset_details import InventoryItemAssetDetails
    from ..models.inventory_item_badge_details import InventoryItemBadgeDetails
    from ..models.inventory_item_game_pass_details import InventoryItemGamePassDetails
    from ..models.inventory_item_private_server_details import InventoryItemPrivateServerDetails


T = TypeVar("T", bound="InventoryItem")


@_attrs_define
class InventoryItem:
    """Represents an item in a user's inventory.

    Attributes:
        path (str | Unset): The resource path of the inventory item.

            Format: `users/{user_id}/inventory-items/{inventory_item_id}` Example: users/123/inventory-items/some-inventory-
            item-id.
        asset_details (InventoryItemAssetDetails | Unset): Specific fields only applicable to assets
        badge_details (InventoryItemBadgeDetails | Unset): Specific fields that are applicable to a badge.
        game_pass_details (InventoryItemGamePassDetails | Unset): Specific fields that are applicable to a game pass.
        private_server_details (InventoryItemPrivateServerDetails | Unset): Specific fields that are applicable to a
            private server.
        add_time (datetime.datetime | Unset): The time when the item was added to the user's inventory. For example, the
            time when the user purchased a private server or was awarded a badge.

            This field is currently not populated for passes. Example: 2023-07-05T12:34:56Z.
    """

    path: str | Unset = UNSET
    asset_details: InventoryItemAssetDetails | Unset = UNSET
    badge_details: InventoryItemBadgeDetails | Unset = UNSET
    game_pass_details: InventoryItemGamePassDetails | Unset = UNSET
    private_server_details: InventoryItemPrivateServerDetails | Unset = UNSET
    add_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        asset_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_details, Unset):
            asset_details = self.asset_details.to_dict()

        badge_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.badge_details, Unset):
            badge_details = self.badge_details.to_dict()

        game_pass_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.game_pass_details, Unset):
            game_pass_details = self.game_pass_details.to_dict()

        private_server_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_server_details, Unset):
            private_server_details = self.private_server_details.to_dict()

        add_time: str | Unset = UNSET
        if not isinstance(self.add_time, Unset):
            add_time = self.add_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if asset_details is not UNSET:
            field_dict["assetDetails"] = asset_details
        if badge_details is not UNSET:
            field_dict["badgeDetails"] = badge_details
        if game_pass_details is not UNSET:
            field_dict["gamePassDetails"] = game_pass_details
        if private_server_details is not UNSET:
            field_dict["privateServerDetails"] = private_server_details
        if add_time is not UNSET:
            field_dict["addTime"] = add_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_item_asset_details import InventoryItemAssetDetails
        from ..models.inventory_item_badge_details import InventoryItemBadgeDetails
        from ..models.inventory_item_game_pass_details import InventoryItemGamePassDetails
        from ..models.inventory_item_private_server_details import InventoryItemPrivateServerDetails

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        _asset_details = d.pop("assetDetails", UNSET)
        asset_details: InventoryItemAssetDetails | Unset
        if isinstance(_asset_details, Unset):
            asset_details = UNSET
        else:
            asset_details = InventoryItemAssetDetails.from_dict(_asset_details)

        _badge_details = d.pop("badgeDetails", UNSET)
        badge_details: InventoryItemBadgeDetails | Unset
        if isinstance(_badge_details, Unset):
            badge_details = UNSET
        else:
            badge_details = InventoryItemBadgeDetails.from_dict(_badge_details)

        _game_pass_details = d.pop("gamePassDetails", UNSET)
        game_pass_details: InventoryItemGamePassDetails | Unset
        if isinstance(_game_pass_details, Unset):
            game_pass_details = UNSET
        else:
            game_pass_details = InventoryItemGamePassDetails.from_dict(_game_pass_details)

        _private_server_details = d.pop("privateServerDetails", UNSET)
        private_server_details: InventoryItemPrivateServerDetails | Unset
        if isinstance(_private_server_details, Unset):
            private_server_details = UNSET
        else:
            private_server_details = InventoryItemPrivateServerDetails.from_dict(_private_server_details)

        _add_time = d.pop("addTime", UNSET)
        add_time: datetime.datetime | Unset
        if isinstance(_add_time, Unset):
            add_time = UNSET
        else:
            add_time = datetime.datetime.fromisoformat(_add_time)

        inventory_item = cls(
            path=path,
            asset_details=asset_details,
            badge_details=badge_details,
            game_pass_details=game_pass_details,
            private_server_details=private_server_details,
            add_time=add_time,
        )

        inventory_item.additional_properties = d
        return inventory_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
