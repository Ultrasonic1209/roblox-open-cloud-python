from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.resource_usage import ResourceUsage
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney


T = TypeVar("T", bound="ServiceUsage")


@_attrs_define
class ServiceUsage:
    """Usage of a service, e.g. Memory Stores

    Attributes:
        service_id (str): Gets or sets service ID.
        subtotal_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is
            done.
            Will be replaced by google.type.Money
        resource_usages (list[ResourceUsage]): Gets or sets the list of resource usages.
    """

    service_id: str
    subtotal_amount: ServiceEfficiencyApiMoney
    resource_usages: list[ResourceUsage]

    def to_dict(self) -> dict[str, Any]:
        service_id = self.service_id

        subtotal_amount = self.subtotal_amount.to_dict()

        resource_usages = []
        for resource_usages_item_data in self.resource_usages:
            resource_usages_item = resource_usages_item_data.to_dict()
            resource_usages.append(resource_usages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceId": service_id,
                "subtotalAmount": subtotal_amount,
                "resourceUsages": resource_usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage import ResourceUsage
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        service_id = d.pop("serviceId")

        subtotal_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("subtotalAmount"))

        resource_usages = []
        _resource_usages = d.pop("resourceUsages")
        for resource_usages_item_data in _resource_usages:
            resource_usages_item = ResourceUsage.from_dict(resource_usages_item_data)

            resource_usages.append(resource_usages_item)

        service_usage = cls(
            service_id=service_id,
            subtotal_amount=subtotal_amount,
            resource_usages=resource_usages,
        )

        return service_usage
