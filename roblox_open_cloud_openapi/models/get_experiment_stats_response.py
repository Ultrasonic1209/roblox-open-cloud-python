from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_stats_operation import ExperimentStatsOperation


T = TypeVar("T", bound="GetExperimentStatsResponse")


@_attrs_define
class GetExperimentStatsResponse:
    """Response body for
    `GET /v1/experimentation/universes/{universeId}/experiments/{experimentId}/stats`.

        Attributes:
            operation (ExperimentStatsOperation | None | Unset): The async operation containing the experiment stats.
    """

    operation: ExperimentStatsOperation | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_stats_operation import ExperimentStatsOperation

        operation: dict[str, Any] | None | Unset
        if isinstance(self.operation, Unset):
            operation = UNSET
        elif isinstance(self.operation, ExperimentStatsOperation):
            operation = self.operation.to_dict()
        else:
            operation = self.operation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_stats_operation import ExperimentStatsOperation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_operation(data: object) -> ExperimentStatsOperation | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_1 = ExperimentStatsOperation.from_dict(data)

                return operation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentStatsOperation | None | Unset, data)

        operation = _parse_operation(d.pop("operation", UNSET))

        get_experiment_stats_response = cls(
            operation=operation,
        )

        return get_experiment_stats_response
