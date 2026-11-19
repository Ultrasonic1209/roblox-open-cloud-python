from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_fixed_granularity import DashboardFixedGranularity


T = TypeVar("T", bound="DashboardSurfaceGranularity")


@_attrs_define
class DashboardSurfaceGranularity:
    """DashboardSurfaceGranularity defines granularity behavior for a dashboard surface.

    Attributes:
        fixed (DashboardFixedGranularity | None | Unset): DashboardFixedGranularity fixes a surface to one granularity.
    """

    fixed: DashboardFixedGranularity | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_fixed_granularity import DashboardFixedGranularity  # noqa: PLC0415

        fixed: dict[str, Any] | None | Unset
        if isinstance(self.fixed, Unset):
            fixed = UNSET
        elif isinstance(self.fixed, DashboardFixedGranularity):
            fixed = self.fixed.to_dict()
        else:
            fixed = self.fixed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixed is not UNSET:
            field_dict["fixed"] = fixed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_fixed_granularity import DashboardFixedGranularity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_fixed(data: object) -> DashboardFixedGranularity | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fixed_type_0 = DashboardFixedGranularity.from_dict(data)

                return fixed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardFixedGranularity | None | Unset, data)

        fixed = _parse_fixed(d.pop("fixed", UNSET))

        dashboard_surface_granularity = cls(
            fixed=fixed,
        )

        return dashboard_surface_granularity
