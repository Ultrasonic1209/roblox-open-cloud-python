from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="DeveloperProductsUpdateDeveloperProductV2Body")


@_attrs_define
class DeveloperProductsUpdateDeveloperProductV2Body:
    """
    Attributes:
        name (None | str | Unset): The name of the developer product.
        description (None | str | Unset): The description of the developer product.
        is_for_sale (bool | None | Unset): Whether the developer product should be on sale.
        price (int | None | Unset): The default price of the developer product.
        image_file (File | None | Unset): The thumbnail image file to be uploaded.
        is_regional_pricing_enabled (bool | None | Unset): Whether regional pricing should be enabled for the developer
            product.
        store_page_enabled (bool | None | Unset): Whether the developer product should be available for purchase on the
            external store page.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_for_sale: bool | None | Unset = UNSET
    price: int | None | Unset = UNSET
    image_file: File | None | Unset = UNSET
    is_regional_pricing_enabled: bool | None | Unset = UNSET
    store_page_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_for_sale: bool | None | Unset
        if isinstance(self.is_for_sale, Unset):
            is_for_sale = UNSET
        else:
            is_for_sale = self.is_for_sale

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        image_file: FileTypes | None | Unset
        if isinstance(self.image_file, Unset):
            image_file = UNSET
        elif isinstance(self.image_file, File):
            image_file = self.image_file.to_tuple()

        else:
            image_file = self.image_file

        is_regional_pricing_enabled: bool | None | Unset
        if isinstance(self.is_regional_pricing_enabled, Unset):
            is_regional_pricing_enabled = UNSET
        else:
            is_regional_pricing_enabled = self.is_regional_pricing_enabled

        store_page_enabled: bool | None | Unset
        if isinstance(self.store_page_enabled, Unset):
            store_page_enabled = UNSET
        else:
            store_page_enabled = self.store_page_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_for_sale is not UNSET:
            field_dict["isForSale"] = is_for_sale
        if price is not UNSET:
            field_dict["price"] = price
        if image_file is not UNSET:
            field_dict["imageFile"] = image_file
        if is_regional_pricing_enabled is not UNSET:
            field_dict["isRegionalPricingEnabled"] = is_regional_pricing_enabled
        if store_page_enabled is not UNSET:
            field_dict["storePageEnabled"] = store_page_enabled

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            if isinstance(self.name, str):
                files.append(("name", (None, str(self.name).encode(), "text/plain")))
            else:
                files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.is_for_sale, Unset):
            if isinstance(self.is_for_sale, bool):
                files.append(("isForSale", (None, str(self.is_for_sale).encode(), "text/plain")))
            else:
                files.append(("isForSale", (None, str(self.is_for_sale).encode(), "text/plain")))

        if not isinstance(self.price, Unset):
            if isinstance(self.price, int):
                files.append(("price", (None, str(self.price).encode(), "text/plain")))
            else:
                files.append(("price", (None, str(self.price).encode(), "text/plain")))

        if not isinstance(self.image_file, Unset):
            if isinstance(self.image_file, File):
                files.append(("imageFile", self.image_file.to_tuple()))
            else:
                files.append(("imageFile", (None, str(self.image_file).encode(), "text/plain")))

        if not isinstance(self.is_regional_pricing_enabled, Unset):
            if isinstance(self.is_regional_pricing_enabled, bool):
                files.append(
                    ("isRegionalPricingEnabled", (None, str(self.is_regional_pricing_enabled).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("isRegionalPricingEnabled", (None, str(self.is_regional_pricing_enabled).encode(), "text/plain"))
                )

        if not isinstance(self.store_page_enabled, Unset):
            if isinstance(self.store_page_enabled, bool):
                files.append(("storePageEnabled", (None, str(self.store_page_enabled).encode(), "text/plain")))
            else:
                files.append(("storePageEnabled", (None, str(self.store_page_enabled).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_for_sale(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_for_sale = _parse_is_for_sale(d.pop("isForSale", UNSET))

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_image_file(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_file_type_0 = File(payload=BytesIO(data))

                return image_file_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        image_file = _parse_image_file(d.pop("imageFile", UNSET))

        def _parse_is_regional_pricing_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_regional_pricing_enabled = _parse_is_regional_pricing_enabled(d.pop("isRegionalPricingEnabled", UNSET))

        def _parse_store_page_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        store_page_enabled = _parse_store_page_enabled(d.pop("storePageEnabled", UNSET))

        developer_products_update_developer_product_v2_body = cls(
            name=name,
            description=description,
            is_for_sale=is_for_sale,
            price=price,
            image_file=image_file,
            is_regional_pricing_enabled=is_regional_pricing_enabled,
            store_page_enabled=store_page_enabled,
        )

        developer_products_update_developer_product_v2_body.additional_properties = d
        return developer_products_update_developer_product_v2_body

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
