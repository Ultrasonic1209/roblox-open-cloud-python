from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_document import CustomDashboardDocument
    from ..models.dashboard_metadata_patch import DashboardMetadataPatch


T = TypeVar("T", bound="CustomDashboardsPublishDashboardJsonBody")


@_attrs_define
class CustomDashboardsPublishDashboardJsonBody:
    """
    Attributes:
        expected_head_etag (None | str | Unset):  Default: ''.
        document (CustomDashboardDocument | None | Unset): CustomDashboardDocument is the dashboard authoring document
            persisted as the
            latest published content. Draft edits remain local client state until the
            caller sends this document to create or publish a dashboard.
        metadata_patch (DashboardMetadataPatch | None | Unset): DashboardMetadataPatch updates dashboard metadata
            without exposing storage rows.
    """

    expected_head_etag: None | str | Unset = ""
    document: CustomDashboardDocument | None | Unset = UNSET
    metadata_patch: DashboardMetadataPatch | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415
        from ..models.dashboard_metadata_patch import DashboardMetadataPatch  # noqa: PLC0415

        expected_head_etag: None | str | Unset
        if isinstance(self.expected_head_etag, Unset):
            expected_head_etag = UNSET
        else:
            expected_head_etag = self.expected_head_etag

        document: dict[str, Any] | None | Unset
        if isinstance(self.document, Unset):
            document = UNSET
        elif isinstance(self.document, CustomDashboardDocument):
            document = self.document.to_dict()
        else:
            document = self.document

        metadata_patch: dict[str, Any] | None | Unset
        if isinstance(self.metadata_patch, Unset):
            metadata_patch = UNSET
        elif isinstance(self.metadata_patch, DashboardMetadataPatch):
            metadata_patch = self.metadata_patch.to_dict()
        else:
            metadata_patch = self.metadata_patch

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expected_head_etag is not UNSET:
            field_dict["expectedHeadEtag"] = expected_head_etag
        if document is not UNSET:
            field_dict["document"] = document
        if metadata_patch is not UNSET:
            field_dict["metadataPatch"] = metadata_patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415
        from ..models.dashboard_metadata_patch import DashboardMetadataPatch  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_expected_head_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_head_etag = _parse_expected_head_etag(d.pop("expectedHeadEtag", UNSET))

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

        def _parse_metadata_patch(data: object) -> DashboardMetadataPatch | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_patch_type_0 = DashboardMetadataPatch.from_dict(data)

                return metadata_patch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardMetadataPatch | None | Unset, data)

        metadata_patch = _parse_metadata_patch(d.pop("metadataPatch", UNSET))

        custom_dashboards_publish_dashboard_json_body = cls(
            expected_head_etag=expected_head_etag,
            document=document,
            metadata_patch=metadata_patch,
        )

        return custom_dashboards_publish_dashboard_json_body
