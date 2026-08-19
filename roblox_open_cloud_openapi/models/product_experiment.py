from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_state import ExperimentState
from ..models.operational_status import OperationalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_configuration import ExperimentConfiguration
    from ..models.targeting_criteria import TargetingCriteria
    from ..models.universe_metric_configuration import UniverseMetricConfiguration


T = TypeVar("T", bound="ProductExperiment")


@_attrs_define
class ProductExperiment:
    """Config-based experiment for a given product. Returned by the Get endpoint and embedded in
    a successful experiment operation.

        Attributes:
            id (None | str | Unset): Experiment ID.
            name (None | str | Unset): Experiment display name.
            description (None | str | Unset): Experiment description.
            created_time (datetime.datetime | Unset): UTC time the experiment was created.
            last_updated_time (None | str | Unset): UTC time the experiment was last updated.
            started_time (None | str | Unset): UTC time the experiment was started (running), if it has been.
            stopped_time (None | str | Unset): UTC time the experiment was stopped, if it has been.
            state (ExperimentState | Unset): Lifecycle state of an experiment.

                EXPERIMENT_STATE_DRAFT

                EXPERIMENT_STATE_SCHEDULED

                EXPERIMENT_STATE_RUNNING

                EXPERIMENT_STATE_COMPLETED

                EXPERIMENT_STATE_CANCELLED

                EXPERIMENT_STATE_DELETED
            experiment_configuration (ExperimentConfiguration | None | Unset): Experiment configuration (variants and
                product-type-specific data).
            exposure_percent (int | Unset): Exposure percent in range 0-100.
            targeting_criteria (None | TargetingCriteria | Unset): Targeting criteria scoping which users are eligible for
                the experiment.
            operational_status (OperationalStatus | Unset): Current operational status reported on an experiment or an async
                operation performed on one.

                OPERATIONAL_STATUS_READY

                OPERATIONAL_STATUS_CREATING

                OPERATIONAL_STATUS_UPDATING

                OPERATIONAL_STATUS_STARTING

                OPERATIONAL_STATUS_STOPPING

                OPERATIONAL_STATUS_SCHEDULING

                OPERATIONAL_STATUS_DELETING

                OPERATIONAL_STATUS_RAMPING_UP

                OPERATIONAL_STATUS_SYNCING

                OPERATIONAL_STATUS_ROLLING_OUT
            created_by (None | str | Unset): User ID of the creator of the experiment.
            scheduled_time (None | str | Unset): UTC time the experiment is scheduled to start, if scheduled.
            duration_seconds (int | Unset): Experiment duration in whole seconds.
            universe_metric_configuration (None | UniverseMetricConfiguration | Unset): Metric configuration (goal +
                learning metrics).
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    last_updated_time: None | str | Unset = UNSET
    started_time: None | str | Unset = UNSET
    stopped_time: None | str | Unset = UNSET
    state: ExperimentState | Unset = UNSET
    experiment_configuration: ExperimentConfiguration | None | Unset = UNSET
    exposure_percent: int | Unset = UNSET
    targeting_criteria: None | TargetingCriteria | Unset = UNSET
    operational_status: OperationalStatus | Unset = UNSET
    created_by: None | str | Unset = UNSET
    scheduled_time: None | str | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    universe_metric_configuration: None | UniverseMetricConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_configuration import ExperimentConfiguration
        from ..models.targeting_criteria import TargetingCriteria
        from ..models.universe_metric_configuration import UniverseMetricConfiguration

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        last_updated_time: None | str | Unset
        if isinstance(self.last_updated_time, Unset):
            last_updated_time = UNSET
        else:
            last_updated_time = self.last_updated_time

        started_time: None | str | Unset
        if isinstance(self.started_time, Unset):
            started_time = UNSET
        else:
            started_time = self.started_time

        stopped_time: None | str | Unset
        if isinstance(self.stopped_time, Unset):
            stopped_time = UNSET
        else:
            stopped_time = self.stopped_time

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

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

        operational_status: str | Unset = UNSET
        if not isinstance(self.operational_status, Unset):
            operational_status = self.operational_status.value

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        scheduled_time: None | str | Unset
        if isinstance(self.scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = self.scheduled_time

        duration_seconds = self.duration_seconds

        universe_metric_configuration: dict[str, Any] | None | Unset
        if isinstance(self.universe_metric_configuration, Unset):
            universe_metric_configuration = UNSET
        elif isinstance(self.universe_metric_configuration, UniverseMetricConfiguration):
            universe_metric_configuration = self.universe_metric_configuration.to_dict()
        else:
            universe_metric_configuration = self.universe_metric_configuration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if last_updated_time is not UNSET:
            field_dict["lastUpdatedTime"] = last_updated_time
        if started_time is not UNSET:
            field_dict["startedTime"] = started_time
        if stopped_time is not UNSET:
            field_dict["stoppedTime"] = stopped_time
        if state is not UNSET:
            field_dict["state"] = state
        if experiment_configuration is not UNSET:
            field_dict["experimentConfiguration"] = experiment_configuration
        if exposure_percent is not UNSET:
            field_dict["exposurePercent"] = exposure_percent
        if targeting_criteria is not UNSET:
            field_dict["targetingCriteria"] = targeting_criteria
        if operational_status is not UNSET:
            field_dict["operationalStatus"] = operational_status
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if scheduled_time is not UNSET:
            field_dict["scheduledTime"] = scheduled_time
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if universe_metric_configuration is not UNSET:
            field_dict["universeMetricConfiguration"] = universe_metric_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_configuration import ExperimentConfiguration
        from ..models.targeting_criteria import TargetingCriteria
        from ..models.universe_metric_configuration import UniverseMetricConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        def _parse_last_updated_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_updated_time = _parse_last_updated_time(d.pop("lastUpdatedTime", UNSET))

        def _parse_started_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_time = _parse_started_time(d.pop("startedTime", UNSET))

        def _parse_stopped_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stopped_time = _parse_stopped_time(d.pop("stoppedTime", UNSET))

        _state = d.pop("state", UNSET)
        state: ExperimentState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ExperimentState(_state)

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

        _operational_status = d.pop("operationalStatus", UNSET)
        operational_status: OperationalStatus | Unset
        if isinstance(_operational_status, Unset):
            operational_status = UNSET
        else:
            operational_status = OperationalStatus(_operational_status)

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_scheduled_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_time = _parse_scheduled_time(d.pop("scheduledTime", UNSET))

        duration_seconds = d.pop("durationSeconds", UNSET)

        def _parse_universe_metric_configuration(data: object) -> None | UniverseMetricConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                universe_metric_configuration_type_1 = UniverseMetricConfiguration.from_dict(data)

                return universe_metric_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UniverseMetricConfiguration | Unset, data)

        universe_metric_configuration = _parse_universe_metric_configuration(
            d.pop("universeMetricConfiguration", UNSET)
        )

        product_experiment = cls(
            id=id,
            name=name,
            description=description,
            created_time=created_time,
            last_updated_time=last_updated_time,
            started_time=started_time,
            stopped_time=stopped_time,
            state=state,
            experiment_configuration=experiment_configuration,
            exposure_percent=exposure_percent,
            targeting_criteria=targeting_criteria,
            operational_status=operational_status,
            created_by=created_by,
            scheduled_time=scheduled_time,
            duration_seconds=duration_seconds,
            universe_metric_configuration=universe_metric_configuration,
        )

        return product_experiment
