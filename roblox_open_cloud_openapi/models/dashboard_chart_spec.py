from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_chart_spec_chart_type_type_0_type_0 import DashboardChartSpecChartTypeType0Type0
from ..models.dashboard_chart_spec_smoothing_type_0_type_0 import DashboardChartSpecSmoothingType0Type0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_overlays import ChartOverlays


T = TypeVar("T", bound="DashboardChartSpec")


@_attrs_define
class DashboardChartSpec:
    """DashboardChartSpec carries chart renderer options (not query/data inputs).

    Attributes:
        chart_type (DashboardChartSpecChartTypeType0Type0 | int | None | Unset): DashboardChartType is the visual
            renderer requested by a chart tile. Default: DashboardChartSpecChartTypeType0Type0.DASHBOARD_CHART_TYPE_INVALID.
        overlays (ChartOverlays | None | Unset): ChartOverlays toggles optional chart adornments (display only, not
            query inputs).
        smoothing (DashboardChartSpecSmoothingType0Type0 | int | None | Unset): DashboardChartSmoothing controls
            optional chart smoothing. Default: DashboardChartSpecSmoothingType0Type0.DASHBOARD_CHART_SMOOTHING_INVALID.
    """

    chart_type: DashboardChartSpecChartTypeType0Type0 | int | None | Unset = (
        DashboardChartSpecChartTypeType0Type0.DASHBOARD_CHART_TYPE_INVALID
    )
    overlays: ChartOverlays | None | Unset = UNSET
    smoothing: DashboardChartSpecSmoothingType0Type0 | int | None | Unset = (
        DashboardChartSpecSmoothingType0Type0.DASHBOARD_CHART_SMOOTHING_INVALID
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_overlays import ChartOverlays  # noqa: PLC0415

        chart_type: int | None | str | Unset
        if isinstance(self.chart_type, Unset):
            chart_type = UNSET
        elif isinstance(self.chart_type, DashboardChartSpecChartTypeType0Type0):
            chart_type = self.chart_type.value
        else:
            chart_type = self.chart_type

        overlays: dict[str, Any] | None | Unset
        if isinstance(self.overlays, Unset):
            overlays = UNSET
        elif isinstance(self.overlays, ChartOverlays):
            overlays = self.overlays.to_dict()
        else:
            overlays = self.overlays

        smoothing: int | None | str | Unset
        if isinstance(self.smoothing, Unset):
            smoothing = UNSET
        elif isinstance(self.smoothing, DashboardChartSpecSmoothingType0Type0):
            smoothing = self.smoothing.value
        else:
            smoothing = self.smoothing

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if overlays is not UNSET:
            field_dict["overlays"] = overlays
        if smoothing is not UNSET:
            field_dict["smoothing"] = smoothing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_overlays import ChartOverlays  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_chart_type(data: object) -> DashboardChartSpecChartTypeType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chart_type_type_0_type_0 = DashboardChartSpecChartTypeType0Type0(data)

                return chart_type_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartSpecChartTypeType0Type0 | int | None | Unset, data)

        chart_type = _parse_chart_type(d.pop("chartType", UNSET))

        def _parse_overlays(data: object) -> ChartOverlays | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overlays_type_0 = ChartOverlays.from_dict(data)

                return overlays_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChartOverlays | None | Unset, data)

        overlays = _parse_overlays(d.pop("overlays", UNSET))

        def _parse_smoothing(data: object) -> DashboardChartSpecSmoothingType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smoothing_type_0_type_0 = DashboardChartSpecSmoothingType0Type0(data)

                return smoothing_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartSpecSmoothingType0Type0 | int | None | Unset, data)

        smoothing = _parse_smoothing(d.pop("smoothing", UNSET))

        dashboard_chart_spec = cls(
            chart_type=chart_type,
            overlays=overlays,
            smoothing=smoothing,
        )

        return dashboard_chart_spec
