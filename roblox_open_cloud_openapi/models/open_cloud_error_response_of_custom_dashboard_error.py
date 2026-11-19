from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.open_cloud_error_of_custom_dashboard_error import OpenCloudErrorOfCustomDashboardError


T = TypeVar("T", bound="OpenCloudErrorResponseOfCustomDashboardError")


@_attrs_define
class OpenCloudErrorResponseOfCustomDashboardError:
    """
    Attributes:
        errors (list[OpenCloudErrorOfCustomDashboardError] | None):
    """

    errors: list[OpenCloudErrorOfCustomDashboardError] | None

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | None
        if isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_cloud_error_of_custom_dashboard_error import OpenCloudErrorOfCustomDashboardError  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_errors(data: object) -> list[OpenCloudErrorOfCustomDashboardError] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = OpenCloudErrorOfCustomDashboardError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OpenCloudErrorOfCustomDashboardError] | None, data)

        errors = _parse_errors(d.pop("errors"))

        open_cloud_error_response_of_custom_dashboard_error = cls(
            errors=errors,
        )

        return open_cloud_error_response_of_custom_dashboard_error
