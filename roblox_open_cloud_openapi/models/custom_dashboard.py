from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_document import CustomDashboardDocument
    from ..models.dashboard_document_version import DashboardDocumentVersion
    from ..models.dashboard_metadata import DashboardMetadata


T = TypeVar("T", bound="CustomDashboard")


@_attrs_define
class CustomDashboard:
    """CustomDashboard is the full dashboard response shape.

    Attributes:
        metadata (DashboardMetadata | None | Unset): DashboardMetadata is the metadata-only shape returned by list
            calls.
            It intentionally omits the document body so list views do not load dashboard payloads.
        document (CustomDashboardDocument | None | Unset): CustomDashboardDocument is the dashboard authoring document
            persisted as the
            latest published content. Draft edits remain local client state until the
            caller sends this document to create or publish a dashboard.
        version (DashboardDocumentVersion | None | Unset): DashboardDocumentVersion identifies the latest persisted
            content returned by the backend.
    """

    metadata: DashboardMetadata | None | Unset = UNSET
    document: CustomDashboardDocument | None | Unset = UNSET
    version: DashboardDocumentVersion | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415
        from ..models.dashboard_document_version import DashboardDocumentVersion  # noqa: PLC0415
        from ..models.dashboard_metadata import DashboardMetadata  # noqa: PLC0415

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DashboardMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        document: dict[str, Any] | None | Unset
        if isinstance(self.document, Unset):
            document = UNSET
        elif isinstance(self.document, CustomDashboardDocument):
            document = self.document.to_dict()
        else:
            document = self.document

        version: dict[str, Any] | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        elif isinstance(self.version, DashboardDocumentVersion):
            version = self.version.to_dict()
        else:
            version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if document is not UNSET:
            field_dict["document"] = document
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415
        from ..models.dashboard_document_version import DashboardDocumentVersion  # noqa: PLC0415
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

        def _parse_document(data: object) -> CustomDashboardDocument | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                document_type_0 = CustomDashboardDocument.from_dict(data)

                return document_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDashboardDocument | None | Unset, data)

        document = _parse_document(d.pop("document", UNSET))

        def _parse_version(data: object) -> DashboardDocumentVersion | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                version_type_0 = DashboardDocumentVersion.from_dict(data)

                return version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardDocumentVersion | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        custom_dashboard = cls(
            metadata=metadata,
            document=document,
            version=version,
        )

        return custom_dashboard
