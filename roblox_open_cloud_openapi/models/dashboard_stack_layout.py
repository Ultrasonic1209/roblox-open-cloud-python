from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_layout_node import DashboardLayoutNode


T = TypeVar("T", bound="DashboardStackLayout")


@_attrs_define
class DashboardStackLayout:
    """DashboardStackLayout is the vertical stack supported by Creator Hub custom dashboards.

    Attributes:
        children (list[DashboardLayoutNode] | None | Unset):
    """

    children: list[DashboardLayoutNode] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_layout_node import DashboardLayoutNode  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_children(data: object) -> list[DashboardLayoutNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = DashboardLayoutNode.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardLayoutNode] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

        dashboard_stack_layout = cls(
            children=children,
        )

        return dashboard_stack_layout
