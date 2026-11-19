from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chart_tile import ChartTile


T = TypeVar("T", bound="DashboardChartTab")


@_attrs_define
class DashboardChartTab:
    """DashboardChartTab defines one chart tab and its chart tile.

    Attributes:
        tab_key (None | str | Unset):  Default: ''.
        label_key (None | str | Unset):  Default: ''.
        chart (ChartTile | None | Unset): ChartTile is a chart body tile.
    """

    tab_key: None | str | Unset = ""
    label_key: None | str | Unset = ""
    chart: ChartTile | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415

        tab_key: None | str | Unset
        if isinstance(self.tab_key, Unset):
            tab_key = UNSET
        else:
            tab_key = self.tab_key

        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        chart: dict[str, Any] | None | Unset
        if isinstance(self.chart, Unset):
            chart = UNSET
        elif isinstance(self.chart, ChartTile):
            chart = self.chart.to_dict()
        else:
            chart = self.chart

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tab_key is not UNSET:
            field_dict["tabKey"] = tab_key
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if chart is not UNSET:
            field_dict["chart"] = chart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_tile import ChartTile  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tab_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tab_key = _parse_tab_key(d.pop("tabKey", UNSET))

        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))

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

        dashboard_chart_tab = cls(
            tab_key=tab_key,
            label_key=label_key,
            chart=chart,
        )

        return dashboard_chart_tab
