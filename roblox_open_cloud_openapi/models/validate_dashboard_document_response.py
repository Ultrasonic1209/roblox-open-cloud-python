from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_validation_issue import CustomDashboardValidationIssue


T = TypeVar("T", bound="ValidateDashboardDocumentResponse")


@_attrs_define
class ValidateDashboardDocumentResponse:
    """
    Attributes:
        is_valid (bool | None | Unset):  Default: False.
        validation_issues (list[CustomDashboardValidationIssue] | None | Unset):
    """

    is_valid: bool | None | Unset = False
    validation_issues: list[CustomDashboardValidationIssue] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_valid: bool | None | Unset
        if isinstance(self.is_valid, Unset):
            is_valid = UNSET
        else:
            is_valid = self.is_valid

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if validation_issues is not UNSET:
            field_dict["validationIssues"] = validation_issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_validation_issue import CustomDashboardValidationIssue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_is_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_valid = _parse_is_valid(d.pop("isValid", UNSET))

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

        validate_dashboard_document_response = cls(
            is_valid=is_valid,
            validation_issues=validation_issues,
        )

        return validate_dashboard_document_response
