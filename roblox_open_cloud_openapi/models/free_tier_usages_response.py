from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_tier_usage_item import FreeTierUsageItem


T = TypeVar("T", bound="FreeTierUsagesResponse")


@_attrs_define
class FreeTierUsagesResponse:
    """Response object for free-tier usage on the Service Unlock page.
    One entry per resource that opts in to a monthly free tier (i.e. monthly_free_units > 0).

        Attributes:
            month_start_utc (datetime.datetime | Unset): Gets or sets UTC midnight of the first day of the month covered by
                this response.
            usages (list[FreeTierUsageItem] | None | Unset): Gets or sets per-resource free-tier usage snapshots.
    """

    month_start_utc: datetime.datetime | Unset = UNSET
    usages: list[FreeTierUsageItem] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        month_start_utc: str | Unset = UNSET
        if not isinstance(self.month_start_utc, Unset):
            month_start_utc = self.month_start_utc.isoformat()

        usages: list[dict[str, Any]] | None | Unset
        if isinstance(self.usages, Unset):
            usages = UNSET
        elif isinstance(self.usages, list):
            usages = []
            for usages_type_0_item_data in self.usages:
                usages_type_0_item = usages_type_0_item_data.to_dict()
                usages.append(usages_type_0_item)

        else:
            usages = self.usages

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if month_start_utc is not UNSET:
            field_dict["monthStartUtc"] = month_start_utc
        if usages is not UNSET:
            field_dict["usages"] = usages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_tier_usage_item import FreeTierUsageItem  # noqa: PLC0415

        d = dict(src_dict)
        _month_start_utc = d.pop("monthStartUtc", UNSET)
        month_start_utc: datetime.datetime | Unset
        if isinstance(_month_start_utc, Unset):
            month_start_utc = UNSET
        else:
            month_start_utc = datetime.datetime.fromisoformat(_month_start_utc)

        def _parse_usages(data: object) -> list[FreeTierUsageItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                usages_type_0 = []
                _usages_type_0 = data
                for usages_type_0_item_data in _usages_type_0:
                    usages_type_0_item = FreeTierUsageItem.from_dict(usages_type_0_item_data)

                    usages_type_0.append(usages_type_0_item)

                return usages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FreeTierUsageItem] | None | Unset, data)

        usages = _parse_usages(d.pop("usages", UNSET))

        free_tier_usages_response = cls(
            month_start_utc=month_start_utc,
            usages=usages,
        )

        return free_tier_usages_response
