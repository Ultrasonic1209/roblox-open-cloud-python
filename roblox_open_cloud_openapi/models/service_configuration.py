from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.budget_level import BudgetLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_configuration import ResourceConfiguration
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="ServiceConfiguration")


@_attrs_define
class ServiceConfiguration:
    """Configuration of a service, including whether unlocked and budget.

    Attributes:
        service_id (str): Gets or sets the service ID.
        resource_configurations (list[ResourceConfiguration]): Gets or sets the list of resource configurations.
        budget_level (BudgetLevel): Indicates the allowed budget levels for a service.
        monthly_budget (None | ServiceEfficiencyApiMoney | Unset): Gets or sets the monthly budget.
    """

    service_id: str
    resource_configurations: list[ResourceConfiguration]
    budget_level: BudgetLevel
    monthly_budget: None | ServiceEfficiencyApiMoney | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        service_id = self.service_id

        resource_configurations = []
        for resource_configurations_item_data in self.resource_configurations:
            resource_configurations_item = resource_configurations_item_data.to_dict()
            resource_configurations.append(resource_configurations_item)

        budget_level = self.budget_level.value

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
                "serviceId": service_id,
                "resourceConfigurations": resource_configurations,
                "budgetLevel": budget_level,
            }
        )
        if monthly_budget is not UNSET:
            field_dict["monthlyBudget"] = monthly_budget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_configuration import ResourceConfiguration
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        service_id = d.pop("serviceId")

        resource_configurations = []
        _resource_configurations = d.pop("resourceConfigurations")
        for resource_configurations_item_data in _resource_configurations:
            resource_configurations_item = ResourceConfiguration.from_dict(resource_configurations_item_data)

            resource_configurations.append(resource_configurations_item)

        budget_level = BudgetLevel(d.pop("budgetLevel"))

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

        service_configuration = cls(
            service_id=service_id,
            resource_configurations=resource_configurations,
            budget_level=budget_level,
            monthly_budget=monthly_budget,
        )

        return service_configuration
