from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_api_error import ExperimentApiError
    from ..models.experiment_stats import ExperimentStats


T = TypeVar("T", bound="ExperimentStatsOperation")


@_attrs_define
class ExperimentStatsOperation:
    """Async operation for fetching experiment stats. When Done is true exactly
    one of Error or ExperimentStats is set; when false, neither is.

        Attributes:
            experiment_id (int | Unset): Experiment ID the stats are for.
            last_modified_time (None | str | Unset): UTC time the operation was last modified.
            done (bool | Unset): True once the stats fetch terminates (success or failure).
            error (ExperimentApiError | None | Unset): Error outcome, when Done is true and the fetch failed.
            experiment_stats (ExperimentStats | None | Unset): Successful outcome, when Done is true and stats are
                available.
    """

    experiment_id: int | Unset = UNSET
    last_modified_time: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    error: ExperimentApiError | None | Unset = UNSET
    experiment_stats: ExperimentStats | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.experiment_stats import ExperimentStats

        experiment_id = self.experiment_id

        last_modified_time: None | str | Unset
        if isinstance(self.last_modified_time, Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = self.last_modified_time

        done = self.done

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ExperimentApiError):
            error = self.error.to_dict()
        else:
            error = self.error

        experiment_stats: dict[str, Any] | None | Unset
        if isinstance(self.experiment_stats, Unset):
            experiment_stats = UNSET
        elif isinstance(self.experiment_stats, ExperimentStats):
            experiment_stats = self.experiment_stats.to_dict()
        else:
            experiment_stats = self.experiment_stats

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if experiment_id is not UNSET:
            field_dict["experimentId"] = experiment_id
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if experiment_stats is not UNSET:
            field_dict["experimentStats"] = experiment_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.experiment_stats import ExperimentStats

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        experiment_id = d.pop("experimentId", UNSET)

        def _parse_last_modified_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_modified_time = _parse_last_modified_time(d.pop("lastModifiedTime", UNSET))

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

        def _parse_experiment_stats(data: object) -> ExperimentStats | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                experiment_stats_type_1 = ExperimentStats.from_dict(data)

                return experiment_stats_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentStats | None | Unset, data)

        experiment_stats = _parse_experiment_stats(d.pop("experimentStats", UNSET))

        experiment_stats_operation = cls(
            experiment_id=experiment_id,
            last_modified_time=last_modified_time,
            done=done,
            error=error,
            experiment_stats=experiment_stats,
        )

        return experiment_stats_operation
