from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.toolbox_service_money_type_0 import ToolboxServiceMoneyType0


T = TypeVar("T", bound="ToolboxServiceCreatorStoreProductType0")


@_attrs_define
class ToolboxServiceCreatorStoreProductType0:
    """The asset's creator store product information.

    Attributes:
        purchase_price (None | ToolboxServiceMoneyType0 | Unset): The price of the asset, including the currency code.
        purchasable (bool | Unset): Whether or not the asset can be purchased in the Creator Store.
    """

    purchase_price: None | ToolboxServiceMoneyType0 | Unset = UNSET
    purchasable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.toolbox_service_money_type_0 import ToolboxServiceMoneyType0

        purchase_price: dict[str, Any] | None | Unset
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        elif isinstance(self.purchase_price, ToolboxServiceMoneyType0):
            purchase_price = self.purchase_price.to_dict()
        else:
            purchase_price = self.purchase_price

        purchasable = self.purchasable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if purchasable is not UNSET:
            field_dict["purchasable"] = purchasable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.toolbox_service_money_type_0 import ToolboxServiceMoneyType0

        d = dict(src_dict)

        def _parse_purchase_price(data: object) -> None | ToolboxServiceMoneyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_toolbox_service_money_type_0 = ToolboxServiceMoneyType0.from_dict(data)

                return componentsschemas_toolbox_service_money_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolboxServiceMoneyType0 | Unset, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))

        purchasable = d.pop("purchasable", UNSET)

        toolbox_service_creator_store_product_type_0 = cls(
            purchase_price=purchase_price,
            purchasable=purchasable,
        )

        return toolbox_service_creator_store_product_type_0
