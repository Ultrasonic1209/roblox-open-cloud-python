from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_component import DashboardComponent
    from ..models.dashboard_flex_layout import DashboardFlexLayout
    from ..models.dashboard_responsive_grid_layout import DashboardResponsiveGridLayout
    from ..models.dashboard_stack_layout import DashboardStackLayout


T = TypeVar("T", bound="DashboardLayoutNode")


@_attrs_define
class DashboardLayoutNode:
    """DashboardLayoutNode is the normalized custom-dashboard layout AST.

    Attributes:
        component (DashboardComponent | None | Unset): A renderable dashboard component.
        stack (DashboardStackLayout | None | Unset): DashboardStackLayout is the vertical stack supported by Creator Hub
            custom dashboards.
        flex (DashboardFlexLayout | None | Unset): DashboardFlexLayout is the fixed row/wrap flex layout supported by
            Creator Hub custom dashboards.
        grid (DashboardResponsiveGridLayout | None | Unset): DashboardResponsiveGridLayout is the one-or-two-column grid
            supported by Creator Hub custom dashboards.
    """

    component: DashboardComponent | None | Unset = UNSET
    stack: DashboardStackLayout | None | Unset = UNSET
    flex: DashboardFlexLayout | None | Unset = UNSET
    grid: DashboardResponsiveGridLayout | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_component import DashboardComponent  # noqa: PLC0415
        from ..models.dashboard_flex_layout import DashboardFlexLayout  # noqa: PLC0415
        from ..models.dashboard_responsive_grid_layout import DashboardResponsiveGridLayout  # noqa: PLC0415
        from ..models.dashboard_stack_layout import DashboardStackLayout  # noqa: PLC0415

        component: dict[str, Any] | None | Unset
        if isinstance(self.component, Unset):
            component = UNSET
        elif isinstance(self.component, DashboardComponent):
            component = self.component.to_dict()
        else:
            component = self.component

        stack: dict[str, Any] | None | Unset
        if isinstance(self.stack, Unset):
            stack = UNSET
        elif isinstance(self.stack, DashboardStackLayout):
            stack = self.stack.to_dict()
        else:
            stack = self.stack

        flex: dict[str, Any] | None | Unset
        if isinstance(self.flex, Unset):
            flex = UNSET
        elif isinstance(self.flex, DashboardFlexLayout):
            flex = self.flex.to_dict()
        else:
            flex = self.flex

        grid: dict[str, Any] | None | Unset
        if isinstance(self.grid, Unset):
            grid = UNSET
        elif isinstance(self.grid, DashboardResponsiveGridLayout):
            grid = self.grid.to_dict()
        else:
            grid = self.grid

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if stack is not UNSET:
            field_dict["stack"] = stack
        if flex is not UNSET:
            field_dict["flex"] = flex
        if grid is not UNSET:
            field_dict["grid"] = grid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_component import DashboardComponent  # noqa: PLC0415
        from ..models.dashboard_flex_layout import DashboardFlexLayout  # noqa: PLC0415
        from ..models.dashboard_responsive_grid_layout import DashboardResponsiveGridLayout  # noqa: PLC0415
        from ..models.dashboard_stack_layout import DashboardStackLayout  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_component(data: object) -> DashboardComponent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_type_0 = DashboardComponent.from_dict(data)

                return component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardComponent | None | Unset, data)

        component = _parse_component(d.pop("component", UNSET))

        def _parse_stack(data: object) -> DashboardStackLayout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stack_type_0 = DashboardStackLayout.from_dict(data)

                return stack_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardStackLayout | None | Unset, data)

        stack = _parse_stack(d.pop("stack", UNSET))

        def _parse_flex(data: object) -> DashboardFlexLayout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                flex_type_0 = DashboardFlexLayout.from_dict(data)

                return flex_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardFlexLayout | None | Unset, data)

        flex = _parse_flex(d.pop("flex", UNSET))

        def _parse_grid(data: object) -> DashboardResponsiveGridLayout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grid_type_0 = DashboardResponsiveGridLayout.from_dict(data)

                return grid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardResponsiveGridLayout | None | Unset, data)

        grid = _parse_grid(d.pop("grid", UNSET))

        dashboard_layout_node = cls(
            component=component,
            stack=stack,
            flex=flex,
            grid=grid,
        )

        return dashboard_layout_node
