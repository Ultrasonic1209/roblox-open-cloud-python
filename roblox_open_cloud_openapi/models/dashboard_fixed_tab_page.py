from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_fixed_tab import DashboardFixedTab
    from ..models.dashboard_page_metadata import DashboardPageMetadata


T = TypeVar("T", bound="DashboardFixedTabPage")


@_attrs_define
class DashboardFixedTabPage:
    """DashboardFixedTabPage renders a dashboard with a fixed set of tabs.

    Attributes:
        metadata (DashboardPageMetadata | None | Unset): DashboardPageMetadata carries localized metadata for a
            dashboard page.
        tabs (list[DashboardFixedTab] | None | Unset):
        tab_order (list[str] | None | Unset): Optional explicit ordering by `DashboardFixedTab.tab_key`. If omitted,
            adapters use the order of `tabs`.
    """

    metadata: DashboardPageMetadata | None | Unset = UNSET
    tabs: list[DashboardFixedTab] | None | Unset = UNSET
    tab_order: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DashboardPageMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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

        tab_order: list[str] | None | Unset
        if isinstance(self.tab_order, Unset):
            tab_order = UNSET
        elif isinstance(self.tab_order, list):
            tab_order = self.tab_order

        else:
            tab_order = self.tab_order

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tabs is not UNSET:
            field_dict["tabs"] = tabs
        if tab_order is not UNSET:
            field_dict["tabOrder"] = tab_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_fixed_tab import DashboardFixedTab  # noqa: PLC0415
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metadata(data: object) -> DashboardPageMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DashboardPageMetadata.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPageMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_tabs(data: object) -> list[DashboardFixedTab] | None | Unset:
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
                    tabs_type_0_item = DashboardFixedTab.from_dict(tabs_type_0_item_data)

                    tabs_type_0.append(tabs_type_0_item)

                return tabs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardFixedTab] | None | Unset, data)

        tabs = _parse_tabs(d.pop("tabs", UNSET))

        def _parse_tab_order(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tab_order_type_0 = cast(list[str], data)

                return tab_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tab_order = _parse_tab_order(d.pop("tabOrder", UNSET))

        dashboard_fixed_tab_page = cls(
            metadata=metadata,
            tabs=tabs,
            tab_order=tab_order,
        )

        return dashboard_fixed_tab_page
