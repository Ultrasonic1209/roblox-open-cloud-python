from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.service_configuration import ServiceConfiguration


T = TypeVar("T", bound="ConsumerConfigurationRequest")


@_attrs_define
class ConsumerConfigurationRequest:
    """Request for updating consumer configuration.

    Attributes:
        service_configurations (list[ServiceConfiguration]): Gets or sets the service configuration lists.
    """

    service_configurations: list[ServiceConfiguration]

    def to_dict(self) -> dict[str, Any]:
        service_configurations = []
        for service_configurations_item_data in self.service_configurations:
            service_configurations_item = service_configurations_item_data.to_dict()
            service_configurations.append(service_configurations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceConfigurations": service_configurations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_configuration import ServiceConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        service_configurations = []
        _service_configurations = d.pop("serviceConfigurations")
        for service_configurations_item_data in _service_configurations:
            service_configurations_item = ServiceConfiguration.from_dict(service_configurations_item_data)

            service_configurations.append(service_configurations_item)

        consumer_configuration_request = cls(
            service_configurations=service_configurations,
        )

        return consumer_configuration_request
