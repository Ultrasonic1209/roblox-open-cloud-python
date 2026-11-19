from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundlePriceRange")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundlePriceRange:
    """DTO containing price range.

    Attributes:
        minimum_price (int | Unset): The minimum allowed price in Robux.
        maximum_price (int | Unset): The maximum allowed price in Robux.
    """

    minimum_price: int | Unset = UNSET
    maximum_price: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        minimum_price = self.minimum_price

        maximum_price = self.maximum_price

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if minimum_price is not UNSET:
            field_dict["minimumPrice"] = minimum_price
        if maximum_price is not UNSET:
            field_dict["maximumPrice"] = maximum_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimum_price = d.pop("minimumPrice", UNSET)

        maximum_price = d.pop("maximumPrice", UNSET)

        roblox_item_configuration_api_models_response_bundle_price_range = cls(
            minimum_price=minimum_price,
            maximum_price=maximum_price,
        )

        return roblox_item_configuration_api_models_response_bundle_price_range
