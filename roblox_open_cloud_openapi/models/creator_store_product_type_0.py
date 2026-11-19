from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.money_type_0 import MoneyType0


T = TypeVar("T", bound="CreatorStoreProductType0")


@_attrs_define
class CreatorStoreProductType0:
    """The asset's creator store product information.

    Attributes:
        purchase_price (MoneyType0 | None): The price of the asset, including the currency code.
        purchasable (bool): Whether or not the asset can be purchased in the Creator Store.
    """

    purchase_price: MoneyType0 | None
    purchasable: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.money_type_0 import MoneyType0  # noqa: PLC0415

        purchase_price: dict[str, Any] | None
        if isinstance(self.purchase_price, MoneyType0):
            purchase_price = self.purchase_price.to_dict()
        else:
            purchase_price = self.purchase_price

        purchasable = self.purchasable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "purchasePrice": purchase_price,
                "purchasable": purchasable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.money_type_0 import MoneyType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_purchase_price(data: object) -> MoneyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_money_type_0 = MoneyType0.from_dict(data)

                return componentsschemas_money_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MoneyType0 | None, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice"))

        purchasable = d.pop("purchasable")

        creator_store_product_type_0 = cls(
            purchase_price=purchase_price,
            purchasable=purchasable,
        )

        return creator_store_product_type_0
