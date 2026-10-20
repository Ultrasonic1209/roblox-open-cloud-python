from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney
    from ..models.service_usage import ServiceUsage


T = TypeVar("T", bound="ConsumerUsage")


@_attrs_define
class ConsumerUsage:
    """Usages of a consumer, e.g. my cool universe.

    Attributes:
        consumer_id (int): Gets or sets the consumer Id.
        subtotal_amount (ServiceEfficiencyApiMoney): Temporary until https://roblox.atlassian.net/browse/ICSC-1360 is
            done.
            Will be replaced by google.type.Money
        service_usages (list[ServiceUsage]): Gets or sets the list of service usages.
        consumer_name (None | str | Unset): Gets or sets consumer name.
    """

    consumer_id: int
    subtotal_amount: ServiceEfficiencyApiMoney
    service_usages: list[ServiceUsage]
    consumer_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consumer_id = self.consumer_id

        subtotal_amount = self.subtotal_amount.to_dict()

        service_usages = []
        for service_usages_item_data in self.service_usages:
            service_usages_item = service_usages_item_data.to_dict()
            service_usages.append(service_usages_item)

        consumer_name: None | str | Unset
        if isinstance(self.consumer_name, Unset):
            consumer_name = UNSET
        else:
            consumer_name = self.consumer_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "consumerId": consumer_id,
                "subtotalAmount": subtotal_amount,
                "serviceUsages": service_usages,
            }
        )
        if consumer_name is not UNSET:
            field_dict["consumerName"] = consumer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_efficiency_api_money import ServiceEfficiencyApiMoney  # noqa: PLC0415
        from ..models.service_usage import ServiceUsage  # noqa: PLC0415

        d = dict(src_dict)
        consumer_id = d.pop("consumerId")

        subtotal_amount = ServiceEfficiencyApiMoney.from_dict(d.pop("subtotalAmount"))

        service_usages = []
        _service_usages = d.pop("serviceUsages")
        for service_usages_item_data in _service_usages:
            service_usages_item = ServiceUsage.from_dict(service_usages_item_data)

            service_usages.append(service_usages_item)

        def _parse_consumer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consumer_name = _parse_consumer_name(d.pop("consumerName", UNSET))

        consumer_usage = cls(
            consumer_id=consumer_id,
            subtotal_amount=subtotal_amount,
            service_usages=service_usages,
            consumer_name=consumer_name,
        )

        return consumer_usage
