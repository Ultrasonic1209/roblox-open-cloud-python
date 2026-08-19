from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_api_error_type import ExperimentApiErrorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_api_error_error_context_type_0 import ExperimentApiErrorErrorContextType0


T = TypeVar("T", bound="ExperimentApiError")


@_attrs_define
class ExperimentApiError:
    """Application-layer error emitted on a failed experiment operation.

    Attributes:
        error_type (ExperimentApiErrorType | Unset): Validation failures.

            EXPERIMENT_API_ERROR_TYPE_INVALID_VARIANT_CONFIGURATION

            EXPERIMENT_API_ERROR_TYPE_INVALID_VARIANT_LABEL

            EXPERIMENT_API_ERROR_TYPE_MUST_HAVE_EXACTLY_ONE_BASELINE_VARIANT

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_OVERLAPPING_RUNTIME

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_INVALID_SCORING_CONFIGURATIONS

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_UNEXPECTED_PRODUCT_TYPE

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_EMPTY_CONFIGURATION

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_EMPTY_VARIANT_METADATA

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_VARIANT_WEIGHT_MUST_BE_POSITIVE

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_VARIANT_WEIGHTS_UNBALANCED

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_PLACE_CONFIG_REQUIRES_SCORING_ID_OR_DEFAULT

            EXPERIMENT_API_ERROR_TYPE_CONFIGS_MISSING_VARIANT

            EXPERIMENT_API_ERROR_TYPE_CONFIGS_VARIANT_MISSING_KEY

            EXPERIMENT_API_ERROR_TYPE_CONFIGS_VARIANT_MISSING_VALUE

            EXPERIMENT_API_ERROR_TYPE_CONFIGS_KEY_ALREADY_IN_USE

            EXPERIMENT_API_ERROR_TYPE_SYSTEM_ERROR

            EXPERIMENT_API_ERROR_TYPE_EXPERIMENT_RESULTS_NOT_FOUND

            EXPERIMENT_API_ERROR_TYPE_INVALID_TARGETING_CRITERIA

            EXPERIMENT_API_ERROR_TYPE_TARGETING_NOT_ALLOWED

            EXPERIMENT_API_ERROR_TYPE_INVALID_DURATION

            EXPERIMENT_API_ERROR_TYPE_CONFIGS_VARIANT_CONFIG_NOT_FOUND

            EXPERIMENT_API_ERROR_TYPE_INVALID_EXPERIMENT_NAME

            EXPERIMENT_API_ERROR_TYPE_CONDITIONAL_CONFIG_REQUIRES_NULL_BASELINE

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_CONTROL_VARIANT_MUST_MATCH_CURRENT_CONFIGURATION

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_VARIANTS_MUST_COVER_SAME_PLACES

            EXPERIMENT_API_ERROR_TYPE_MATCHMAKING_VARIANT_HAS_DUPLICATE_PLACES
        error_code (None | str | Unset): Stable machine-readable error code.
        error_message (None | str | Unset): Human-readable description of the failure.
        error_context (ExperimentApiErrorErrorContextType0 | None | Unset): Optional structured context about the
            failure (field paths, offending values, etc.).
    """

    error_type: ExperimentApiErrorType | Unset = UNSET
    error_code: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    error_context: ExperimentApiErrorErrorContextType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_api_error_error_context_type_0 import ExperimentApiErrorErrorContextType0

        error_type: str | Unset = UNSET
        if not isinstance(self.error_type, Unset):
            error_type = self.error_type.value

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        error_context: dict[str, Any] | None | Unset
        if isinstance(self.error_context, Unset):
            error_context = UNSET
        elif isinstance(self.error_context, ExperimentApiErrorErrorContextType0):
            error_context = self.error_context.to_dict()
        else:
            error_context = self.error_context

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error_type is not UNSET:
            field_dict["errorType"] = error_type
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_context is not UNSET:
            field_dict["errorContext"] = error_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_api_error_error_context_type_0 import ExperimentApiErrorErrorContextType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _error_type = d.pop("errorType", UNSET)
        error_type: ExperimentApiErrorType | Unset
        if isinstance(_error_type, Unset):
            error_type = UNSET
        else:
            error_type = ExperimentApiErrorType(_error_type)

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_error_context(data: object) -> ExperimentApiErrorErrorContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_context_type_0 = ExperimentApiErrorErrorContextType0.from_dict(data)

                return error_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentApiErrorErrorContextType0 | None | Unset, data)

        error_context = _parse_error_context(d.pop("errorContext", UNSET))

        experiment_api_error = cls(
            error_type=error_type,
            error_code=error_code,
            error_message=error_message,
            error_context=error_context,
        )

        return experiment_api_error
