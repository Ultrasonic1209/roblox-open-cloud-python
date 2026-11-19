from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_data_spec import DashboardChartDataSpec


T = TypeVar("T", bound="DashboardTable")


@_attrs_define
class DashboardTable:
    """DashboardTable renders a table from dashboard chart data inputs.

    Attributes:
        component_id (None | str | Unset):  Default: ''.
        title (None | str | Unset):  Default: ''.
        data_spec (DashboardChartDataSpec | None | Unset): DashboardChartDataSpec carries chart query inputs synthesized
            into RAQI requests.
    """

    component_id: None | str | Unset = ""
    title: None | str | Unset = ""
    data_spec: DashboardChartDataSpec | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_chart_data_spec import DashboardChartDataSpec  # noqa: PLC0415

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

        data_spec: dict[str, Any] | None | Unset
        if isinstance(self.data_spec, Unset):
            data_spec = UNSET
        elif isinstance(self.data_spec, DashboardChartDataSpec):
            data_spec = self.data_spec.to_dict()
        else:
            data_spec = self.data_spec

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if title is not UNSET:
            field_dict["title"] = title
        if data_spec is not UNSET:
            field_dict["dataSpec"] = data_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_chart_data_spec import DashboardChartDataSpec  # noqa: PLC0415

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

        def _parse_data_spec(data: object) -> DashboardChartDataSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_spec_type_0 = DashboardChartDataSpec.from_dict(data)

                return data_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartDataSpec | None | Unset, data)

        data_spec = _parse_data_spec(d.pop("dataSpec", UNSET))

        dashboard_table = cls(
            component_id=component_id,
            title=title,
            data_spec=data_spec,
        )

        return dashboard_table
