from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pre_signed_upload_url import PreSignedUploadUrl


T = TypeVar("T", bound="MultipartUploadStartResponse")


@_attrs_define
class MultipartUploadStartResponse:
    """Response of Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadStartOperation

    Attributes:
        operation_path (None | str | Unset): ID of the operation.
        upload_urls (list[PreSignedUploadUrl] | None | Unset): A list of upload urls to upload chunks.
    """

    operation_path: None | str | Unset = UNSET
    upload_urls: list[PreSignedUploadUrl] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_path: None | str | Unset
        if isinstance(self.operation_path, Unset):
            operation_path = UNSET
        else:
            operation_path = self.operation_path

        upload_urls: list[dict[str, Any]] | None | Unset
        if isinstance(self.upload_urls, Unset):
            upload_urls = UNSET
        elif isinstance(self.upload_urls, list):
            upload_urls = []
            for upload_urls_type_0_item_data in self.upload_urls:
                upload_urls_type_0_item = upload_urls_type_0_item_data.to_dict()
                upload_urls.append(upload_urls_type_0_item)

        else:
            upload_urls = self.upload_urls

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation_path is not UNSET:
            field_dict["operationPath"] = operation_path
        if upload_urls is not UNSET:
            field_dict["uploadUrls"] = upload_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pre_signed_upload_url import PreSignedUploadUrl  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_operation_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_path = _parse_operation_path(d.pop("operationPath", UNSET))

        def _parse_upload_urls(data: object) -> list[PreSignedUploadUrl] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                upload_urls_type_0 = []
                _upload_urls_type_0 = data
                for upload_urls_type_0_item_data in _upload_urls_type_0:
                    upload_urls_type_0_item = PreSignedUploadUrl.from_dict(upload_urls_type_0_item_data)

                    upload_urls_type_0.append(upload_urls_type_0_item)

                return upload_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PreSignedUploadUrl] | None | Unset, data)

        upload_urls = _parse_upload_urls(d.pop("uploadUrls", UNSET))

        multipart_upload_start_response = cls(
            operation_path=operation_path,
            upload_urls=upload_urls,
        )

        return multipart_upload_start_response
