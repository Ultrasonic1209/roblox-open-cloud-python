from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_fixed_granularity_granularity_type_0_type_0 import (
    DashboardFixedGranularityGranularityType0Type0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardFixedGranularity")


@_attrs_define
class DashboardFixedGranularity:
    """DashboardFixedGranularity fixes a surface to one granularity.

    Attributes:
        granularity (DashboardFixedGranularityGranularityType0Type0 | int | None | Unset): DashboardGranularity is the
            time bucketing for chart and summary-card queries.
            Synthesis maps each value to Creator Hub `TimeInterval` literals and then to
            `MetricGranularity` in RAQI. INVALID is rejected on write. Default:
            DashboardFixedGranularityGranularityType0Type0.DASHBOARD_GRANULARITY_INVALID.
    """

    granularity: DashboardFixedGranularityGranularityType0Type0 | int | None | Unset = (
        DashboardFixedGranularityGranularityType0Type0.DASHBOARD_GRANULARITY_INVALID
    )

    def to_dict(self) -> dict[str, Any]:
        granularity: int | None | str | Unset
        if isinstance(self.granularity, Unset):
            granularity = UNSET
        elif isinstance(self.granularity, DashboardFixedGranularityGranularityType0Type0):
            granularity = self.granularity.value
        else:
            granularity = self.granularity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if granularity is not UNSET:
            field_dict["granularity"] = granularity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_granularity(data: object) -> DashboardFixedGranularityGranularityType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                granularity_type_0_type_0 = DashboardFixedGranularityGranularityType0Type0(data)

                return granularity_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardFixedGranularityGranularityType0Type0 | int | None | Unset, data)

        granularity = _parse_granularity(d.pop("granularity", UNSET))

        dashboard_fixed_granularity = cls(
            granularity=granularity,
        )

        return dashboard_fixed_granularity
