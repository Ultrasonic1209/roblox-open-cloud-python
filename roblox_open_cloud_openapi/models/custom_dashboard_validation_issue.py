from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.custom_dashboard_validation_issue_reason_type_0_type_0 import (
    CustomDashboardValidationIssueReasonType0Type0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDashboardValidationIssue")


@_attrs_define
class CustomDashboardValidationIssue:
    """CustomDashboardValidationIssue identifies a document field/path and the failed rule.

    Attributes:
        field_path (None | str | Unset):  Default: ''.
        reason (CustomDashboardValidationIssueReasonType0Type0 | int | None | Unset):
            CustomDashboardValidationIssueReason categorizes a single validation failure. Default:
            CustomDashboardValidationIssueReasonType0Type0.CUSTOM_DASHBOARD_VALIDATION_ISSUE_REASON_INVALID.
        message (None | str | Unset):  Default: ''.
        rejected_values (list[str] | None | Unset):
    """

    field_path: None | str | Unset = ""
    reason: CustomDashboardValidationIssueReasonType0Type0 | int | None | Unset = (
        CustomDashboardValidationIssueReasonType0Type0.CUSTOM_DASHBOARD_VALIDATION_ISSUE_REASON_INVALID
    )
    message: None | str | Unset = ""
    rejected_values: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_path: None | str | Unset
        if isinstance(self.field_path, Unset):
            field_path = UNSET
        else:
            field_path = self.field_path

        reason: int | None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, CustomDashboardValidationIssueReasonType0Type0):
            reason = self.reason.value
        else:
            reason = self.reason

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        rejected_values: list[str] | None | Unset
        if isinstance(self.rejected_values, Unset):
            rejected_values = UNSET
        elif isinstance(self.rejected_values, list):
            rejected_values = self.rejected_values

        else:
            rejected_values = self.rejected_values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_path is not UNSET:
            field_dict["fieldPath"] = field_path
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if rejected_values is not UNSET:
            field_dict["rejectedValues"] = rejected_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_path = _parse_field_path(d.pop("fieldPath", UNSET))

        def _parse_reason(data: object) -> CustomDashboardValidationIssueReasonType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0_type_0 = CustomDashboardValidationIssueReasonType0Type0(data)

                return reason_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDashboardValidationIssueReasonType0Type0 | int | None | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_rejected_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rejected_values_type_0 = cast(list[str], data)

                return rejected_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        rejected_values = _parse_rejected_values(d.pop("rejectedValues", UNSET))

        custom_dashboard_validation_issue = cls(
            field_path=field_path,
            reason=reason,
            message=message,
            rejected_values=rejected_values,
        )

        return custom_dashboard_validation_issue
