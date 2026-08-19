from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_experiment import ProductExperiment


T = TypeVar("T", bound="GetExperimentResponse")


@_attrs_define
class GetExperimentResponse:
    """Response body for GET /v1/universes/{universeId}/experiment/{experimentId}.

    Attributes:
        experiment (None | ProductExperiment | Unset): The requested experiment.
    """

    experiment: None | ProductExperiment | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_experiment import ProductExperiment

        experiment: dict[str, Any] | None | Unset
        if isinstance(self.experiment, Unset):
            experiment = UNSET
        elif isinstance(self.experiment, ProductExperiment):
            experiment = self.experiment.to_dict()
        else:
            experiment = self.experiment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if experiment is not UNSET:
            field_dict["experiment"] = experiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_experiment import ProductExperiment

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

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

        get_experiment_response = cls(
            experiment=experiment,
        )

        return get_experiment_response
