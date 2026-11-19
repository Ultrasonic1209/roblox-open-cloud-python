from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_surface_resource_type_keys_type_0_item_type_0 import (
    DashboardSurfaceResourceTypeKeysType0ItemType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_layout_node import DashboardLayoutNode
    from ..models.dashboard_surface_controls import DashboardSurfaceControls


T = TypeVar("T", bound="DashboardSurface")


@_attrs_define
class DashboardSurface:
    """DashboardSurface is a renderable analytics surface. It owns page-wide
    analytics context/controls as well as the layout nodes rendered inside that
    context.

        Attributes:
            resource_type_keys (list[DashboardSurfaceResourceTypeKeysType0ItemType0 | int] | None | Unset):
            controls (DashboardSurfaceControls | None | Unset): DashboardSurfaceControls defines the page-wide controls for
                a dashboard surface.
            body_nodes (list[DashboardLayoutNode] | None | Unset): Main recursive layout tree.
    """

    resource_type_keys: list[DashboardSurfaceResourceTypeKeysType0ItemType0 | int] | None | Unset = UNSET
    controls: DashboardSurfaceControls | None | Unset = UNSET
    body_nodes: list[DashboardLayoutNode] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_surface_controls import DashboardSurfaceControls  # noqa: PLC0415

        resource_type_keys: list[int | str] | None | Unset
        if isinstance(self.resource_type_keys, Unset):
            resource_type_keys = UNSET
        elif isinstance(self.resource_type_keys, list):
            resource_type_keys = []
            for resource_type_keys_type_0_item_data in self.resource_type_keys:
                resource_type_keys_type_0_item: int | str
                if isinstance(resource_type_keys_type_0_item_data, DashboardSurfaceResourceTypeKeysType0ItemType0):
                    resource_type_keys_type_0_item = resource_type_keys_type_0_item_data.value
                else:
                    resource_type_keys_type_0_item = resource_type_keys_type_0_item_data
                resource_type_keys.append(resource_type_keys_type_0_item)

        else:
            resource_type_keys = self.resource_type_keys

        controls: dict[str, Any] | None | Unset
        if isinstance(self.controls, Unset):
            controls = UNSET
        elif isinstance(self.controls, DashboardSurfaceControls):
            controls = self.controls.to_dict()
        else:
            controls = self.controls

        body_nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.body_nodes, Unset):
            body_nodes = UNSET
        elif isinstance(self.body_nodes, list):
            body_nodes = []
            for body_nodes_type_0_item_data in self.body_nodes:
                body_nodes_type_0_item = body_nodes_type_0_item_data.to_dict()
                body_nodes.append(body_nodes_type_0_item)

        else:
            body_nodes = self.body_nodes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_type_keys is not UNSET:
            field_dict["resourceTypeKeys"] = resource_type_keys
        if controls is not UNSET:
            field_dict["controls"] = controls
        if body_nodes is not UNSET:
            field_dict["bodyNodes"] = body_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_layout_node import DashboardLayoutNode  # noqa: PLC0415
        from ..models.dashboard_surface_controls import DashboardSurfaceControls  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_resource_type_keys(
            data: object,
        ) -> list[DashboardSurfaceResourceTypeKeysType0ItemType0 | int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_type_keys_type_0 = []
                _resource_type_keys_type_0 = data
                for resource_type_keys_type_0_item_data in _resource_type_keys_type_0:

                    def _parse_resource_type_keys_type_0_item(
                        data: object,
                    ) -> DashboardSurfaceResourceTypeKeysType0ItemType0 | int:
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            resource_type_keys_type_0_item_type_0 = DashboardSurfaceResourceTypeKeysType0ItemType0(data)

                            return resource_type_keys_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(DashboardSurfaceResourceTypeKeysType0ItemType0 | int, data)

                    resource_type_keys_type_0_item = _parse_resource_type_keys_type_0_item(
                        resource_type_keys_type_0_item_data
                    )

                    resource_type_keys_type_0.append(resource_type_keys_type_0_item)

                return resource_type_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardSurfaceResourceTypeKeysType0ItemType0 | int] | None | Unset, data)

        resource_type_keys = _parse_resource_type_keys(d.pop("resourceTypeKeys", UNSET))

        def _parse_controls(data: object) -> DashboardSurfaceControls | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                controls_type_0 = DashboardSurfaceControls.from_dict(data)

                return controls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSurfaceControls | None | Unset, data)

        controls = _parse_controls(d.pop("controls", UNSET))

        def _parse_body_nodes(data: object) -> list[DashboardLayoutNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                body_nodes_type_0 = []
                _body_nodes_type_0 = data
                for body_nodes_type_0_item_data in _body_nodes_type_0:
                    body_nodes_type_0_item = DashboardLayoutNode.from_dict(body_nodes_type_0_item_data)

                    body_nodes_type_0.append(body_nodes_type_0_item)

                return body_nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardLayoutNode] | None | Unset, data)

        body_nodes = _parse_body_nodes(d.pop("bodyNodes", UNSET))

        dashboard_surface = cls(
            resource_type_keys=resource_type_keys,
            controls=controls,
            body_nodes=body_nodes,
        )

        return dashboard_surface
