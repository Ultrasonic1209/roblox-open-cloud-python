from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price import Price
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="ResourceUsage")


@_attrs_define
class ResourceUsage:
    """Usage of a resource e.g. Memory Stores Requests.

    Attributes:
        resource_id (str): Gets or sets resource ID.
        unit_cost (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        price (Price): Describes the price of a resource.
        total_cost (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        free_amount (float | Unset): Gets or sets free amount
        paid_amount (float | Unset): Gets or sets paid amount
    """

    resource_id: str
    unit_cost: ServiceEfficiencyApiMoney
    price: Price
    total_cost: ServiceEfficiencyApiMoney
    free_amount: float | Unset = UNSET
    paid_amount: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        unit_cost = self.unit_cost.to_dict()

        price = self.price.to_dict()

        total_cost = self.total_cost.to_dict()

        free_amount = self.free_amount

        paid_amount = self.paid_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceId": resource_id,
                "unitCost": unit_cost,
                "price": price,
                "totalCost": total_cost,
            }
        )
        if free_amount is not UNSET:
            field_dict["freeAmount"] = free_amount
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price import Price
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        resource_id = d.pop("resourceId")

        unit_cost = ServiceEfficiencyApiMoney.from_dict(d.pop("unitCost"))

        price = Price.from_dict(d.pop("price"))

        total_cost = ServiceEfficiencyApiMoney.from_dict(d.pop("totalCost"))

        free_amount = d.pop("freeAmount", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        resource_usage = cls(
            resource_id=resource_id,
            unit_cost=unit_cost,
            price=price,
            total_cost=total_cost,
            free_amount=free_amount,
            paid_amount=paid_amount,
        )

        return resource_usage
