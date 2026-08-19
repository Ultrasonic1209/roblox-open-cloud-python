from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.operational_status import OperationalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_api_error import ExperimentApiError
    from ..models.product_experiment import ProductExperiment


T = TypeVar("T", bound="ExperimentOperation")


@_attrs_define
class ExperimentOperation:
    """Async operation result for an experiment Create / Update / Discard call. When
    Done is true, at most one of Error or Experiment is set; when false, neither is. A successful delete is the
    one case where a done operation carries neither: the experiment no longer exists, so
    no Experiment body is returned.

        Attributes:
            operation_id (None | str | Unset): Stable operation ID.
            status (OperationalStatus | Unset): Current operational status reported on an experiment or an async operation
                performed on one.

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
            created_time (datetime.datetime | Unset): UTC time the operation was created.
            done (bool | Unset): True once the operation terminates (success or failure). When false, neither
                Error nor Experiment is populated.
            error (ExperimentApiError | None | Unset): Error outcome. Populated iff Done is true and the operation failed.
            experiment (None | ProductExperiment | Unset): Successful outcome. Populated iff Done is true and the operation
                succeeded and returned an experiment resource.
    """

    operation_id: None | str | Unset = UNSET
    status: OperationalStatus | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    done: bool | Unset = UNSET
    error: ExperimentApiError | None | Unset = UNSET
    experiment: None | ProductExperiment | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.product_experiment import ProductExperiment

        operation_id: None | str | Unset
        if isinstance(self.operation_id, Unset):
            operation_id = UNSET
        else:
            operation_id = self.operation_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        done = self.done

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ExperimentApiError):
            error = self.error.to_dict()
        else:
            error = self.error

        experiment: dict[str, Any] | None | Unset
        if isinstance(self.experiment, Unset):
            experiment = UNSET
        elif isinstance(self.experiment, ProductExperiment):
            experiment = self.experiment.to_dict()
        else:
            experiment = self.experiment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if experiment is not UNSET:
            field_dict["experiment"] = experiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.product_experiment import ProductExperiment

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_operation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_id = _parse_operation_id(d.pop("operationId", UNSET))

        _status = d.pop("status", UNSET)
        status: OperationalStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OperationalStatus(_status)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        done = d.pop("done", UNSET)

        def _parse_error(data: object) -> ExperimentApiError | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = ExperimentApiError.from_dict(data)

                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentApiError | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_experiment(data: object) -> None | ProductExperiment | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                experiment_type_1 = ProductExperiment.from_dict(data)

                return experiment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductExperiment | Unset, data)

        experiment = _parse_experiment(d.pop("experiment", UNSET))

        experiment_operation = cls(
            operation_id=operation_id,
            status=status,
            created_time=created_time,
            done=done,
            error=error,
            experiment=experiment,
        )

        return experiment_operation
