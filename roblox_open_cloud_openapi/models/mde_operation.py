from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_api_error import ExperimentApiError
    from ..models.mde_result import MdeResult


T = TypeVar("T", bound="MdeOperation")


@_attrs_define
class MdeOperation:
    """Async operation result for a `:calculateMde` call. When Done is true
    exactly one of Error or Mde is set; when false, neither is.

        Attributes:
            operation_id (None | str | Unset): Stable operation ID.
            last_modified_time (None | str | Unset): UTC time the operation was last modified.
            done (bool | Unset): True once the calculation terminates (success or failure).
            error (ExperimentApiError | None | Unset): Error outcome, when Done is true and the calculation failed.
            mde (MdeResult | None | Unset): Successful outcome, when Done is true and a result is available.
    """

    operation_id: None | str | Unset = UNSET
    last_modified_time: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    error: ExperimentApiError | None | Unset = UNSET
    mde: MdeResult | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.mde_result import MdeResult

        operation_id: None | str | Unset
        if isinstance(self.operation_id, Unset):
            operation_id = UNSET
        else:
            operation_id = self.operation_id

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

        mde: dict[str, Any] | None | Unset
        if isinstance(self.mde, Unset):
            mde = UNSET
        elif isinstance(self.mde, MdeResult):
            mde = self.mde.to_dict()
        else:
            mde = self.mde

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if mde is not UNSET:
            field_dict["mde"] = mde

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_api_error import ExperimentApiError
        from ..models.mde_result import MdeResult

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_operation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_id = _parse_operation_id(d.pop("operationId", UNSET))

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

        def _parse_mde(data: object) -> MdeResult | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mde_type_1 = MdeResult.from_dict(data)

                return mde_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MdeResult | None | Unset, data)

        mde = _parse_mde(d.pop("mde", UNSET))

        mde_operation = cls(
            operation_id=operation_id,
            last_modified_time=last_modified_time,
            done=done,
            error=error,
            mde=mde,
        )

        return mde_operation
