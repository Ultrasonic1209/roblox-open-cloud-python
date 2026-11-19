from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_publishing_fee_info import (
        RobloxItemConfigurationApiModelsResponsePublishingFeeInfo,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseGetPriceFloorResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseGetPriceFloorResponse:
    """Defines the response model for the GET v1/items/price-floor endpoint.

    Attributes:
        price_floor (int | Unset): The price floor.
        paid_item_publishing_fee (RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset): A publishing fee
            returned with the price floor.
        free_item_publishing_fee (RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset): A publishing fee
            returned with the price floor.
    """

    price_floor: int | Unset = UNSET
    paid_item_publishing_fee: RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset = UNSET
    free_item_publishing_fee: RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_floor = self.price_floor

        paid_item_publishing_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paid_item_publishing_fee, Unset):
            paid_item_publishing_fee = self.paid_item_publishing_fee.to_dict()

        free_item_publishing_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_item_publishing_fee, Unset):
            free_item_publishing_fee = self.free_item_publishing_fee.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if price_floor is not UNSET:
            field_dict["priceFloor"] = price_floor
        if paid_item_publishing_fee is not UNSET:
            field_dict["paidItemPublishingFee"] = paid_item_publishing_fee
        if free_item_publishing_fee is not UNSET:
            field_dict["freeItemPublishingFee"] = free_item_publishing_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_publishing_fee_info import (
            RobloxItemConfigurationApiModelsResponsePublishingFeeInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        price_floor = d.pop("priceFloor", UNSET)

        _paid_item_publishing_fee = d.pop("paidItemPublishingFee", UNSET)
        paid_item_publishing_fee: RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset
        if isinstance(_paid_item_publishing_fee, Unset):
            paid_item_publishing_fee = UNSET
        else:
            paid_item_publishing_fee = RobloxItemConfigurationApiModelsResponsePublishingFeeInfo.from_dict(
                _paid_item_publishing_fee
            )

        _free_item_publishing_fee = d.pop("freeItemPublishingFee", UNSET)
        free_item_publishing_fee: RobloxItemConfigurationApiModelsResponsePublishingFeeInfo | Unset
        if isinstance(_free_item_publishing_fee, Unset):
            free_item_publishing_fee = UNSET
        else:
            free_item_publishing_fee = RobloxItemConfigurationApiModelsResponsePublishingFeeInfo.from_dict(
                _free_item_publishing_fee
            )

        roblox_item_configuration_api_models_response_get_price_floor_response = cls(
            price_floor=price_floor,
            paid_item_publishing_fee=paid_item_publishing_fee,
            free_item_publishing_fee=free_item_publishing_fee,
        )

        return roblox_item_configuration_api_models_response_get_price_floor_response
