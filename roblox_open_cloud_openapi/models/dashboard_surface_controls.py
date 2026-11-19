from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_annotation_options import DashboardAnnotationOptions
    from ..models.dashboard_surface_granularity import DashboardSurfaceGranularity
    from ..models.dashboard_time_range_options import DashboardTimeRangeOptions
    from ..models.tile_filter import TileFilter


T = TypeVar("T", bound="DashboardSurfaceControls")


@_attrs_define
class DashboardSurfaceControls:
    """DashboardSurfaceControls defines the page-wide controls for a dashboard surface.

    Attributes:
        time_range_options (DashboardTimeRangeOptions | None | Unset): DashboardTimeRangeOptions defines the available
            time range behavior for a surface.
        filter_dimension_keys (list[str] | None | Unset):
        default_filters (list[TileFilter] | None | Unset):
        breakdown_dimension_keys (list[str] | None | Unset):
        default_breakdown_dimension_keys (list[str] | None | Unset):
        granularity (DashboardSurfaceGranularity | None | Unset): DashboardSurfaceGranularity defines granularity
            behavior for a dashboard surface.
        annotation_options (DashboardAnnotationOptions | None | Unset): DashboardAnnotationOptions defines annotation
            controls for a dashboard surface.
    """

    time_range_options: DashboardTimeRangeOptions | None | Unset = UNSET
    filter_dimension_keys: list[str] | None | Unset = UNSET
    default_filters: list[TileFilter] | None | Unset = UNSET
    breakdown_dimension_keys: list[str] | None | Unset = UNSET
    default_breakdown_dimension_keys: list[str] | None | Unset = UNSET
    granularity: DashboardSurfaceGranularity | None | Unset = UNSET
    annotation_options: DashboardAnnotationOptions | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_annotation_options import DashboardAnnotationOptions  # noqa: PLC0415
        from ..models.dashboard_surface_granularity import DashboardSurfaceGranularity  # noqa: PLC0415
        from ..models.dashboard_time_range_options import DashboardTimeRangeOptions  # noqa: PLC0415

        time_range_options: dict[str, Any] | None | Unset
        if isinstance(self.time_range_options, Unset):
            time_range_options = UNSET
        elif isinstance(self.time_range_options, DashboardTimeRangeOptions):
            time_range_options = self.time_range_options.to_dict()
        else:
            time_range_options = self.time_range_options

        filter_dimension_keys: list[str] | None | Unset
        if isinstance(self.filter_dimension_keys, Unset):
            filter_dimension_keys = UNSET
        elif isinstance(self.filter_dimension_keys, list):
            filter_dimension_keys = self.filter_dimension_keys

        else:
            filter_dimension_keys = self.filter_dimension_keys

        default_filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.default_filters, Unset):
            default_filters = UNSET
        elif isinstance(self.default_filters, list):
            default_filters = []
            for default_filters_type_0_item_data in self.default_filters:
                default_filters_type_0_item = default_filters_type_0_item_data.to_dict()
                default_filters.append(default_filters_type_0_item)

        else:
            default_filters = self.default_filters

        breakdown_dimension_keys: list[str] | None | Unset
        if isinstance(self.breakdown_dimension_keys, Unset):
            breakdown_dimension_keys = UNSET
        elif isinstance(self.breakdown_dimension_keys, list):
            breakdown_dimension_keys = self.breakdown_dimension_keys

        else:
            breakdown_dimension_keys = self.breakdown_dimension_keys

        default_breakdown_dimension_keys: list[str] | None | Unset
        if isinstance(self.default_breakdown_dimension_keys, Unset):
            default_breakdown_dimension_keys = UNSET
        elif isinstance(self.default_breakdown_dimension_keys, list):
            default_breakdown_dimension_keys = self.default_breakdown_dimension_keys

        else:
            default_breakdown_dimension_keys = self.default_breakdown_dimension_keys

        granularity: dict[str, Any] | None | Unset
        if isinstance(self.granularity, Unset):
            granularity = UNSET
        elif isinstance(self.granularity, DashboardSurfaceGranularity):
            granularity = self.granularity.to_dict()
        else:
            granularity = self.granularity

        annotation_options: dict[str, Any] | None | Unset
        if isinstance(self.annotation_options, Unset):
            annotation_options = UNSET
        elif isinstance(self.annotation_options, DashboardAnnotationOptions):
            annotation_options = self.annotation_options.to_dict()
        else:
            annotation_options = self.annotation_options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if time_range_options is not UNSET:
            field_dict["timeRangeOptions"] = time_range_options
        if filter_dimension_keys is not UNSET:
            field_dict["filterDimensionKeys"] = filter_dimension_keys
        if default_filters is not UNSET:
            field_dict["defaultFilters"] = default_filters
        if breakdown_dimension_keys is not UNSET:
            field_dict["breakdownDimensionKeys"] = breakdown_dimension_keys
        if default_breakdown_dimension_keys is not UNSET:
            field_dict["defaultBreakdownDimensionKeys"] = default_breakdown_dimension_keys
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if annotation_options is not UNSET:
            field_dict["annotationOptions"] = annotation_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_annotation_options import DashboardAnnotationOptions  # noqa: PLC0415
        from ..models.dashboard_surface_granularity import DashboardSurfaceGranularity  # noqa: PLC0415
        from ..models.dashboard_time_range_options import DashboardTimeRangeOptions  # noqa: PLC0415
        from ..models.tile_filter import TileFilter  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_time_range_options(data: object) -> DashboardTimeRangeOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_range_options_type_0 = DashboardTimeRangeOptions.from_dict(data)

                return time_range_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTimeRangeOptions | None | Unset, data)

        time_range_options = _parse_time_range_options(d.pop("timeRangeOptions", UNSET))

        def _parse_filter_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_dimension_keys_type_0 = cast(list[str], data)

                return filter_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        filter_dimension_keys = _parse_filter_dimension_keys(d.pop("filterDimensionKeys", UNSET))

        def _parse_default_filters(data: object) -> list[TileFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_filters_type_0 = []
                _default_filters_type_0 = data
                for default_filters_type_0_item_data in _default_filters_type_0:
                    default_filters_type_0_item = TileFilter.from_dict(default_filters_type_0_item_data)

                    default_filters_type_0.append(default_filters_type_0_item)

                return default_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TileFilter] | None | Unset, data)

        default_filters = _parse_default_filters(d.pop("defaultFilters", UNSET))

        def _parse_breakdown_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_dimension_keys_type_0 = cast(list[str], data)

                return breakdown_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        breakdown_dimension_keys = _parse_breakdown_dimension_keys(d.pop("breakdownDimensionKeys", UNSET))

        def _parse_default_breakdown_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_breakdown_dimension_keys_type_0 = cast(list[str], data)

                return default_breakdown_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        default_breakdown_dimension_keys = _parse_default_breakdown_dimension_keys(
            d.pop("defaultBreakdownDimensionKeys", UNSET)
        )

        def _parse_granularity(data: object) -> DashboardSurfaceGranularity | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                granularity_type_0 = DashboardSurfaceGranularity.from_dict(data)

                return granularity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSurfaceGranularity | None | Unset, data)

        granularity = _parse_granularity(d.pop("granularity", UNSET))

        def _parse_annotation_options(data: object) -> DashboardAnnotationOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annotation_options_type_0 = DashboardAnnotationOptions.from_dict(data)

                return annotation_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardAnnotationOptions | None | Unset, data)

        annotation_options = _parse_annotation_options(d.pop("annotationOptions", UNSET))

        dashboard_surface_controls = cls(
            time_range_options=time_range_options,
            filter_dimension_keys=filter_dimension_keys,
            default_filters=default_filters,
            breakdown_dimension_keys=breakdown_dimension_keys,
            default_breakdown_dimension_keys=default_breakdown_dimension_keys,
            granularity=granularity,
            annotation_options=annotation_options,
        )

        return dashboard_surface_controls
