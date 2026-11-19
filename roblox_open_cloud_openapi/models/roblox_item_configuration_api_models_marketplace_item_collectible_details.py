from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_marketplace_item_licensing_info import (
        RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails:
    """Details specific to a collectible item. Set only when the item is a collectible.

    Attributes:
        collectible_item_id (str | Unset): The collectible item id.
        quantity_limit_per_user (int | Unset): The max number of instances of the collectible item a user can own. Null
            if there is no limit.
        total_restocked_quantity (int | Unset): The total quantity that has been restocked for the collectible item.
        last_restocked_time (datetime.datetime | Unset): The time the collectible item was last restocked.
        is_resellable (bool | Unset): Whether the collectible item is resellable.
        total_quantity (int | Unset): The total quantity available for the collectible item.
        licensing_info (RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo | Unset): Licensing info for the
            collectible item.
    """

    collectible_item_id: str | Unset = UNSET
    quantity_limit_per_user: int | Unset = UNSET
    total_restocked_quantity: int | Unset = UNSET
    last_restocked_time: datetime.datetime | Unset = UNSET
    is_resellable: bool | Unset = UNSET
    total_quantity: int | Unset = UNSET
    licensing_info: RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collectible_item_id = self.collectible_item_id

        quantity_limit_per_user = self.quantity_limit_per_user

        total_restocked_quantity = self.total_restocked_quantity

        last_restocked_time: str | Unset = UNSET
        if not isinstance(self.last_restocked_time, Unset):
            last_restocked_time = self.last_restocked_time.isoformat()

        is_resellable = self.is_resellable

        total_quantity = self.total_quantity

        licensing_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.licensing_info, Unset):
            licensing_info = self.licensing_info.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collectible_item_id is not UNSET:
            field_dict["collectibleItemId"] = collectible_item_id
        if quantity_limit_per_user is not UNSET:
            field_dict["quantityLimitPerUser"] = quantity_limit_per_user
        if total_restocked_quantity is not UNSET:
            field_dict["totalRestockedQuantity"] = total_restocked_quantity
        if last_restocked_time is not UNSET:
            field_dict["lastRestockedTime"] = last_restocked_time
        if is_resellable is not UNSET:
            field_dict["isResellable"] = is_resellable
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if licensing_info is not UNSET:
            field_dict["licensingInfo"] = licensing_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_marketplace_item_licensing_info import (
            RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        collectible_item_id = d.pop("collectibleItemId", UNSET)

        quantity_limit_per_user = d.pop("quantityLimitPerUser", UNSET)

        total_restocked_quantity = d.pop("totalRestockedQuantity", UNSET)

        _last_restocked_time = d.pop("lastRestockedTime", UNSET)
        last_restocked_time: datetime.datetime | Unset
        if isinstance(_last_restocked_time, Unset):
            last_restocked_time = UNSET
        else:
            last_restocked_time = datetime.datetime.fromisoformat(_last_restocked_time)

        is_resellable = d.pop("isResellable", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        _licensing_info = d.pop("licensingInfo", UNSET)
        licensing_info: RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo | Unset
        if isinstance(_licensing_info, Unset):
            licensing_info = UNSET
        else:
            licensing_info = RobloxItemConfigurationApiModelsMarketplaceItemLicensingInfo.from_dict(_licensing_info)

        roblox_item_configuration_api_models_marketplace_item_collectible_details = cls(
            collectible_item_id=collectible_item_id,
            quantity_limit_per_user=quantity_limit_per_user,
            total_restocked_quantity=total_restocked_quantity,
            last_restocked_time=last_restocked_time,
            is_resellable=is_resellable,
            total_quantity=total_quantity,
            licensing_info=licensing_info,
        )

        return roblox_item_configuration_api_models_marketplace_item_collectible_details
