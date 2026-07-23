from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.upload_thumbnails_response_file_to_operation_id_dict import (
        UploadThumbnailsResponseFileToOperationIdDict,
    )


T = TypeVar("T", bound="UploadThumbnailsResponse")


@_attrs_define
class UploadThumbnailsResponse:
    """
    Attributes:
        file_to_operation_id_dict (UploadThumbnailsResponseFileToOperationIdDict):
    """

    file_to_operation_id_dict: UploadThumbnailsResponseFileToOperationIdDict

    def to_dict(self) -> dict[str, Any]:
        file_to_operation_id_dict = self.file_to_operation_id_dict.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fileToOperationIdDict": file_to_operation_id_dict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_thumbnails_response_file_to_operation_id_dict import (
            UploadThumbnailsResponseFileToOperationIdDict,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        file_to_operation_id_dict = UploadThumbnailsResponseFileToOperationIdDict.from_dict(
            d.pop("fileToOperationIdDict")
        )

        upload_thumbnails_response = cls(
            file_to_operation_id_dict=file_to_operation_id_dict,
        )

        return upload_thumbnails_response
