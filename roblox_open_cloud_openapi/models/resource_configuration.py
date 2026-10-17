from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price import Price
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="ResourceConfiguration")


@_attrs_define
class ResourceConfiguration:
    """Configuration for a resource, like Memory Stores request unit.

    Attributes:
        resource_id (str): Gets or sets the resource ID.
        unlocked (bool): Gets or sets a value indicating whether the resource has unlocked additional usage.
        unit_cost (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is done.
            Will be replaced by google.type.Money
        price (Price): Describes the price of a resource.
        monthly_budget (None | ServiceEfficiencyApiMoney | Unset): Gets or sets the monthly budget.
    """

    resource_id: str
    unlocked: bool
    unit_cost: ServiceEfficiencyApiMoney
    price: Price
    monthly_budget: None | ServiceEfficiencyApiMoney | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        resource_id = self.resource_id

        unlocked = self.unlocked

        unit_cost = self.unit_cost.to_dict()

        price = self.price.to_dict()

        monthly_budget: dict[str, Any] | None | Unset
        if isinstance(self.monthly_budget, Unset):
            monthly_budget = UNSET
        elif isinstance(self.monthly_budget, ServiceEfficiencyApiMoney):
            monthly_budget = self.monthly_budget.to_dict()
        else:
            monthly_budget = self.monthly_budget

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceId": resource_id,
                "unlocked": unlocked,
                "unitCost": unit_cost,
                "price": price,
            }
        )
        if monthly_budget is not UNSET:
            field_dict["monthlyBudget"] = monthly_budget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price import Price
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        resource_id = d.pop("resourceId")

        unlocked = d.pop("unlocked")

        unit_cost = ServiceEfficiencyApiMoney.from_dict(d.pop("unitCost"))

        price = Price.from_dict(d.pop("price"))

        def _parse_monthly_budget(data: object) -> None | ServiceEfficiencyApiMoney | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monthly_budget_type_1 = ServiceEfficiencyApiMoney.from_dict(data)

                return monthly_budget_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServiceEfficiencyApiMoney | Unset, data)

        monthly_budget = _parse_monthly_budget(d.pop("monthlyBudget", UNSET))

        resource_configuration = cls(
            resource_id=resource_id,
            unlocked=unlocked,
            unit_cost=unit_cost,
            price=price,
            monthly_budget=monthly_budget,
        )

        return resource_configuration
