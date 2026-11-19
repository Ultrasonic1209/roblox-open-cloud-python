from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_video_source import CampaignVideoSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignVideo")


@_attrs_define
class CampaignVideo:
    """
    Attributes:
        source (CampaignVideoSource): The video shown on the sponsored tile. Values can be `IMAGE_ONLY` or
            `PREVIEW_VIDEO`.
        preview_video_asset_id (str | Unset): When source is `PREVIEW_VIDEO`, the experience's current preview video
            asset ID,
            as a decimal string (read-only). Omitted when the experience has no eligible
            preview video, in which case the tile shows the image creative. Also omitted
            when sponsored video tiles aren't enabled for the campaign's billing account.
    """

    source: CampaignVideoSource
    preview_video_asset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        preview_video_asset_id = self.preview_video_asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if preview_video_asset_id is not UNSET:
            field_dict["previewVideoAssetId"] = preview_video_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = CampaignVideoSource(d.pop("source"))

        preview_video_asset_id = d.pop("previewVideoAssetId", UNSET)

        campaign_video = cls(
            source=source,
            preview_video_asset_id=preview_video_asset_id,
        )

        campaign_video.additional_properties = d
        return campaign_video

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
