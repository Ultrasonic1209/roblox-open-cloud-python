from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_layout_node import DashboardLayoutNode
    from ..models.dashboard_page_metadata import DashboardPageMetadata
    from ..models.dashboard_surface import DashboardSurface


T = TypeVar("T", bound="DashboardBreakdownTabPage")


@_attrs_define
class DashboardBreakdownTabPage:
    """DashboardBreakdownTabPage renders tabs generated from breakdown values.

    Attributes:
        metadata (DashboardPageMetadata | None | Unset): DashboardPageMetadata carries localized metadata for a
            dashboard page.
        tab_breakdown_dimension_key (None | str | Unset):  Default: ''.
        tab_surface (DashboardSurface | None | Unset): DashboardSurface is a renderable analytics surface. It owns page-
            wide
            analytics context/controls as well as the layout nodes rendered inside that
            context.
        no_tab_empty_state (DashboardSurface | None | Unset): DashboardSurface is a renderable analytics surface. It
            owns page-wide
            analytics context/controls as well as the layout nodes rendered inside that
            context.
        pre_tab_nodes (list[DashboardLayoutNode] | None | Unset):
    """

    metadata: DashboardPageMetadata | None | Unset = UNSET
    tab_breakdown_dimension_key: None | str | Unset = ""
    tab_surface: DashboardSurface | None | Unset = UNSET
    no_tab_empty_state: DashboardSurface | None | Unset = UNSET
    pre_tab_nodes: list[DashboardLayoutNode] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DashboardPageMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        tab_breakdown_dimension_key: None | str | Unset
        if isinstance(self.tab_breakdown_dimension_key, Unset):
            tab_breakdown_dimension_key = UNSET
        else:
            tab_breakdown_dimension_key = self.tab_breakdown_dimension_key

        tab_surface: dict[str, Any] | None | Unset
        if isinstance(self.tab_surface, Unset):
            tab_surface = UNSET
        elif isinstance(self.tab_surface, DashboardSurface):
            tab_surface = self.tab_surface.to_dict()
        else:
            tab_surface = self.tab_surface

        no_tab_empty_state: dict[str, Any] | None | Unset
        if isinstance(self.no_tab_empty_state, Unset):
            no_tab_empty_state = UNSET
        elif isinstance(self.no_tab_empty_state, DashboardSurface):
            no_tab_empty_state = self.no_tab_empty_state.to_dict()
        else:
            no_tab_empty_state = self.no_tab_empty_state

        pre_tab_nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.pre_tab_nodes, Unset):
            pre_tab_nodes = UNSET
        elif isinstance(self.pre_tab_nodes, list):
            pre_tab_nodes = []
            for pre_tab_nodes_type_0_item_data in self.pre_tab_nodes:
                pre_tab_nodes_type_0_item = pre_tab_nodes_type_0_item_data.to_dict()
                pre_tab_nodes.append(pre_tab_nodes_type_0_item)

        else:
            pre_tab_nodes = self.pre_tab_nodes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tab_breakdown_dimension_key is not UNSET:
            field_dict["tabBreakdownDimensionKey"] = tab_breakdown_dimension_key
        if tab_surface is not UNSET:
            field_dict["tabSurface"] = tab_surface
        if no_tab_empty_state is not UNSET:
            field_dict["noTabEmptyState"] = no_tab_empty_state
        if pre_tab_nodes is not UNSET:
            field_dict["preTabNodes"] = pre_tab_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_layout_node import DashboardLayoutNode  # noqa: PLC0415
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

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

        def _parse_tab_breakdown_dimension_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tab_breakdown_dimension_key = _parse_tab_breakdown_dimension_key(d.pop("tabBreakdownDimensionKey", UNSET))

        def _parse_tab_surface(data: object) -> DashboardSurface | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tab_surface_type_0 = DashboardSurface.from_dict(data)

                return tab_surface_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSurface | None | Unset, data)

        tab_surface = _parse_tab_surface(d.pop("tabSurface", UNSET))

        def _parse_no_tab_empty_state(data: object) -> DashboardSurface | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                no_tab_empty_state_type_0 = DashboardSurface.from_dict(data)

                return no_tab_empty_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSurface | None | Unset, data)

        no_tab_empty_state = _parse_no_tab_empty_state(d.pop("noTabEmptyState", UNSET))

        def _parse_pre_tab_nodes(data: object) -> list[DashboardLayoutNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pre_tab_nodes_type_0 = []
                _pre_tab_nodes_type_0 = data
                for pre_tab_nodes_type_0_item_data in _pre_tab_nodes_type_0:
                    pre_tab_nodes_type_0_item = DashboardLayoutNode.from_dict(pre_tab_nodes_type_0_item_data)

                    pre_tab_nodes_type_0.append(pre_tab_nodes_type_0_item)

                return pre_tab_nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardLayoutNode] | None | Unset, data)

        pre_tab_nodes = _parse_pre_tab_nodes(d.pop("preTabNodes", UNSET))

        dashboard_breakdown_tab_page = cls(
            metadata=metadata,
            tab_breakdown_dimension_key=tab_breakdown_dimension_key,
            tab_surface=tab_surface,
            no_tab_empty_state=no_tab_empty_state,
            pre_tab_nodes=pre_tab_nodes,
        )

        return dashboard_breakdown_tab_page
