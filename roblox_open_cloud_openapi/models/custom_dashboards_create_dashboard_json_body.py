from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_document import CustomDashboardDocument


T = TypeVar("T", bound="CustomDashboardsCreateDashboardJsonBody")


@_attrs_define
class CustomDashboardsCreateDashboardJsonBody:
    """
    Attributes:
        name (None | str | Unset):  Default: ''.
        description (None | str | Unset):  Default: ''.
        document (CustomDashboardDocument | None | Unset): CustomDashboardDocument is the dashboard authoring document
            persisted as the
            latest published content. Draft edits remain local client state until the
            caller sends this document to create or publish a dashboard.
        idempotency_key (None | str | Unset): Optional caller-supplied token that makes this create idempotent.
            Repeating a create with
            the same key, universe, and actor within the server's retention window returns the
            originally created dashboard instead of creating a second one. The key identifies the
            request, not the document: two creates with identical content but different keys still
            produce two dashboards. Omitting it preserves the non-idempotent behaviour exactly.

            A key stays bound while its server-side reservation exists, including after its dashboard
            is deleted. Reusing a key bound to a deleted dashboard, or one reserved at least seven days
            ago whose dashboard is missing, fails with FAILED_PRECONDITION and reason
            IDEMPOTENCY_KEY_CONSUMED. Missing dashboards can only be recovered during the first seven
            days after reservation; creating another dashboard requires a new key.

            An empty string is treated as omitted; a non-empty whitespace-only key is invalid. Length is
            capped by `DashboardLimits.max_idempotency_key_length`, which applies to new keys only. Default: ''.
    """

    name: None | str | Unset = ""
    description: None | str | Unset = ""
    document: CustomDashboardDocument | None | Unset = UNSET
    idempotency_key: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        document: dict[str, Any] | None | Unset
        if isinstance(self.document, Unset):
            document = UNSET
        elif isinstance(self.document, CustomDashboardDocument):
            document = self.document.to_dict()
        else:
            document = self.document

        idempotency_key: None | str | Unset
        if isinstance(self.idempotency_key, Unset):
            idempotency_key = UNSET
        else:
            idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if document is not UNSET:
            field_dict["document"] = document
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_document import CustomDashboardDocument  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_idempotency_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idempotency_key = _parse_idempotency_key(d.pop("idempotencyKey", UNSET))

        custom_dashboards_create_dashboard_json_body = cls(
            name=name,
            description=description,
            document=document,
            idempotency_key=idempotency_key,
        )

        return custom_dashboards_create_dashboard_json_body
