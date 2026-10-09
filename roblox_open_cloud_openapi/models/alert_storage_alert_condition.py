from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_storage_condition_operator import AlertStorageConditionOperator
from ..models.alert_storage_evaluation_mode import AlertStorageEvaluationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertStorageAlertCondition")


@_attrs_define
class AlertStorageAlertCondition:
    """The threshold condition that determines when an alert fires.

    Attributes:
        operator (AlertStorageConditionOperator): Comparison operator used to evaluate whether a metric value breaches a
            threshold.

            Gt

            Gte

            Lt

            Lte
        threshold (float): Numeric threshold the metric value is compared against.
        evaluation_mode (AlertStorageEvaluationMode): Determines how the metric value is derived before being compared
            against the threshold.

            Absolute

            PeriodOverPeriod
        period_offset_multiplier (int | None | Unset): How many intervals back the comparison period is placed for
            `PeriodOverPeriod`
            evaluation. A value of `1` compares against the immediately preceding interval;
            a value of `7` with a `OneDay` interval compares against the same day last
            week. `null` for `Absolute` conditions.
    """

    operator: AlertStorageConditionOperator
    threshold: float
    evaluation_mode: AlertStorageEvaluationMode
    period_offset_multiplier: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        threshold = self.threshold

        evaluation_mode = self.evaluation_mode.value

        period_offset_multiplier: int | None | Unset
        if isinstance(self.period_offset_multiplier, Unset):
            period_offset_multiplier = UNSET
        else:
            period_offset_multiplier = self.period_offset_multiplier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operator": operator,
                "threshold": threshold,
                "evaluationMode": evaluation_mode,
            }
        )
        if period_offset_multiplier is not UNSET:
            field_dict["periodOffsetMultiplier"] = period_offset_multiplier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        operator = AlertStorageConditionOperator(d.pop("operator"))

        threshold = d.pop("threshold")

        evaluation_mode = AlertStorageEvaluationMode(d.pop("evaluationMode"))

        def _parse_period_offset_multiplier(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_offset_multiplier = _parse_period_offset_multiplier(d.pop("periodOffsetMultiplier", UNSET))

        alert_storage_alert_condition = cls(
            operator=operator,
            threshold=threshold,
            evaluation_mode=evaluation_mode,
            period_offset_multiplier=period_offset_multiplier,
        )

        return alert_storage_alert_condition
