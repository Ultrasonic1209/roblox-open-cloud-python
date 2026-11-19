from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_metadata import DashboardMetadata


T = TypeVar("T", bound="DeleteDashboardResponse")


@_attrs_define
class DeleteDashboardResponse:
    """
    Attributes:
        metadata (DashboardMetadata | None | Unset): DashboardMetadata is the metadata-only shape returned by list
            calls.
            It intentionally omits the document body so list views do not load dashboard payloads.
    """

    metadata: DashboardMetadata | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_metadata import DashboardMetadata  # noqa: PLC0415

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DashboardMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_metadata import DashboardMetadata  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_metadata(data: object) -> DashboardMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DashboardMetadata.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        delete_dashboard_response = cls(
            metadata=metadata,
        )

        return delete_dashboard_response
