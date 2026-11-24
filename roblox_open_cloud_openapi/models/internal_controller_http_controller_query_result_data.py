from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_controller_http_controller_result_file import InternalControllerHttpControllerResultFile


T = TypeVar("T", bound="InternalControllerHttpControllerQueryResultData")


@_attrs_define
class InternalControllerHttpControllerQueryResultData:
    """
    Attributes:
        expires_at (str | Unset): ExpiresAt is when the result stops being downloadable at all, RFC 3339. Example:
            2026-02-01T00:00:00Z.
        files (list[InternalControllerHttpControllerResultFile] | Unset): Files are the result objects, one presigned
            URL each. All must be fetched to
            have the complete extract. Empty when the query matched no rows.
        format_ (str | Unset): Format is the encoding of every file. Example: csv.gz.
        job_id (str | Unset): JobID is the public id of the query job. Example: 3f6b1c2e-9d4a-4c1b-9f2e-2a1b3c4d5e6f.
        row_count (int | Unset): RowCount is the total across all files, so a client can verify it reassembled
            the complete extract. Example: 4200.
        state (str | Unset): State is the job's current lifecycle state. Example: SUCCEEDED.
        url_expires_at (str | Unset): URLExpiresAt is when these links stop working, RFC 3339; never later than
            ExpiresAt. Re-request this endpoint for fresh links until then. Example: 2026-01-31T01:00:00Z.
    """

    expires_at: str | Unset = UNSET
    files: list[InternalControllerHttpControllerResultFile] | Unset = UNSET
    format_: str | Unset = UNSET
    job_id: str | Unset = UNSET
    row_count: int | Unset = UNSET
    state: str | Unset = UNSET
    url_expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        format_ = self.format_

        job_id = self.job_id

        row_count = self.row_count

        state = self.state

        url_expires_at = self.url_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if files is not UNSET:
            field_dict["files"] = files
        if format_ is not UNSET:
            field_dict["format"] = format_
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if state is not UNSET:
            field_dict["state"] = state
        if url_expires_at is not UNSET:
            field_dict["url_expires_at"] = url_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_controller_http_controller_result_file import InternalControllerHttpControllerResultFile  # noqa: PLC0415

        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        _files = d.pop("files", UNSET)
        files: list[InternalControllerHttpControllerResultFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = InternalControllerHttpControllerResultFile.from_dict(files_item_data)

                files.append(files_item)

        format_ = d.pop("format", UNSET)

        job_id = d.pop("job_id", UNSET)

        row_count = d.pop("row_count", UNSET)

        state = d.pop("state", UNSET)

        url_expires_at = d.pop("url_expires_at", UNSET)

        internal_controller_http_controller_query_result_data = cls(
            expires_at=expires_at,
            files=files,
            format_=format_,
            job_id=job_id,
            row_count=row_count,
            state=state,
            url_expires_at=url_expires_at,
        )

        internal_controller_http_controller_query_result_data.additional_properties = d
        return internal_controller_http_controller_query_result_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
