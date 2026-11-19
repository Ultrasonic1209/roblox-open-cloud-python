from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_dimension_filter_and_breakdown_control import DashboardDimensionFilterAndBreakdownControl


T = TypeVar("T", bound="DashboardDimensionFilterAndBreakdownSubcontext")


@_attrs_define
class DashboardDimensionFilterAndBreakdownSubcontext:
    """DashboardDimensionFilterAndBreakdownSubcontext applies local dimension controls to a component.

    Attributes:
        controls (list[DashboardDimensionFilterAndBreakdownControl] | None | Unset):
    """

    controls: list[DashboardDimensionFilterAndBreakdownControl] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        controls: list[dict[str, Any]] | None | Unset
        if isinstance(self.controls, Unset):
            controls = UNSET
        elif isinstance(self.controls, list):
            controls = []
            for controls_type_0_item_data in self.controls:
                controls_type_0_item = controls_type_0_item_data.to_dict()
                controls.append(controls_type_0_item)

        else:
            controls = self.controls

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if controls is not UNSET:
            field_dict["controls"] = controls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_dimension_filter_and_breakdown_control import (
            DashboardDimensionFilterAndBreakdownControl,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_controls(data: object) -> list[DashboardDimensionFilterAndBreakdownControl] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                controls_type_0 = []
                _controls_type_0 = data
                for controls_type_0_item_data in _controls_type_0:
                    controls_type_0_item = DashboardDimensionFilterAndBreakdownControl.from_dict(
                        controls_type_0_item_data
                    )

                    controls_type_0.append(controls_type_0_item)

                return controls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardDimensionFilterAndBreakdownControl] | None | Unset, data)

        controls = _parse_controls(d.pop("controls", UNSET))

        dashboard_dimension_filter_and_breakdown_subcontext = cls(
            controls=controls,
        )

        return dashboard_dimension_filter_and_breakdown_subcontext
