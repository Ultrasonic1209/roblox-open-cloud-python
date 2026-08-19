from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mde_operation import MdeOperation


T = TypeVar("T", bound="CalculateExperimentMdeResponse")


@_attrs_define
class CalculateExperimentMdeResponse:
    """Response body for
    `POST /v1/experimentation/universes/{universeId}/experiments:calculateMde`.

        Attributes:
            operation (MdeOperation | None | Unset): The MDE async operation.
    """

    operation: MdeOperation | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.mde_operation import MdeOperation

        operation: dict[str, Any] | None | Unset
        if isinstance(self.operation, Unset):
            operation = UNSET
        elif isinstance(self.operation, MdeOperation):
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
        from ..models.mde_operation import MdeOperation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_operation(data: object) -> MdeOperation | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_type_1 = MdeOperation.from_dict(data)

                return operation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MdeOperation | None | Unset, data)

        operation = _parse_operation(d.pop("operation", UNSET))

        calculate_experiment_mde_response = cls(
            operation=operation,
        )

        return calculate_experiment_mde_response
