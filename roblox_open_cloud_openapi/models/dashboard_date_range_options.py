from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_date_range_default import DashboardDateRangeDefault


T = TypeVar("T", bound="DashboardDateRangeOptions")


@_attrs_define
class DashboardDateRangeOptions:
    """DashboardDateRangeOptions defines date range control behavior for a surface.

    Attributes:
        default_selection (DashboardDateRangeDefault | None | Unset): DashboardDateRangeDefault selects the initial date
            range for a surface.
    """

    default_selection: DashboardDateRangeDefault | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_date_range_default import DashboardDateRangeDefault  # noqa: PLC0415

        default_selection: dict[str, Any] | None | Unset
        if isinstance(self.default_selection, Unset):
            default_selection = UNSET
        elif isinstance(self.default_selection, DashboardDateRangeDefault):
            default_selection = self.default_selection.to_dict()
        else:
            default_selection = self.default_selection

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_selection is not UNSET:
            field_dict["defaultSelection"] = default_selection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_date_range_default import DashboardDateRangeDefault  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_default_selection(data: object) -> DashboardDateRangeDefault | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_selection_type_0 = DashboardDateRangeDefault.from_dict(data)

                return default_selection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardDateRangeDefault | None | Unset, data)

        default_selection = _parse_default_selection(d.pop("defaultSelection", UNSET))

        dashboard_date_range_options = cls(
            default_selection=default_selection,
        )

        return dashboard_date_range_options
