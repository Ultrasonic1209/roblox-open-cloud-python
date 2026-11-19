from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_computed_metric_source import DashboardComputedMetricSource


T = TypeVar("T", bound="DashboardComputedMetric")


@_attrs_define
class DashboardComputedMetric:
    """DashboardComputedMetric is an inline dashboard authoring definition. It has
    no standalone resource or persistence lifecycle.

        Attributes:
            sources (list[DashboardComputedMetricSource] | None | Unset):
            formula (None | str | Unset):  Default: ''.
            display_name (None | str | Unset):  Default: ''.
            l_7_smoothing (bool | None | Unset):  Default: False.
    """

    sources: list[DashboardComputedMetricSource] | None | Unset = UNSET
    formula: None | str | Unset = ""
    display_name: None | str | Unset = ""
    l_7_smoothing: bool | None | Unset = False

    def to_dict(self) -> dict[str, Any]:
        sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        formula: None | str | Unset
        if isinstance(self.formula, Unset):
            formula = UNSET
        else:
            formula = self.formula

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        l_7_smoothing: bool | None | Unset
        if isinstance(self.l_7_smoothing, Unset):
            l_7_smoothing = UNSET
        else:
            l_7_smoothing = self.l_7_smoothing

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources
        if formula is not UNSET:
            field_dict["formula"] = formula
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if l_7_smoothing is not UNSET:
            field_dict["l7Smoothing"] = l_7_smoothing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_computed_metric_source import DashboardComputedMetricSource  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_sources(data: object) -> list[DashboardComputedMetricSource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = DashboardComputedMetricSource.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardComputedMetricSource] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        def _parse_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formula = _parse_formula(d.pop("formula", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_l_7_smoothing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        l_7_smoothing = _parse_l_7_smoothing(d.pop("l7Smoothing", UNSET))

        dashboard_computed_metric = cls(
            sources=sources,
            formula=formula,
            display_name=display_name,
            l_7_smoothing=l_7_smoothing,
        )

        return dashboard_computed_metric
