from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_surface import DashboardSurface


T = TypeVar("T", bound="DashboardFixedTab")


@_attrs_define
class DashboardFixedTab:
    """DashboardFixedTab defines one tab in a fixed-tab dashboard page.

    Attributes:
        tab_key (None | str | Unset):  Default: ''.
        label_key (None | str | Unset):  Default: ''.
        surface (DashboardSurface | None | Unset): DashboardSurface is a renderable analytics surface. It owns page-wide
            analytics context/controls as well as the layout nodes rendered inside that
            context.
    """

    tab_key: None | str | Unset = ""
    label_key: None | str | Unset = ""
    surface: DashboardSurface | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

        tab_key: None | str | Unset
        if isinstance(self.tab_key, Unset):
            tab_key = UNSET
        else:
            tab_key = self.tab_key

        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        surface: dict[str, Any] | None | Unset
        if isinstance(self.surface, Unset):
            surface = UNSET
        elif isinstance(self.surface, DashboardSurface):
            surface = self.surface.to_dict()
        else:
            surface = self.surface

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tab_key is not UNSET:
            field_dict["tabKey"] = tab_key
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if surface is not UNSET:
            field_dict["surface"] = surface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tab_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tab_key = _parse_tab_key(d.pop("tabKey", UNSET))

        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))

        def _parse_surface(data: object) -> DashboardSurface | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                surface_type_0 = DashboardSurface.from_dict(data)

                return surface_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSurface | None | Unset, data)

        surface = _parse_surface(d.pop("surface", UNSET))

        dashboard_fixed_tab = cls(
            tab_key=tab_key,
            label_key=label_key,
            surface=surface,
        )

        return dashboard_fixed_tab
