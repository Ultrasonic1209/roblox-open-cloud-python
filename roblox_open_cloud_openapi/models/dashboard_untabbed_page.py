from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_page_metadata import DashboardPageMetadata
    from ..models.dashboard_surface import DashboardSurface


T = TypeVar("T", bound="DashboardUntabbedPage")


@_attrs_define
class DashboardUntabbedPage:
    """DashboardUntabbedPage renders a dashboard page without tabs.

    Attributes:
        metadata (DashboardPageMetadata | None | Unset): DashboardPageMetadata carries localized metadata for a
            dashboard page.
        surface (DashboardSurface | None | Unset): DashboardSurface is a renderable analytics surface. It owns page-wide
            analytics context/controls as well as the layout nodes rendered inside that
            context.
    """

    metadata: DashboardPageMetadata | None | Unset = UNSET
    surface: DashboardSurface | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DashboardPageMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        surface: dict[str, Any] | None | Unset
        if isinstance(self.surface, Unset):
            surface = UNSET
        elif isinstance(self.surface, DashboardSurface):
            surface = self.surface.to_dict()
        else:
            surface = self.surface

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if surface is not UNSET:
            field_dict["surface"] = surface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_page_metadata import DashboardPageMetadata  # noqa: PLC0415
        from ..models.dashboard_surface import DashboardSurface  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metadata(data: object) -> DashboardPageMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DashboardPageMetadata.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPageMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

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

        dashboard_untabbed_page = cls(
            metadata=metadata,
            surface=surface,
        )

        return dashboard_untabbed_page
