from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_previous_period_config import DashboardPreviousPeriodConfig


T = TypeVar("T", bound="ChartOverlays")


@_attrs_define
class ChartOverlays:
    """ChartOverlays toggles optional chart adornments (display only, not query inputs).

    Attributes:
        genre_benchmark (bool | None | Unset):  Default: False.
        similar_experience_benchmark (bool | None | Unset):  Default: False.
        top_experience_benchmark (bool | None | Unset):  Default: False.
        previous_period (bool | None | Unset): Legacy enablement bit. Writers that set previous_period_config must also
            set this field so older readers continue to render a default comparison. Default: False.
        quota (bool | None | Unset):  Default: False.
        previous_period_config (DashboardPreviousPeriodConfig | None | Unset): DashboardPreviousPeriodConfig stores an
            authored previous-period comparison.
            relative_offset and custom_start_time are optional independently so the
            contract can losslessly preserve Creator Hub editor state.
    """

    genre_benchmark: bool | None | Unset = False
    similar_experience_benchmark: bool | None | Unset = False
    top_experience_benchmark: bool | None | Unset = False
    previous_period: bool | None | Unset = False
    quota: bool | None | Unset = False
    previous_period_config: DashboardPreviousPeriodConfig | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_previous_period_config import DashboardPreviousPeriodConfig  # noqa: PLC0415

        genre_benchmark: bool | None | Unset
        if isinstance(self.genre_benchmark, Unset):
            genre_benchmark = UNSET
        else:
            genre_benchmark = self.genre_benchmark

        similar_experience_benchmark: bool | None | Unset
        if isinstance(self.similar_experience_benchmark, Unset):
            similar_experience_benchmark = UNSET
        else:
            similar_experience_benchmark = self.similar_experience_benchmark

        top_experience_benchmark: bool | None | Unset
        if isinstance(self.top_experience_benchmark, Unset):
            top_experience_benchmark = UNSET
        else:
            top_experience_benchmark = self.top_experience_benchmark

        previous_period: bool | None | Unset
        if isinstance(self.previous_period, Unset):
            previous_period = UNSET
        else:
            previous_period = self.previous_period

        quota: bool | None | Unset
        if isinstance(self.quota, Unset):
            quota = UNSET
        else:
            quota = self.quota

        previous_period_config: dict[str, Any] | None | Unset
        if isinstance(self.previous_period_config, Unset):
            previous_period_config = UNSET
        elif isinstance(self.previous_period_config, DashboardPreviousPeriodConfig):
            previous_period_config = self.previous_period_config.to_dict()
        else:
            previous_period_config = self.previous_period_config

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if genre_benchmark is not UNSET:
            field_dict["genreBenchmark"] = genre_benchmark
        if similar_experience_benchmark is not UNSET:
            field_dict["similarExperienceBenchmark"] = similar_experience_benchmark
        if top_experience_benchmark is not UNSET:
            field_dict["topExperienceBenchmark"] = top_experience_benchmark
        if previous_period is not UNSET:
            field_dict["previousPeriod"] = previous_period
        if quota is not UNSET:
            field_dict["quota"] = quota
        if previous_period_config is not UNSET:
            field_dict["previousPeriodConfig"] = previous_period_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_previous_period_config import DashboardPreviousPeriodConfig  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_genre_benchmark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        genre_benchmark = _parse_genre_benchmark(d.pop("genreBenchmark", UNSET))

        def _parse_similar_experience_benchmark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        similar_experience_benchmark = _parse_similar_experience_benchmark(d.pop("similarExperienceBenchmark", UNSET))

        def _parse_top_experience_benchmark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        top_experience_benchmark = _parse_top_experience_benchmark(d.pop("topExperienceBenchmark", UNSET))

        def _parse_previous_period(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        previous_period = _parse_previous_period(d.pop("previousPeriod", UNSET))

        def _parse_quota(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        quota = _parse_quota(d.pop("quota", UNSET))

        def _parse_previous_period_config(data: object) -> DashboardPreviousPeriodConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_period_config_type_0 = DashboardPreviousPeriodConfig.from_dict(data)

                return previous_period_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPreviousPeriodConfig | None | Unset, data)

        previous_period_config = _parse_previous_period_config(d.pop("previousPeriodConfig", UNSET))

        chart_overlays = cls(
            genre_benchmark=genre_benchmark,
            similar_experience_benchmark=similar_experience_benchmark,
            top_experience_benchmark=top_experience_benchmark,
            previous_period=previous_period,
            quota=quota,
            previous_period_config=previous_period_config,
        )

        return chart_overlays
