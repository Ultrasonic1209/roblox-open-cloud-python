from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.universe_experiment_metric import UniverseExperimentMetric
from ..types import UNSET, Unset

T = TypeVar("T", bound="UniverseMetricConfiguration")


@_attrs_define
class UniverseMetricConfiguration:
    """Metric configuration for an experiment.

    Attributes:
        goal_metric (UniverseExperimentMetric | Unset): Metric tracked for a universe experiment.

            UNIVERSE_EXPERIMENT_METRIC_AVERAGE_SESSION_TIME

            UNIVERSE_EXPERIMENT_METRIC_PLAYTIME_PER_USER

            UNIVERSE_EXPERIMENT_METRIC_DAY_1_RETENTION

            UNIVERSE_EXPERIMENT_METRIC_DAY_7_RETENTION

            UNIVERSE_EXPERIMENT_METRIC_PAYER_CONVERSION_RATE

            UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_USER

            UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_PAYING_USER
        learning_metrics (list[UniverseExperimentMetric] | None | Unset): Learning (observation-only) metrics.
    """

    goal_metric: UniverseExperimentMetric | Unset = UNSET
    learning_metrics: list[UniverseExperimentMetric] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        goal_metric: str | Unset = UNSET
        if not isinstance(self.goal_metric, Unset):
            goal_metric = self.goal_metric.value

        learning_metrics: list[str] | None | Unset
        if isinstance(self.learning_metrics, Unset):
            learning_metrics = UNSET
        elif isinstance(self.learning_metrics, list):
            learning_metrics = []
            for learning_metrics_type_0_item_data in self.learning_metrics:
                learning_metrics_type_0_item = learning_metrics_type_0_item_data.value
                learning_metrics.append(learning_metrics_type_0_item)

        else:
            learning_metrics = self.learning_metrics

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if goal_metric is not UNSET:
            field_dict["goalMetric"] = goal_metric
        if learning_metrics is not UNSET:
            field_dict["learningMetrics"] = learning_metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _goal_metric = d.pop("goalMetric", UNSET)
        goal_metric: UniverseExperimentMetric | Unset
        if isinstance(_goal_metric, Unset):
            goal_metric = UNSET
        else:
            goal_metric = UniverseExperimentMetric(_goal_metric)

        def _parse_learning_metrics(data: object) -> list[UniverseExperimentMetric] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                learning_metrics_type_0 = []
                _learning_metrics_type_0 = data
                for learning_metrics_type_0_item_data in _learning_metrics_type_0:
                    learning_metrics_type_0_item = UniverseExperimentMetric(learning_metrics_type_0_item_data)

                    learning_metrics_type_0.append(learning_metrics_type_0_item)

                return learning_metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UniverseExperimentMetric] | None | Unset, data)

        learning_metrics = _parse_learning_metrics(d.pop("learningMetrics", UNSET))

        universe_metric_configuration = cls(
            goal_metric=goal_metric,
            learning_metrics=learning_metrics,
        )

        return universe_metric_configuration
