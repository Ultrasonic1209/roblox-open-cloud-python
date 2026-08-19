from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.universe_experiment_metric import UniverseExperimentMetric
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_configuration import ExperimentConfiguration
    from ..models.targeting_criteria import TargetingCriteria


T = TypeVar("T", bound="UpdateExperimentData")


@_attrs_define
class UpdateExperimentData:
    """Request body for
    `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
    Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is modeled as a full replace
    of these fields.

        Attributes:
            name (None | str | Unset): Experiment display name.
            description (None | str | Unset): Experiment description.
            experiment_configuration (ExperimentConfiguration | None | Unset): Experiment configuration (variants + product-
                type-specific data).
            exposure_percent (int | Unset): Exposure percent in range 0-100.
            targeting_criteria (None | TargetingCriteria | Unset): Targeting criteria scoping which users are eligible for
                the experiment.
            duration_seconds (int | Unset): Experiment duration in whole seconds.
            universe_goal_metric (UniverseExperimentMetric | Unset): Metric tracked for a universe experiment.

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_SESSION_TIME

                UNIVERSE_EXPERIMENT_METRIC_PLAYTIME_PER_USER

                UNIVERSE_EXPERIMENT_METRIC_DAY_1_RETENTION

                UNIVERSE_EXPERIMENT_METRIC_DAY_7_RETENTION

                UNIVERSE_EXPERIMENT_METRIC_PAYER_CONVERSION_RATE

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_USER

                UNIVERSE_EXPERIMENT_METRIC_AVERAGE_REVENUE_PER_PAYING_USER
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    experiment_configuration: ExperimentConfiguration | None | Unset = UNSET
    exposure_percent: int | Unset = UNSET
    targeting_criteria: None | TargetingCriteria | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    universe_goal_metric: UniverseExperimentMetric | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_configuration import ExperimentConfiguration
        from ..models.targeting_criteria import TargetingCriteria

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        experiment_configuration: dict[str, Any] | None | Unset
        if isinstance(self.experiment_configuration, Unset):
            experiment_configuration = UNSET
        elif isinstance(self.experiment_configuration, ExperimentConfiguration):
            experiment_configuration = self.experiment_configuration.to_dict()
        else:
            experiment_configuration = self.experiment_configuration

        exposure_percent = self.exposure_percent

        targeting_criteria: dict[str, Any] | None | Unset
        if isinstance(self.targeting_criteria, Unset):
            targeting_criteria = UNSET
        elif isinstance(self.targeting_criteria, TargetingCriteria):
            targeting_criteria = self.targeting_criteria.to_dict()
        else:
            targeting_criteria = self.targeting_criteria

        duration_seconds = self.duration_seconds

        universe_goal_metric: str | Unset = UNSET
        if not isinstance(self.universe_goal_metric, Unset):
            universe_goal_metric = self.universe_goal_metric.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if experiment_configuration is not UNSET:
            field_dict["experimentConfiguration"] = experiment_configuration
        if exposure_percent is not UNSET:
            field_dict["exposurePercent"] = exposure_percent
        if targeting_criteria is not UNSET:
            field_dict["targetingCriteria"] = targeting_criteria
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if universe_goal_metric is not UNSET:
            field_dict["universeGoalMetric"] = universe_goal_metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_configuration import ExperimentConfiguration
        from ..models.targeting_criteria import TargetingCriteria

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_experiment_configuration(data: object) -> ExperimentConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                experiment_configuration_type_1 = ExperimentConfiguration.from_dict(data)

                return experiment_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentConfiguration | None | Unset, data)

        experiment_configuration = _parse_experiment_configuration(d.pop("experimentConfiguration", UNSET))

        exposure_percent = d.pop("exposurePercent", UNSET)

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

        duration_seconds = d.pop("durationSeconds", UNSET)

        _universe_goal_metric = d.pop("universeGoalMetric", UNSET)
        universe_goal_metric: UniverseExperimentMetric | Unset
        if isinstance(_universe_goal_metric, Unset):
            universe_goal_metric = UNSET
        else:
            universe_goal_metric = UniverseExperimentMetric(_universe_goal_metric)

        update_experiment_data = cls(
            name=name,
            description=description,
            experiment_configuration=experiment_configuration,
            exposure_percent=exposure_percent,
            targeting_criteria=targeting_criteria,
            duration_seconds=duration_seconds,
            universe_goal_metric=universe_goal_metric,
        )

        return update_experiment_data
