from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.universe_experiment_metric import UniverseExperimentMetric
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.targeting_criteria import TargetingCriteria


T = TypeVar("T", bound="CalculateExperimentMdeData")


@_attrs_define
class CalculateExperimentMdeData:
    """Request body for
    `POST /v1/experimentation/universes/{universeId}/experiments:calculateMde`.

        Attributes:
            exposure_percent (int | Unset): Exposure percent in range 0-100. Percent of eligible users seeing the
                experiment.
            duration_seconds (int | Unset): Planned duration of the experiment in whole seconds.
                Values must be an exact multiple of `86400`.
            baseline_weight (float | Unset): Relative weight (in [0, 100]) for the baseline (control) variant.
            variant_weights (list[float] | None | Unset): Relative weights (each in [0, 100]) for each non-baseline variant.
            universe_goal_metric (UniverseExperimentMetric | Unset): Metric tracked for a universe experiment.

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_SESSION_TIME

                UNIVERSE_EXPERIMENT_METRIC_PLAYTIME_PER_USER

                UNIVERSE_EXPERIMENT_METRIC_DAY_1_RETENTION

                UNIVERSE_EXPERIMENT_METRIC_DAY_7_RETENTION

                UNIVERSE_EXPERIMENT_METRIC_PAYER_CONVERSION_RATE

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_USER

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_PAYING_USER
            targeting_criteria (None | TargetingCriteria | Unset): Targeting criteria used to scope the analytics window.
    """

    exposure_percent: int | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    baseline_weight: float | Unset = UNSET
    variant_weights: list[float] | None | Unset = UNSET
    universe_goal_metric: UniverseExperimentMetric | Unset = UNSET
    targeting_criteria: None | TargetingCriteria | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.targeting_criteria import TargetingCriteria

        exposure_percent = self.exposure_percent

        duration_seconds = self.duration_seconds

        baseline_weight = self.baseline_weight

        variant_weights: list[float] | None | Unset
        if isinstance(self.variant_weights, Unset):
            variant_weights = UNSET
        elif isinstance(self.variant_weights, list):
            variant_weights = self.variant_weights

        else:
            variant_weights = self.variant_weights

        universe_goal_metric: str | Unset = UNSET
        if not isinstance(self.universe_goal_metric, Unset):
            universe_goal_metric = self.universe_goal_metric.value

        targeting_criteria: dict[str, Any] | None | Unset
        if isinstance(self.targeting_criteria, Unset):
            targeting_criteria = UNSET
        elif isinstance(self.targeting_criteria, TargetingCriteria):
            targeting_criteria = self.targeting_criteria.to_dict()
        else:
            targeting_criteria = self.targeting_criteria

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if exposure_percent is not UNSET:
            field_dict["exposurePercent"] = exposure_percent
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if baseline_weight is not UNSET:
            field_dict["baselineWeight"] = baseline_weight
        if variant_weights is not UNSET:
            field_dict["variantWeights"] = variant_weights
        if universe_goal_metric is not UNSET:
            field_dict["universeGoalMetric"] = universe_goal_metric
        if targeting_criteria is not UNSET:
            field_dict["targetingCriteria"] = targeting_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.targeting_criteria import TargetingCriteria

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        exposure_percent = d.pop("exposurePercent", UNSET)

        duration_seconds = d.pop("durationSeconds", UNSET)

        baseline_weight = d.pop("baselineWeight", UNSET)

        def _parse_variant_weights(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variant_weights_type_0 = cast(list[float], data)

                return variant_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        variant_weights = _parse_variant_weights(d.pop("variantWeights", UNSET))

        _universe_goal_metric = d.pop("universeGoalMetric", UNSET)
        universe_goal_metric: UniverseExperimentMetric | Unset
        if isinstance(_universe_goal_metric, Unset):
            universe_goal_metric = UNSET
        else:
            universe_goal_metric = UniverseExperimentMetric(_universe_goal_metric)

        def _parse_targeting_criteria(data: object) -> None | TargetingCriteria | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                targeting_criteria_type_1 = TargetingCriteria.from_dict(data)

                return targeting_criteria_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TargetingCriteria | Unset, data)

        targeting_criteria = _parse_targeting_criteria(d.pop("targetingCriteria", UNSET))

        calculate_experiment_mde_data = cls(
            exposure_percent=exposure_percent,
            duration_seconds=duration_seconds,
            baseline_weight=baseline_weight,
            variant_weights=variant_weights,
            universe_goal_metric=universe_goal_metric,
            targeting_criteria=targeting_criteria,
        )

        return calculate_experiment_mde_data
