from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.upload_status import UploadStatus

if TYPE_CHECKING:
    from ..models.upload_thumbnails_status_response_upload_thumbnail_status_dict import (
        UploadThumbnailsStatusResponseUploadThumbnailStatusDict,
    )


T = TypeVar("T", bound="UploadThumbnailsStatusResponse")


@_attrs_define
class UploadThumbnailsStatusResponse:
    """
    Attributes:
        upload_status (UploadStatus):
        upload_thumbnail_status_dict (UploadThumbnailsStatusResponseUploadThumbnailStatusDict):
    """

    upload_status: UploadStatus
    upload_thumbnail_status_dict: UploadThumbnailsStatusResponseUploadThumbnailStatusDict

    def to_dict(self) -> dict[str, Any]:
        upload_status = self.upload_status.value

        upload_thumbnail_status_dict = self.upload_thumbnail_status_dict.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uploadStatus": upload_status,
                "uploadThumbnailStatusDict": upload_thumbnail_status_dict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_thumbnails_status_response_upload_thumbnail_status_dict import (
            UploadThumbnailsStatusResponseUploadThumbnailStatusDict,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        upload_status = UploadStatus(d.pop("uploadStatus"))

        upload_thumbnail_status_dict = UploadThumbnailsStatusResponseUploadThumbnailStatusDict.from_dict(
            d.pop("uploadThumbnailStatusDict")
        )

        upload_thumbnails_status_response = cls(
            upload_status=upload_status,
            upload_thumbnail_status_dict=upload_thumbnail_status_dict,
        )

        return upload_thumbnails_status_response
