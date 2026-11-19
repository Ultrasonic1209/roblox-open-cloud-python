from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_document import CustomDashboardDocument


T = TypeVar("T", bound="CustomDashboardsValidateDashboardDocumentJsonBody")


@_attrs_define
class CustomDashboardsValidateDashboardDocumentJsonBody:
    """
    Attributes:
        document (CustomDashboardDocument | None | Unset): CustomDashboardDocument is the dashboard authoring document
            persisted as the
            latest published content. Draft edits remain local client state until the
            caller sends this document to create or publish a dashboard.
    """

    document: CustomDashboardDocument | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415

        document: dict[str, Any] | None | Unset
        if isinstance(self.document, Unset):
            document = UNSET
        elif isinstance(self.document, CustomDashboardDocument):
            document = self.document.to_dict()
        else:
            document = self.document

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415

        d = dict(src_dict)

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

        custom_dashboards_validate_dashboard_document_json_body = cls(
            document=document,
        )

        return custom_dashboards_validate_dashboard_document_json_body
