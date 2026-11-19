from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_controlled_subcontext_body import DashboardControlledSubcontextBody
    from ..models.dashboard_dimension_filter_and_breakdown_subcontext import (
        DashboardDimensionFilterAndBreakdownSubcontext,
    )
    from ..models.dashboard_time_range_subcontext import DashboardTimeRangeSubcontext


T = TypeVar("T", bound="DashboardControlledSubcontext")


@_attrs_define
class DashboardControlledSubcontext:
    """DashboardControlledSubcontext mirrors RAQI controlled subcontexts as a
    component wrapper, not a layout primitive. It applies local controls/context
    overrides to exactly one chart/table-like body.

        Attributes:
            dimension_filter_and_breakdown (DashboardDimensionFilterAndBreakdownSubcontext | None | Unset):
                DashboardDimensionFilterAndBreakdownSubcontext applies local dimension controls to a component.
            time_range (DashboardTimeRangeSubcontext | None | Unset): DashboardTimeRangeSubcontext applies a local time
                range control to a component.
            body (DashboardControlledSubcontextBody | None | Unset): DashboardControlledSubcontextBody stores the chart or
                table controlled by a local subcontext.
    """

    dimension_filter_and_breakdown: DashboardDimensionFilterAndBreakdownSubcontext | None | Unset = UNSET
    time_range: DashboardTimeRangeSubcontext | None | Unset = UNSET
    body: DashboardControlledSubcontextBody | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_controlled_subcontext_body import DashboardControlledSubcontextBody  # noqa: PLC0415
        from ..models.dashboard_dimension_filter_and_breakdown_subcontext import (
            DashboardDimensionFilterAndBreakdownSubcontext,  # noqa: PLC0415
        )
        from ..models.dashboard_time_range_subcontext import DashboardTimeRangeSubcontext  # noqa: PLC0415

        dimension_filter_and_breakdown: dict[str, Any] | None | Unset
        if isinstance(self.dimension_filter_and_breakdown, Unset):
            dimension_filter_and_breakdown = UNSET
        elif isinstance(self.dimension_filter_and_breakdown, DashboardDimensionFilterAndBreakdownSubcontext):
            dimension_filter_and_breakdown = self.dimension_filter_and_breakdown.to_dict()
        else:
            dimension_filter_and_breakdown = self.dimension_filter_and_breakdown

        time_range: dict[str, Any] | None | Unset
        if isinstance(self.time_range, Unset):
            time_range = UNSET
        elif isinstance(self.time_range, DashboardTimeRangeSubcontext):
            time_range = self.time_range.to_dict()
        else:
            time_range = self.time_range

        body: dict[str, Any] | None | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        elif isinstance(self.body, DashboardControlledSubcontextBody):
            body = self.body.to_dict()
        else:
            body = self.body

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dimension_filter_and_breakdown is not UNSET:
            field_dict["dimensionFilterAndBreakdown"] = dimension_filter_and_breakdown
        if time_range is not UNSET:
            field_dict["timeRange"] = time_range
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_controlled_subcontext_body import DashboardControlledSubcontextBody  # noqa: PLC0415
        from ..models.dashboard_dimension_filter_and_breakdown_subcontext import (
            DashboardDimensionFilterAndBreakdownSubcontext,  # noqa: PLC0415
        )
        from ..models.dashboard_time_range_subcontext import DashboardTimeRangeSubcontext  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_dimension_filter_and_breakdown(
            data: object,
        ) -> DashboardDimensionFilterAndBreakdownSubcontext | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dimension_filter_and_breakdown_type_0 = DashboardDimensionFilterAndBreakdownSubcontext.from_dict(data)

                return dimension_filter_and_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardDimensionFilterAndBreakdownSubcontext | None | Unset, data)

        dimension_filter_and_breakdown = _parse_dimension_filter_and_breakdown(
            d.pop("dimensionFilterAndBreakdown", UNSET)
        )

        def _parse_time_range(data: object) -> DashboardTimeRangeSubcontext | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_range_type_0 = DashboardTimeRangeSubcontext.from_dict(data)

                return time_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTimeRangeSubcontext | None | Unset, data)

        time_range = _parse_time_range(d.pop("timeRange", UNSET))

        def _parse_body(data: object) -> DashboardControlledSubcontextBody | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                body_type_0 = DashboardControlledSubcontextBody.from_dict(data)

                return body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardControlledSubcontextBody | None | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        dashboard_controlled_subcontext = cls(
            dimension_filter_and_breakdown=dimension_filter_and_breakdown,
            time_range=time_range,
            body=body,
        )

        return dashboard_controlled_subcontext
