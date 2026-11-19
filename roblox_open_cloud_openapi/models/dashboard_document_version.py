from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardDocumentVersion")


@_attrs_define
class DashboardDocumentVersion:
    """DashboardDocumentVersion identifies the latest persisted content returned by the backend.

    Attributes:
        published_document_id (None | str | Unset):  Default: ''.
        published_version (None | str | Unset): Signed 64-bit integer encoded as a decimal string. Default: '0'.
        content_hash (None | str | Unset):  Default: ''.
    """

    published_document_id: None | str | Unset = ""
    published_version: None | str | Unset = "0"
    content_hash: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        published_document_id: None | str | Unset
        if isinstance(self.published_document_id, Unset):
            published_document_id = UNSET
        else:
            published_document_id = self.published_document_id

        published_version: None | str | Unset
        if isinstance(self.published_version, Unset):
            published_version = UNSET
        else:
            published_version = self.published_version

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if published_document_id is not UNSET:
            field_dict["publishedDocumentId"] = published_document_id
        if published_version is not UNSET:
            field_dict["publishedVersion"] = published_version
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_published_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_document_id = _parse_published_document_id(d.pop("publishedDocumentId", UNSET))

        def _parse_published_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_version = _parse_published_version(d.pop("publishedVersion", UNSET))

        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("contentHash", UNSET))

        dashboard_document_version = cls(
            published_document_id=published_document_id,
            published_version=published_version,
            content_hash=content_hash,
        )

        return dashboard_document_version
