from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.open_cloud_error_of_custom_dashboard_error_details_reason_type_0_type_0 import (
    OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_conflict_details import CustomDashboardConflictDetails
    from ..models.custom_dashboard_validation_issue import CustomDashboardValidationIssue


T = TypeVar("T", bound="OpenCloudErrorOfCustomDashboardErrorDetails")


@_attrs_define
class OpenCloudErrorOfCustomDashboardErrorDetails:
    """CustomDashboardError is the structured error detail for API failures.

    Attributes:
        reason (int | None | OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0 | Unset):  Default:
            OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0.CUSTOM_DASHBOARD_ERROR_REASON_INVALID.
        dashboard_id (None | str | Unset):  Default: ''.
        message (None | str | Unset):  Default: ''.
        validation_issues (list[CustomDashboardValidationIssue] | None | Unset):
        conflict_details (CustomDashboardConflictDetails | None | Unset):
    """

    reason: int | None | OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0 | Unset = (
        OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0.CUSTOM_DASHBOARD_ERROR_REASON_INVALID
    )
    dashboard_id: None | str | Unset = ""
    message: None | str | Unset = ""
    validation_issues: list[CustomDashboardValidationIssue] | None | Unset = UNSET
    conflict_details: CustomDashboardConflictDetails | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_conflict_details import CustomDashboardConflictDetails  # noqa: PLC0415

        reason: int | None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0):
            reason = self.reason.value
        else:
            reason = self.reason

        dashboard_id: None | str | Unset
        if isinstance(self.dashboard_id, Unset):
            dashboard_id = UNSET
        else:
            dashboard_id = self.dashboard_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        validation_issues: list[dict[str, Any]] | None | Unset
        if isinstance(self.validation_issues, Unset):
            validation_issues = UNSET
        elif isinstance(self.validation_issues, list):
            validation_issues = []
            for validation_issues_type_0_item_data in self.validation_issues:
                validation_issues_type_0_item = validation_issues_type_0_item_data.to_dict()
                validation_issues.append(validation_issues_type_0_item)

        else:
            validation_issues = self.validation_issues

        conflict_details: dict[str, Any] | None | Unset
        if isinstance(self.conflict_details, Unset):
            conflict_details = UNSET
        elif isinstance(self.conflict_details, CustomDashboardConflictDetails):
            conflict_details = self.conflict_details.to_dict()
        else:
            conflict_details = self.conflict_details

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id
        if message is not UNSET:
            field_dict["message"] = message
        if validation_issues is not UNSET:
            field_dict["validationIssues"] = validation_issues
        if conflict_details is not UNSET:
            field_dict["conflictDetails"] = conflict_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_conflict_details import CustomDashboardConflictDetails  # noqa: PLC0415
        from ..models.custom_dashboard_validation_issue import CustomDashboardValidationIssue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_reason(
            data: object,
        ) -> int | None | OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_0_type_0 = OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0(data)

                return reason_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | None | OpenCloudErrorOfCustomDashboardErrorDetailsReasonType0Type0 | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_dashboard_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_id = _parse_dashboard_id(d.pop("dashboardId", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_validation_issues(data: object) -> list[CustomDashboardValidationIssue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                validation_issues_type_0 = []
                _validation_issues_type_0 = data
                for validation_issues_type_0_item_data in _validation_issues_type_0:
                    validation_issues_type_0_item = CustomDashboardValidationIssue.from_dict(
                        validation_issues_type_0_item_data
                    )

                    validation_issues_type_0.append(validation_issues_type_0_item)

                return validation_issues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomDashboardValidationIssue] | None | Unset, data)

        validation_issues = _parse_validation_issues(d.pop("validationIssues", UNSET))

        def _parse_conflict_details(data: object) -> CustomDashboardConflictDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conflict_details_type_0 = CustomDashboardConflictDetails.from_dict(data)

                return conflict_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDashboardConflictDetails | None | Unset, data)

        conflict_details = _parse_conflict_details(d.pop("conflictDetails", UNSET))

        open_cloud_error_of_custom_dashboard_error_details = cls(
            reason=reason,
            dashboard_id=dashboard_id,
            message=message,
            validation_issues=validation_issues,
            conflict_details=conflict_details,
        )

        return open_cloud_error_of_custom_dashboard_error_details
