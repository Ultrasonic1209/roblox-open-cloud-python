from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_chart_data_spec import DashboardChartDataSpec
    from ..models.dashboard_chart_spec import DashboardChartSpec


T = TypeVar("T", bound="ChartTile")


@_attrs_define
class ChartTile:
    """ChartTile is a chart body tile.

    Attributes:
        tile_id (None | str | Unset):  Default: ''.
        title (None | str | Unset):  Default: ''.
        data_spec (DashboardChartDataSpec | None | Unset): DashboardChartDataSpec carries chart query inputs synthesized
            into RAQI requests.
        chart_spec (DashboardChartSpec | None | Unset): DashboardChartSpec carries chart renderer options (not
            query/data inputs).
    """

    tile_id: None | str | Unset = ""
    title: None | str | Unset = ""
    data_spec: DashboardChartDataSpec | None | Unset = UNSET
    chart_spec: DashboardChartSpec | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_chart_data_spec import DashboardChartDataSpec  # noqa: PLC0415
        from ..models.dashboard_chart_spec import DashboardChartSpec  # noqa: PLC0415

        tile_id: None | str | Unset
        if isinstance(self.tile_id, Unset):
            tile_id = UNSET
        else:
            tile_id = self.tile_id

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

        chart_spec: dict[str, Any] | None | Unset
        if isinstance(self.chart_spec, Unset):
            chart_spec = UNSET
        elif isinstance(self.chart_spec, DashboardChartSpec):
            chart_spec = self.chart_spec.to_dict()
        else:
            chart_spec = self.chart_spec

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tile_id is not UNSET:
            field_dict["tileId"] = tile_id
        if title is not UNSET:
            field_dict["title"] = title
        if data_spec is not UNSET:
            field_dict["dataSpec"] = data_spec
        if chart_spec is not UNSET:
            field_dict["chartSpec"] = chart_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_chart_data_spec import DashboardChartDataSpec  # noqa: PLC0415
        from ..models.dashboard_chart_spec import DashboardChartSpec  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tile_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tile_id = _parse_tile_id(d.pop("tileId", UNSET))

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

        def _parse_chart_spec(data: object) -> DashboardChartSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chart_spec_type_0 = DashboardChartSpec.from_dict(data)

                return chart_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardChartSpec | None | Unset, data)

        chart_spec = _parse_chart_spec(d.pop("chartSpec", UNSET))

        chart_tile = cls(
            tile_id=tile_id,
            title=title,
            data_spec=data_spec,
            chart_spec=chart_spec,
        )

        return chart_tile
