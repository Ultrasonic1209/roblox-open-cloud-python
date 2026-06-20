from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creator_store_product_restrictions_item import CreatorStoreProductRestrictionsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="CreatorStoreProduct")


@_attrs_define
class CreatorStoreProduct:
    """Represents a product in the Creator Store. This resource is used to manage
    distribution and pricing of assets on the Creator Store.

        Attributes:
            path (str | Unset): The resource path of the creator store product.

                Format: `creator-store-products/{creator_store_product_id}` Example: creator-store-products/123.
            base_price (Money | Unset): Represents an amount of money with its currency type.

                Examples:
                 - Five US dollars === `{currency_code: "USD" quantity: {significand: 5}}`
            purchase_price (Money | Unset): Represents an amount of money with its currency type.

                Examples:
                 - Five US dollars === `{currency_code: "USD" quantity: {significand: 5}}`
            published (bool | Unset): Whether the seller intends to distribute the Creator Store product on
                the Creator Store. A seller might intend to distribute a product, but due
                to some restrictions on the seller or underlying Creator Store product, the
                product may not be available for purchase. See
                `restrictions` and `purchasable` for more details. Example: True.
            restrictions (list[CreatorStoreProductRestrictionsItem] | Unset): Restrictions applied to the product. A product
                can have multiple
                restrictions active at one time.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | RESTRICTION_UNSPECIFIED | Unspecified restriction. |
                  | SOLD_ITEM_RESTRICTED | The item being sold has been restricted by Roblox  Details may be available by
                looking up that item directly. |
                  | SELLER_TEMPORARILY_RESTRICTED | The product is restricted because the seller's account is temporarily
                restricted by Roblox. |
                  | SELLER_PERMANENTLY_RESTRICTED | The product is restricted because the seller's account is permanently
                restricted by Roblox. |
                  | SELLER_NO_LONGER_ACTIVE | The product is restricted because the seller's account was deleted or is otherwise
                no longer active. |
            purchasable (bool | Unset): Whether the product is purchasable.

                For this value to be true, `published` must be true and `restrictions` must
                be empty. If this value is false, the product may not be acquired by any
                user. Example: True.
            user_seller (str | Unset): The Roblox user selling the product.
            group_seller (str | Unset): The Roblox group selling the product.
            model_asset_id (str | Unset): The Creator Store product is a model with this asset ID.
            plugin_asset_id (str | Unset): The Creator Store product is a plugin with this asset ID.

                Supported base prices in USD: $0, $4.99, $5.99, $6.99, $7.99, $8.99,
                $9.99, $10.99, $11.99, $12.99, $13.99, $14.99, $15.99, $16.99, $17.99,
                $18.99, $19.99, $24.99, $29.99, $34.99, $39.99, $44.99, $49.99, $59.99,
                $69.99, $79.99, $89.99, $99.99, $149.99, $199.99, $249.99
            audio_asset_id (str | Unset): The Creator Store product is an audio file with this asset ID.
            decal_asset_id (str | Unset): The Creator Store product is a decal with this asset ID.
            mesh_part_asset_id (str | Unset): The Creator Store product is a mesh part with this asset ID.
            video_asset_id (str | Unset): The Creator Store product is a video with this asset ID.
            font_family_asset_id (str | Unset): The Creator Store product is a font family with this asset ID.
    """

    path: str | Unset = UNSET
    base_price: Money | Unset = UNSET
    purchase_price: Money | Unset = UNSET
    published: bool | Unset = UNSET
    restrictions: list[CreatorStoreProductRestrictionsItem] | Unset = UNSET
    purchasable: bool | Unset = UNSET
    user_seller: str | Unset = UNSET
    group_seller: str | Unset = UNSET
    model_asset_id: str | Unset = UNSET
    plugin_asset_id: str | Unset = UNSET
    audio_asset_id: str | Unset = UNSET
    decal_asset_id: str | Unset = UNSET
    mesh_part_asset_id: str | Unset = UNSET
    video_asset_id: str | Unset = UNSET
    font_family_asset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        base_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_price, Unset):
            base_price = self.base_price.to_dict()

        purchase_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purchase_price, Unset):
            purchase_price = self.purchase_price.to_dict()

        published = self.published

        restrictions: list[str] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = []
            for restrictions_item_data in self.restrictions:
                restrictions_item = restrictions_item_data.value
                restrictions.append(restrictions_item)

        purchasable = self.purchasable

        user_seller = self.user_seller

        group_seller = self.group_seller

        model_asset_id = self.model_asset_id

        plugin_asset_id = self.plugin_asset_id

        audio_asset_id = self.audio_asset_id

        decal_asset_id = self.decal_asset_id

        mesh_part_asset_id = self.mesh_part_asset_id

        video_asset_id = self.video_asset_id

        font_family_asset_id = self.font_family_asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if base_price is not UNSET:
            field_dict["basePrice"] = base_price
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if published is not UNSET:
            field_dict["published"] = published
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if purchasable is not UNSET:
            field_dict["purchasable"] = purchasable
        if user_seller is not UNSET:
            field_dict["userSeller"] = user_seller
        if group_seller is not UNSET:
            field_dict["groupSeller"] = group_seller
        if model_asset_id is not UNSET:
            field_dict["modelAssetId"] = model_asset_id
        if plugin_asset_id is not UNSET:
            field_dict["pluginAssetId"] = plugin_asset_id
        if audio_asset_id is not UNSET:
            field_dict["audioAssetId"] = audio_asset_id
        if decal_asset_id is not UNSET:
            field_dict["decalAssetId"] = decal_asset_id
        if mesh_part_asset_id is not UNSET:
            field_dict["meshPartAssetId"] = mesh_part_asset_id
        if video_asset_id is not UNSET:
            field_dict["videoAssetId"] = video_asset_id
        if font_family_asset_id is not UNSET:
            field_dict["fontFamilyAssetId"] = font_family_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.money import Money

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        _base_price = d.pop("basePrice", UNSET)
        base_price: Money | Unset
        if isinstance(_base_price, Unset):
            base_price = UNSET
        else:
            base_price = Money.from_dict(_base_price)

        _purchase_price = d.pop("purchasePrice", UNSET)
        purchase_price: Money | Unset
        if isinstance(_purchase_price, Unset):
            purchase_price = UNSET
        else:
            purchase_price = Money.from_dict(_purchase_price)

        published = d.pop("published", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: list[CreatorStoreProductRestrictionsItem] | Unset = UNSET
        if _restrictions is not UNSET:
            restrictions = []
            for restrictions_item_data in _restrictions:
                restrictions_item = CreatorStoreProductRestrictionsItem(restrictions_item_data)

                restrictions.append(restrictions_item)

        purchasable = d.pop("purchasable", UNSET)

        user_seller = d.pop("userSeller", UNSET)

        group_seller = d.pop("groupSeller", UNSET)

        model_asset_id = d.pop("modelAssetId", UNSET)

        plugin_asset_id = d.pop("pluginAssetId", UNSET)

        audio_asset_id = d.pop("audioAssetId", UNSET)

        decal_asset_id = d.pop("decalAssetId", UNSET)

        mesh_part_asset_id = d.pop("meshPartAssetId", UNSET)

        video_asset_id = d.pop("videoAssetId", UNSET)

        font_family_asset_id = d.pop("fontFamilyAssetId", UNSET)

        creator_store_product = cls(
            path=path,
            base_price=base_price,
            purchase_price=purchase_price,
            published=published,
            restrictions=restrictions,
            purchasable=purchasable,
            user_seller=user_seller,
            group_seller=group_seller,
            model_asset_id=model_asset_id,
            plugin_asset_id=plugin_asset_id,
            audio_asset_id=audio_asset_id,
            decal_asset_id=decal_asset_id,
            mesh_part_asset_id=mesh_part_asset_id,
            video_asset_id=video_asset_id,
            font_family_asset_id=font_family_asset_id,
        )

        creator_store_product.additional_properties = d
        return creator_store_product

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
