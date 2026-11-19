from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_economy_api_chart_data_point_response import RobloxEconomyApiChartDataPointResponse


T = TypeVar("T", bound="RobloxEconomyApiResaleDataResponse")


@_attrs_define
class RobloxEconomyApiResaleDataResponse:
    """Resale data for an item.

    Attributes:
        asset_stock (int | Unset): The total number of this item that can be sold.
        sales (int | Unset): How many of the item have been sold.
        number_remaining (int | Unset): How many of the item remain to be sold.
        recent_average_price (int | Unset): The recent average selling price of the item.
        original_price (int | Unset): The original selling price for the item.
        price_data_points (list[RobloxEconomyApiChartDataPointResponse] | Unset): Price points for the past 180 days.
        volume_data_points (list[RobloxEconomyApiChartDataPointResponse] | Unset): Volume points for the past 180 days.
    """

    asset_stock: int | Unset = UNSET
    sales: int | Unset = UNSET
    number_remaining: int | Unset = UNSET
    recent_average_price: int | Unset = UNSET
    original_price: int | Unset = UNSET
    price_data_points: list[RobloxEconomyApiChartDataPointResponse] | Unset = UNSET
    volume_data_points: list[RobloxEconomyApiChartDataPointResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_stock = self.asset_stock

        sales = self.sales

        number_remaining = self.number_remaining

        recent_average_price = self.recent_average_price

        original_price = self.original_price

        price_data_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.price_data_points, Unset):
            price_data_points = []
            for price_data_points_item_data in self.price_data_points:
                price_data_points_item = price_data_points_item_data.to_dict()
                price_data_points.append(price_data_points_item)

        volume_data_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.volume_data_points, Unset):
            volume_data_points = []
            for volume_data_points_item_data in self.volume_data_points:
                volume_data_points_item = volume_data_points_item_data.to_dict()
                volume_data_points.append(volume_data_points_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_stock is not UNSET:
            field_dict["assetStock"] = asset_stock
        if sales is not UNSET:
            field_dict["sales"] = sales
        if number_remaining is not UNSET:
            field_dict["numberRemaining"] = number_remaining
        if recent_average_price is not UNSET:
            field_dict["recentAveragePrice"] = recent_average_price
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if price_data_points is not UNSET:
            field_dict["priceDataPoints"] = price_data_points
        if volume_data_points is not UNSET:
            field_dict["volumeDataPoints"] = volume_data_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_economy_api_chart_data_point_response import RobloxEconomyApiChartDataPointResponse  # noqa: PLC0415

        d = dict(src_dict)
        asset_stock = d.pop("assetStock", UNSET)

        sales = d.pop("sales", UNSET)

        number_remaining = d.pop("numberRemaining", UNSET)

        recent_average_price = d.pop("recentAveragePrice", UNSET)

        original_price = d.pop("originalPrice", UNSET)

        _price_data_points = d.pop("priceDataPoints", UNSET)
        price_data_points: list[RobloxEconomyApiChartDataPointResponse] | Unset = UNSET
        if _price_data_points is not UNSET:
            price_data_points = []
            for price_data_points_item_data in _price_data_points:
                price_data_points_item = RobloxEconomyApiChartDataPointResponse.from_dict(price_data_points_item_data)

                price_data_points.append(price_data_points_item)

        _volume_data_points = d.pop("volumeDataPoints", UNSET)
        volume_data_points: list[RobloxEconomyApiChartDataPointResponse] | Unset = UNSET
        if _volume_data_points is not UNSET:
            volume_data_points = []
            for volume_data_points_item_data in _volume_data_points:
                volume_data_points_item = RobloxEconomyApiChartDataPointResponse.from_dict(volume_data_points_item_data)

                volume_data_points.append(volume_data_points_item)

        roblox_economy_api_resale_data_response = cls(
            asset_stock=asset_stock,
            sales=sales,
            number_remaining=number_remaining,
            recent_average_price=recent_average_price,
            original_price=original_price,
            price_data_points=price_data_points,
            volume_data_points=volume_data_points,
        )

        return roblox_economy_api_resale_data_response
