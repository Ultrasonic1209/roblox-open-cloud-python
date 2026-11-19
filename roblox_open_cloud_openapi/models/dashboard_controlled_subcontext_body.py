from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_tile import ChartTile
    from ..models.dashboard_tabbed_chart import DashboardTabbedChart
    from ..models.dashboard_tabbed_table import DashboardTabbedTable
    from ..models.dashboard_table import DashboardTable


T = TypeVar("T", bound="DashboardControlledSubcontextBody")


@_attrs_define
class DashboardControlledSubcontextBody:
    """DashboardControlledSubcontextBody stores the chart or table controlled by a local subcontext.

    Attributes:
        chart (ChartTile | None | Unset): ChartTile is a chart body tile.
        tabbed_chart (DashboardTabbedChart | None | Unset): DashboardTabbedChart renders chart tiles behind chart-
            specific tabs.
        table (DashboardTable | None | Unset): DashboardTable renders a table from dashboard chart data inputs.
        tabbed_table (DashboardTabbedTable | None | Unset): DashboardTabbedTable renders table components behind table-
            specific tabs.
    """

    chart: ChartTile | None | Unset = UNSET
    tabbed_chart: DashboardTabbedChart | None | Unset = UNSET
    table: DashboardTable | None | Unset = UNSET
    tabbed_table: DashboardTabbedTable | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415
        from ..models.dashboard_tabbed_chart import DashboardTabbedChart  # noqa: PLC0415
        from ..models.dashboard_tabbed_table import DashboardTabbedTable  # noqa: PLC0415
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415

        chart: dict[str, Any] | None | Unset
        if isinstance(self.chart, Unset):
            chart = UNSET
        elif isinstance(self.chart, ChartTile):
            chart = self.chart.to_dict()
        else:
            chart = self.chart

        tabbed_chart: dict[str, Any] | None | Unset
        if isinstance(self.tabbed_chart, Unset):
            tabbed_chart = UNSET
        elif isinstance(self.tabbed_chart, DashboardTabbedChart):
            tabbed_chart = self.tabbed_chart.to_dict()
        else:
            tabbed_chart = self.tabbed_chart

        table: dict[str, Any] | None | Unset
        if isinstance(self.table, Unset):
            table = UNSET
        elif isinstance(self.table, DashboardTable):
            table = self.table.to_dict()
        else:
            table = self.table

        tabbed_table: dict[str, Any] | None | Unset
        if isinstance(self.tabbed_table, Unset):
            tabbed_table = UNSET
        elif isinstance(self.tabbed_table, DashboardTabbedTable):
            tabbed_table = self.tabbed_table.to_dict()
        else:
            tabbed_table = self.tabbed_table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if chart is not UNSET:
            field_dict["chart"] = chart
        if tabbed_chart is not UNSET:
            field_dict["tabbedChart"] = tabbed_chart
        if table is not UNSET:
            field_dict["table"] = table
        if tabbed_table is not UNSET:
            field_dict["tabbedTable"] = tabbed_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415
        from ..models.dashboard_tabbed_chart import DashboardTabbedChart  # noqa: PLC0415
        from ..models.dashboard_tabbed_table import DashboardTabbedTable  # noqa: PLC0415
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_chart(data: object) -> ChartTile | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chart_type_0 = ChartTile.from_dict(data)

                return chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChartTile | None | Unset, data)

        chart = _parse_chart(d.pop("chart", UNSET))

        def _parse_tabbed_chart(data: object) -> DashboardTabbedChart | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tabbed_chart_type_0 = DashboardTabbedChart.from_dict(data)

                return tabbed_chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTabbedChart | None | Unset, data)

        tabbed_chart = _parse_tabbed_chart(d.pop("tabbedChart", UNSET))

        def _parse_table(data: object) -> DashboardTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                table_type_0 = DashboardTable.from_dict(data)

                return table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTable | None | Unset, data)

        table = _parse_table(d.pop("table", UNSET))

        def _parse_tabbed_table(data: object) -> DashboardTabbedTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tabbed_table_type_0 = DashboardTabbedTable.from_dict(data)

                return tabbed_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTabbedTable | None | Unset, data)

        tabbed_table = _parse_tabbed_table(d.pop("tabbedTable", UNSET))

        dashboard_controlled_subcontext_body = cls(
            chart=chart,
            tabbed_chart=tabbed_chart,
            table=table,
            tabbed_table=tabbed_table,
        )

        return dashboard_controlled_subcontext_body
