from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_tab import DashboardChartTab


T = TypeVar("T", bound="DashboardTabbedChart")


@_attrs_define
class DashboardTabbedChart:
    """DashboardTabbedChart renders chart tiles behind chart-specific tabs.

    Attributes:
        component_id (None | str | Unset):  Default: ''.
        title (None | str | Unset):  Default: ''.
        tabs (list[DashboardChartTab] | None | Unset):
    """

    component_id: None | str | Unset = ""
    title: None | str | Unset = ""
    tabs: list[DashboardChartTab] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        component_id: None | str | Unset
        if isinstance(self.component_id, Unset):
            component_id = UNSET
        else:
            component_id = self.component_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        tabs: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabs, Unset):
            tabs = UNSET
        elif isinstance(self.tabs, list):
            tabs = []
            for tabs_type_0_item_data in self.tabs:
                tabs_type_0_item = tabs_type_0_item_data.to_dict()
                tabs.append(tabs_type_0_item)

        else:
            tabs = self.tabs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if title is not UNSET:
            field_dict["title"] = title
        if tabs is not UNSET:
            field_dict["tabs"] = tabs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_chart_tab import DashboardChartTab  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_component_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component_id = _parse_component_id(d.pop("componentId", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_tabs(data: object) -> list[DashboardChartTab] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabs_type_0 = []
                _tabs_type_0 = data
                for tabs_type_0_item_data in _tabs_type_0:
                    tabs_type_0_item = DashboardChartTab.from_dict(tabs_type_0_item_data)

                    tabs_type_0.append(tabs_type_0_item)

                return tabs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardChartTab] | None | Unset, data)

        tabs = _parse_tabs(d.pop("tabs", UNSET))

        dashboard_tabbed_chart = cls(
            component_id=component_id,
            title=title,
            tabs=tabs,
        )

        return dashboard_tabbed_chart
