from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FreeTierUsageItem")


@_attrs_define
class FreeTierUsageItem:
    """Per-resource free-tier usage snapshot.

    Attributes:
        service_id (None | str | Unset): Gets or sets the service identifier (e.g. "rcc").
        resource_id (None | str | Unset): Gets or sets the resource identifier (e.g. "ccu-cores").
        monthly_free_units (int | Unset): Gets or sets the current monthly free-tier cap from pricing config.
        consumed (float | Unset): Gets or sets the live month-to-date consumed units.
        remaining (float | Unset): Gets or sets the live month-to-date remaining units.
        last_updated_utc (datetime.datetime | Unset): Gets or sets the time at which this snapshot was projected.
    """

    service_id: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    monthly_free_units: int | Unset = UNSET
    consumed: float | Unset = UNSET
    remaining: float | Unset = UNSET
    last_updated_utc: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_id: None | str | Unset
        if isinstance(self.service_id, Unset):
            service_id = UNSET
        else:
            service_id = self.service_id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        monthly_free_units = self.monthly_free_units

        consumed = self.consumed

        remaining = self.remaining

        last_updated_utc: str | Unset = UNSET
        if not isinstance(self.last_updated_utc, Unset):
            last_updated_utc = self.last_updated_utc.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if monthly_free_units is not UNSET:
            field_dict["monthlyFreeUnits"] = monthly_free_units
        if consumed is not UNSET:
            field_dict["consumed"] = consumed
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if last_updated_utc is not UNSET:
            field_dict["lastUpdatedUtc"] = last_updated_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_service_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_id = _parse_service_id(d.pop("serviceId", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        monthly_free_units = d.pop("monthlyFreeUnits", UNSET)

        consumed = d.pop("consumed", UNSET)

        remaining = d.pop("remaining", UNSET)

        _last_updated_utc = d.pop("lastUpdatedUtc", UNSET)
        last_updated_utc: datetime.datetime | Unset
        if isinstance(_last_updated_utc, Unset):
            last_updated_utc = UNSET
        else:
            last_updated_utc = datetime.datetime.fromisoformat(_last_updated_utc)

        free_tier_usage_item = cls(
            service_id=service_id,
            resource_id=resource_id,
            monthly_free_units=monthly_free_units,
            consumed=consumed,
            remaining=remaining,
            last_updated_utc=last_updated_utc,
        )

        return free_tier_usage_item
