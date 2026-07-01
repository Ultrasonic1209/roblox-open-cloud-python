from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_information_struct import PriceInformationStruct


T = TypeVar("T", bound="DeveloperProductConfigV2")


@_attrs_define
class DeveloperProductConfigV2:
    """Creator-facing representation of a developer product configuration.

    Attributes:
        product_id (int): The product ID of the developer product.
        name (str): The name of the developer product.
        description (str): The description of the developer product.
        icon_image_asset_id (int | None): The icon image (thumbnail) asset ID of the developer product.
        universe_id (int): The universe ID that the developer product belongs to.
        is_for_sale (bool): Whether the developer product is currently on sale.
        price_information (None | PriceInformationStruct): The pricing configuration associated with the product.
        is_immutable (bool): Whether the developer product cannot be modified, such as when created as a commerce
            product.
        created_timestamp (datetime.datetime): The timestamp when the developer product was created.
        updated_timestamp (datetime.datetime): The timestamp when the developer product was last updated.
        is_managed_pricing_enabled (bool): Whether managed pricing is enabled for the developer product.
        store_page_enabled (bool | None | Unset): Whether the developer product is currently available for purchase on
            the external store page.
    """

    product_id: int
    name: str
    description: str
    icon_image_asset_id: int | None
    universe_id: int
    is_for_sale: bool
    price_information: None | PriceInformationStruct
    is_immutable: bool
    created_timestamp: datetime.datetime
    updated_timestamp: datetime.datetime
    is_managed_pricing_enabled: bool
    store_page_enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.price_information_struct import PriceInformationStruct

        product_id = self.product_id

        name = self.name

        description = self.description

        icon_image_asset_id: int | None
        icon_image_asset_id = self.icon_image_asset_id

        universe_id = self.universe_id

        is_for_sale = self.is_for_sale

        price_information: dict[str, Any] | None
        if isinstance(self.price_information, PriceInformationStruct):
            price_information = self.price_information.to_dict()
        else:
            price_information = self.price_information

        is_immutable = self.is_immutable

        created_timestamp = self.created_timestamp.isoformat()

        updated_timestamp = self.updated_timestamp.isoformat()

        is_managed_pricing_enabled = self.is_managed_pricing_enabled

        store_page_enabled: bool | None | Unset
        if isinstance(self.store_page_enabled, Unset):
            store_page_enabled = UNSET
        else:
            store_page_enabled = self.store_page_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "productId": product_id,
                "name": name,
                "description": description,
                "iconImageAssetId": icon_image_asset_id,
                "universeId": universe_id,
                "isForSale": is_for_sale,
                "priceInformation": price_information,
                "isImmutable": is_immutable,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "isManagedPricingEnabled": is_managed_pricing_enabled,
            }
        )
        if store_page_enabled is not UNSET:
            field_dict["storePageEnabled"] = store_page_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_information_struct import PriceInformationStruct

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        product_id = d.pop("productId")

        name = d.pop("name")

        description = d.pop("description")

        def _parse_icon_image_asset_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        icon_image_asset_id = _parse_icon_image_asset_id(d.pop("iconImageAssetId"))

        universe_id = d.pop("universeId")

        is_for_sale = d.pop("isForSale")

        def _parse_price_information(data: object) -> None | PriceInformationStruct:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_information_type_1 = PriceInformationStruct.from_dict(data)

                return price_information_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PriceInformationStruct, data)

        price_information = _parse_price_information(d.pop("priceInformation"))

        is_immutable = d.pop("isImmutable")

        created_timestamp = datetime.datetime.fromisoformat(d.pop("createdTimestamp"))

        updated_timestamp = datetime.datetime.fromisoformat(d.pop("updatedTimestamp"))

        is_managed_pricing_enabled = d.pop("isManagedPricingEnabled")

        def _parse_store_page_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        store_page_enabled = _parse_store_page_enabled(d.pop("storePageEnabled", UNSET))

        developer_product_config_v2 = cls(
            product_id=product_id,
            name=name,
            description=description,
            icon_image_asset_id=icon_image_asset_id,
            universe_id=universe_id,
            is_for_sale=is_for_sale,
            price_information=price_information,
            is_immutable=is_immutable,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            is_managed_pricing_enabled=is_managed_pricing_enabled,
            store_page_enabled=store_page_enabled,
        )

        return developer_product_config_v2
