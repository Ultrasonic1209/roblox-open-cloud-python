from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_tile import ChartTile
    from ..models.dashboard_controlled_subcontext import DashboardControlledSubcontext
    from ..models.dashboard_tabbed_chart import DashboardTabbedChart
    from ..models.dashboard_tabbed_table import DashboardTabbedTable
    from ..models.dashboard_table import DashboardTable
    from ..models.summary_card_tile import SummaryCardTile


T = TypeVar("T", bound="DashboardComponent")


@_attrs_define
class DashboardComponent:
    """DashboardComponent wraps each renderable dashboard body component.

    Attributes:
        chart (ChartTile | None | Unset): A chart component.
        tabbed_chart (DashboardTabbedChart | None | Unset): A tabbed chart; Creator Hub does not yet support authoring
            this component.
        table (DashboardTable | None | Unset): A table component. Creator Hub currently authors tables through ChartTile
            instead.
        tabbed_table (DashboardTabbedTable | None | Unset): A tabbed table; Creator Hub does not yet support authoring
            this component.
        summary_card (None | SummaryCardTile | Unset): A summary card component.
        controlled_subcontext (DashboardControlledSubcontext | None | Unset): Controls applied to a component.
    """

    chart: ChartTile | None | Unset = UNSET
    tabbed_chart: DashboardTabbedChart | None | Unset = UNSET
    table: DashboardTable | None | Unset = UNSET
    tabbed_table: DashboardTabbedTable | None | Unset = UNSET
    summary_card: None | SummaryCardTile | Unset = UNSET
    controlled_subcontext: DashboardControlledSubcontext | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415
        from ..models.dashboard_controlled_subcontext import DashboardControlledSubcontext  # noqa: PLC0415
        from ..models.dashboard_tabbed_chart import DashboardTabbedChart  # noqa: PLC0415
        from ..models.dashboard_tabbed_table import DashboardTabbedTable  # noqa: PLC0415
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415
        from ..models.summary_card_tile import SummaryCardTile  # noqa: PLC0415

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

        summary_card: dict[str, Any] | None | Unset
        if isinstance(self.summary_card, Unset):
            summary_card = UNSET
        elif isinstance(self.summary_card, SummaryCardTile):
            summary_card = self.summary_card.to_dict()
        else:
            summary_card = self.summary_card

        controlled_subcontext: dict[str, Any] | None | Unset
        if isinstance(self.controlled_subcontext, Unset):
            controlled_subcontext = UNSET
        elif isinstance(self.controlled_subcontext, DashboardControlledSubcontext):
            controlled_subcontext = self.controlled_subcontext.to_dict()
        else:
            controlled_subcontext = self.controlled_subcontext

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
        if summary_card is not UNSET:
            field_dict["summaryCard"] = summary_card
        if controlled_subcontext is not UNSET:
            field_dict["controlledSubcontext"] = controlled_subcontext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415
        from ..models.dashboard_controlled_subcontext import DashboardControlledSubcontext  # noqa: PLC0415
        from ..models.dashboard_tabbed_chart import DashboardTabbedChart  # noqa: PLC0415
        from ..models.dashboard_tabbed_table import DashboardTabbedTable  # noqa: PLC0415
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415
        from ..models.summary_card_tile import SummaryCardTile  # noqa: PLC0415

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

        def _parse_summary_card(data: object) -> None | SummaryCardTile | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                summary_card_type_0 = SummaryCardTile.from_dict(data)

                return summary_card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SummaryCardTile | Unset, data)

        summary_card = _parse_summary_card(d.pop("summaryCard", UNSET))

        def _parse_controlled_subcontext(data: object) -> DashboardControlledSubcontext | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                controlled_subcontext_type_0 = DashboardControlledSubcontext.from_dict(data)

                return controlled_subcontext_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardControlledSubcontext | None | Unset, data)

        controlled_subcontext = _parse_controlled_subcontext(d.pop("controlledSubcontext", UNSET))

        dashboard_component = cls(
            chart=chart,
            tabbed_chart=tabbed_chart,
            table=table,
            tabbed_table=tabbed_table,
            summary_card=summary_card,
            controlled_subcontext=controlled_subcontext,
        )

        return dashboard_component
