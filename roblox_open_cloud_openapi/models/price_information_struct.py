from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pricing_feature import PricingFeature

T = TypeVar("T", bound="PriceInformationStruct")


@_attrs_define
class PriceInformationStruct:
    """The pricing configuration information.

    Attributes:
        default_price_in_robux (int | None): The configured default price in Robux.
        enabled_features (list[PricingFeature]): The enabled pricing features for the developer product.
    """

    default_price_in_robux: int | None
    enabled_features: list[PricingFeature]

    def to_dict(self) -> dict[str, Any]:
        default_price_in_robux: int | None
        default_price_in_robux = self.default_price_in_robux

        enabled_features = []
        for enabled_features_item_data in self.enabled_features:
            enabled_features_item = enabled_features_item_data.value
            enabled_features.append(enabled_features_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "defaultPriceInRobux": default_price_in_robux,
                "enabledFeatures": enabled_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_default_price_in_robux(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        default_price_in_robux = _parse_default_price_in_robux(d.pop("defaultPriceInRobux"))

        enabled_features = []
        _enabled_features = d.pop("enabledFeatures")
        for enabled_features_item_data in _enabled_features:
            enabled_features_item = PricingFeature(enabled_features_item_data)

            enabled_features.append(enabled_features_item)

        price_information_struct = cls(
            default_price_in_robux=default_price_in_robux,
            enabled_features=enabled_features,
        )

        return price_information_struct
