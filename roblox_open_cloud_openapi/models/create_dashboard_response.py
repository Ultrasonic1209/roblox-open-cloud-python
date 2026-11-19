from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard import CustomDashboard


T = TypeVar("T", bound="CreateDashboardResponse")


@_attrs_define
class CreateDashboardResponse:
    """
    Attributes:
        dashboard (CustomDashboard | None | Unset): CustomDashboard is the full dashboard response shape.
    """

    dashboard: CustomDashboard | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard import CustomDashboard  # noqa: PLC0415

        dashboard: dict[str, Any] | None | Unset
        if isinstance(self.dashboard, Unset):
            dashboard = UNSET
        elif isinstance(self.dashboard, CustomDashboard):
            dashboard = self.dashboard.to_dict()
        else:
            dashboard = self.dashboard

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard import CustomDashboard  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_dashboard(data: object) -> CustomDashboard | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dashboard_type_0 = CustomDashboard.from_dict(data)

                return dashboard_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDashboard | None | Unset, data)

        dashboard = _parse_dashboard(d.pop("dashboard", UNSET))

        create_dashboard_response = cls(
            dashboard=dashboard,
        )

        return create_dashboard_response
