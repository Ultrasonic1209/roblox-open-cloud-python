from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseCollectiblesPriceFloorResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseCollectiblesPriceFloorResponse:
    """Price floor response.

    Attributes:
        price_floor_in_robux (int | Unset): Price floor in Robux.
        display_name (str | Unset): Optional display name for the price floor.
    """

    price_floor_in_robux: int | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_floor_in_robux = self.price_floor_in_robux

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_floor_in_robux is not UNSET:
            field_dict["priceFloorInRobux"] = price_floor_in_robux
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_floor_in_robux = d.pop("priceFloorInRobux", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_item_configuration_api_models_response_collectibles_price_floor_response = cls(
            price_floor_in_robux=price_floor_in_robux,
            display_name=display_name,
        )

        return roblox_item_configuration_api_models_response_collectibles_price_floor_response
