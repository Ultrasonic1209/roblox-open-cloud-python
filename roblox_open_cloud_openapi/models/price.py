from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="Price")


@_attrs_define
class Price:
    """Describes the price of a resource.

    Attributes:
        cost (None | ServiceEfficiencyApiMoney | Unset): Cost of the resource.
        unit_amount (int | Unset): The number of units of the resource to which the cost applies. For example, if `cost`
            is 0.0044 and `unit_amount` is
            1000000, the cost is $0.0044 per million of units. The split between `cost` and `unit_amount` should reflect how
            we
            refer to the price in real life, e.g. the above example reflects how we talk about the price of UMS request
            units
            ($0.0044 per million request units).
    """

    cost: None | ServiceEfficiencyApiMoney | Unset = UNSET
    unit_amount: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        cost: dict[str, Any] | None | Unset
        if isinstance(self.cost, Unset):
            cost = UNSET
        elif isinstance(self.cost, ServiceEfficiencyApiMoney):
            cost = self.cost.to_dict()
        else:
            cost = self.cost

        unit_amount = self.unit_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_cost(data: object) -> None | ServiceEfficiencyApiMoney | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cost_type_1 = ServiceEfficiencyApiMoney.from_dict(data)

                return cost_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServiceEfficiencyApiMoney | Unset, data)

        cost = _parse_cost(d.pop("cost", UNSET))

        unit_amount = d.pop("unitAmount", UNSET)

        price = cls(
            cost=cost,
            unit_amount=unit_amount,
        )

        return price
