from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.thumbnail_personalization_api_moderation_status import ThumbnailPersonalizationApiModerationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadThumbnailStatus")


@_attrs_define
class UploadThumbnailStatus:
    """
    Attributes:
        homepage_thumbnail_id (None | str | Unset):
        asset_id (int | Unset):
        moderation_status (ThumbnailPersonalizationApiModerationStatus | Unset):
    """

    homepage_thumbnail_id: None | str | Unset = UNSET
    asset_id: int | Unset = UNSET
    moderation_status: ThumbnailPersonalizationApiModerationStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        homepage_thumbnail_id: None | str | Unset
        if isinstance(self.homepage_thumbnail_id, Unset):
            homepage_thumbnail_id = UNSET
        else:
            homepage_thumbnail_id = self.homepage_thumbnail_id

        asset_id = self.asset_id

        moderation_status: str | Unset = UNSET
        if not isinstance(self.moderation_status, Unset):
            moderation_status = self.moderation_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if homepage_thumbnail_id is not UNSET:
            field_dict["homepageThumbnailId"] = homepage_thumbnail_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_homepage_thumbnail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        homepage_thumbnail_id = _parse_homepage_thumbnail_id(d.pop("homepageThumbnailId", UNSET))

        asset_id = d.pop("assetId", UNSET)

        _moderation_status = d.pop("moderationStatus", UNSET)
        moderation_status: ThumbnailPersonalizationApiModerationStatus | Unset
        if isinstance(_moderation_status, Unset):
            moderation_status = UNSET
        else:
            moderation_status = ThumbnailPersonalizationApiModerationStatus(_moderation_status)

        upload_thumbnail_status = cls(
            homepage_thumbnail_id=homepage_thumbnail_id,
            asset_id=asset_id,
            moderation_status=moderation_status,
        )

        return upload_thumbnail_status
