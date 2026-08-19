from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_summary import ExperimentSummary


T = TypeVar("T", bound="ListExperimentsResponse")


@_attrs_define
class ListExperimentsResponse:
    """Response body for `GET /v1/experimentation/universes/{universeId}/experiments`.

    Attributes:
        experiments (list[ExperimentSummary] | None | Unset): The page of experiments matching the query.
        total (int | Unset): Total number of experiments for the universe matching the filters
                        (independent of pagination).
    """

    experiments: list[ExperimentSummary] | None | Unset = UNSET
    total: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        experiments: list[dict[str, Any]] | None | Unset
        if isinstance(self.experiments, Unset):
            experiments = UNSET
        elif isinstance(self.experiments, list):
            experiments = []
            for experiments_type_0_item_data in self.experiments:
                experiments_type_0_item = experiments_type_0_item_data.to_dict()
                experiments.append(experiments_type_0_item)

        else:
            experiments = self.experiments

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if experiments is not UNSET:
            field_dict["experiments"] = experiments
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_summary import ExperimentSummary

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_experiments(data: object) -> list[ExperimentSummary] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experiments_type_0 = []
                _experiments_type_0 = data
                for experiments_type_0_item_data in _experiments_type_0:
                    experiments_type_0_item = ExperimentSummary.from_dict(experiments_type_0_item_data)

                    experiments_type_0.append(experiments_type_0_item)

                return experiments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExperimentSummary] | None | Unset, data)

        experiments = _parse_experiments(d.pop("experiments", UNSET))

        total = d.pop("total", UNSET)

        list_experiments_response = cls(
            experiments=experiments,
            total=total,
        )

        return list_experiments_response
