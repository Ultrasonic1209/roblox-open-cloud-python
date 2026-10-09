from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsAlertControlPlaneModelsErrorResponse")


@_attrs_define
class AnalyticsAlertControlPlaneModelsErrorResponse:
    """Standard error response body for the Alerts API.

    Attributes:
        error_code (None | str | Unset): Machine-readable error code (e.g. PERMISSION_DENIED).
        message (None | str | Unset): Human-readable error description.
    """

    error_code: None | str | Unset = UNSET
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        analytics_alert_control_plane_models_error_response = cls(
            error_code=error_code,
            message=message,
        )

        return analytics_alert_control_plane_models_error_response
