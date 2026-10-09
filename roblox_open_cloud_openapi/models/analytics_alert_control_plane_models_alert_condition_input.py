from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_condition_operator import AlertStorageConditionOperator
from ..models.alert_storage_evaluation_mode import AlertStorageEvaluationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsAlertConditionInput")


@_attrs_define
class AnalyticsAlertControlPlaneModelsAlertConditionInput:
    """The threshold condition for an alert. Specifies the comparison operator, threshold value,
    and how the metric value is derived before comparison.

    On create, `operator`, `threshold`, and `evaluationMode` are all required.
    On update (PATCH), the entire `condition` object is optional; when included, any
    sub-field can be omitted to keep its current value.

    `periodOffsetMultiplier` only applies when `evaluationMode` is
    `PeriodOverPeriod`. It is ignored for `Absolute` conditions.

        Attributes:
            operator (AlertStorageConditionOperator | Unset): Comparison operator used to evaluate whether a metric value
                breaches a threshold.

                Gt

                Gte

                Lt

                Lte
            threshold (float | None | Unset): Numeric threshold the metric value is compared against.
                Required on create; optional on update.
            evaluation_mode (AlertStorageEvaluationMode | Unset): Determines how the metric value is derived before being
                compared against the threshold.

                Absolute

                PeriodOverPeriod
            period_offset_multiplier (int | None | Unset): How many intervals back the comparison period is placed for
                `PeriodOverPeriod` evaluation. For example, a value of `1` (the default)
                compares the current interval against the immediately preceding interval.
                A value of `7` with a `OneDay` interval compares today against the same
                day last week. Only valid when `evaluationMode` is `PeriodOverPeriod`;
                omit or leave `null` for `Absolute` conditions.
    """

    operator: AlertStorageConditionOperator | Unset = UNSET
    threshold: float | None | Unset = UNSET
    evaluation_mode: AlertStorageEvaluationMode | Unset = UNSET
    period_offset_multiplier: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        threshold: float | None | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

        evaluation_mode: str | Unset = UNSET
        if not isinstance(self.evaluation_mode, Unset):
            evaluation_mode = self.evaluation_mode.value

        period_offset_multiplier: int | None | Unset
        if isinstance(self.period_offset_multiplier, Unset):
            period_offset_multiplier = UNSET
        else:
            period_offset_multiplier = self.period_offset_multiplier

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if evaluation_mode is not UNSET:
            field_dict["evaluationMode"] = evaluation_mode
        if period_offset_multiplier is not UNSET:
            field_dict["periodOffsetMultiplier"] = period_offset_multiplier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _operator = d.pop("operator", UNSET)
        operator: AlertStorageConditionOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = AlertStorageConditionOperator(_operator)

        def _parse_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        _evaluation_mode = d.pop("evaluationMode", UNSET)
        evaluation_mode: AlertStorageEvaluationMode | Unset
        if isinstance(_evaluation_mode, Unset):
            evaluation_mode = UNSET
        else:
            evaluation_mode = AlertStorageEvaluationMode(_evaluation_mode)

        def _parse_period_offset_multiplier(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_offset_multiplier = _parse_period_offset_multiplier(d.pop("periodOffsetMultiplier", UNSET))

        analytics_alert_control_plane_models_alert_condition_input = cls(
            operator=operator,
            threshold=threshold,
            evaluation_mode=evaluation_mode,
            period_offset_multiplier=period_offset_multiplier,
        )

        return analytics_alert_control_plane_models_alert_condition_input
