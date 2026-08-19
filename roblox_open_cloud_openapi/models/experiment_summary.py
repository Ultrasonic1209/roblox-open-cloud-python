from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_product_type import ExperimentProductType
from ..models.experiment_state import ExperimentState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentSummary")


@_attrs_define
class ExperimentSummary:
    """Summary view of an experiment returned by the list endpoint. Does not include the variant /
    configuration payload; clients should call Get for the full payload.

        Attributes:
            id (None | str | Unset): Experiment ID.
            name (None | str | Unset): Experiment display name.
            description (None | str | Unset): Experiment description.
            created_time (datetime.datetime | Unset): UTC time the experiment was created.
            last_updated_time (None | str | Unset): UTC time the experiment was last updated.
            started_time (None | str | Unset): UTC time the experiment was started, if running.
            stopped_time (None | str | Unset): UTC time the experiment was stopped, if completed/cancelled.
            state (ExperimentState | Unset): Lifecycle state of an experiment.

                EXPERIMENT_STATE_DRAFT

                EXPERIMENT_STATE_SCHEDULED

                EXPERIMENT_STATE_RUNNING

                EXPERIMENT_STATE_COMPLETED

                EXPERIMENT_STATE_CANCELLED

                EXPERIMENT_STATE_DELETED
            created_by (None | str | Unset): User ID of the creator of the experiment.
            experiment_config_key (None | str | Unset): Convenience field exposing the first config key referenced by the
                first variant
                (in-game-configs experiments only). Empty for matchmaking.
            scheduled_time (None | str | Unset): UTC time the experiment is scheduled to start, if scheduled.
            duration_seconds (int | Unset): Planned experiment duration in whole seconds.
            product_type (ExperimentProductType | Unset): Type of product the experiment is targeting.

                EXPERIMENT_PRODUCT_TYPE_IN_GAME_CONFIGS

                EXPERIMENT_PRODUCT_TYPE_MATCHMAKING
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    last_updated_time: None | str | Unset = UNSET
    started_time: None | str | Unset = UNSET
    stopped_time: None | str | Unset = UNSET
    state: ExperimentState | Unset = UNSET
    created_by: None | str | Unset = UNSET
    experiment_config_key: None | str | Unset = UNSET
    scheduled_time: None | str | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    product_type: ExperimentProductType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        experiment_config_key: None | str | Unset
        if isinstance(self.experiment_config_key, Unset):
            experiment_config_key = UNSET
        else:
            experiment_config_key = self.experiment_config_key

        scheduled_time: None | str | Unset
        if isinstance(self.scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = self.scheduled_time

        duration_seconds = self.duration_seconds

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

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
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if experiment_config_key is not UNSET:
            field_dict["experimentConfigKey"] = experiment_config_key
        if scheduled_time is not UNSET:
            field_dict["scheduledTime"] = scheduled_time
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if product_type is not UNSET:
            field_dict["productType"] = product_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_experiment_config_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experiment_config_key = _parse_experiment_config_key(d.pop("experimentConfigKey", UNSET))

        def _parse_scheduled_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_time = _parse_scheduled_time(d.pop("scheduledTime", UNSET))

        duration_seconds = d.pop("durationSeconds", UNSET)

        _product_type = d.pop("productType", UNSET)
        product_type: ExperimentProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = ExperimentProductType(_product_type)

        experiment_summary = cls(
            id=id,
            name=name,
            description=description,
            created_time=created_time,
            last_updated_time=last_updated_time,
            started_time=started_time,
            stopped_time=stopped_time,
            state=state,
            created_by=created_by,
            experiment_config_key=experiment_config_key,
            scheduled_time=scheduled_time,
            duration_seconds=duration_seconds,
            product_type=product_type,
        )

        return experiment_summary
