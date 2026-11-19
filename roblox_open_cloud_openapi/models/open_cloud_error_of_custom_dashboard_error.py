from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_cloud_error_of_custom_dashboard_error_details import OpenCloudErrorOfCustomDashboardErrorDetails


T = TypeVar("T", bound="OpenCloudErrorOfCustomDashboardError")


@_attrs_define
class OpenCloudErrorOfCustomDashboardError:
    """
    Attributes:
        code (int):
        message (None | str):
        details (OpenCloudErrorOfCustomDashboardErrorDetails | Unset): CustomDashboardError is the structured error
            detail for API failures.
        reference_id (None | str | Unset):
    """

    code: int
    message: None | str
    details: OpenCloudErrorOfCustomDashboardErrorDetails | Unset = UNSET
    reference_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message: None | str
        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        reference_id: None | str | Unset
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        else:
            reference_id = self.reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_cloud_error_of_custom_dashboard_error_details import (
            OpenCloudErrorOfCustomDashboardErrorDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = d.pop("code")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        _details = d.pop("details", UNSET)
        details: OpenCloudErrorOfCustomDashboardErrorDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = OpenCloudErrorOfCustomDashboardErrorDetails.from_dict(_details)

        def _parse_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_id = _parse_reference_id(d.pop("referenceId", UNSET))

        open_cloud_error_of_custom_dashboard_error = cls(
            code=code,
            message=message,
            details=details,
            reference_id=reference_id,
        )

        open_cloud_error_of_custom_dashboard_error.additional_properties = d
        return open_cloud_error_of_custom_dashboard_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
