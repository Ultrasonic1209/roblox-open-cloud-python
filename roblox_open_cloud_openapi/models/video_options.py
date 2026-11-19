from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.video_options_sources_item import VideoOptionsSourcesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_video import PreviewVideo


T = TypeVar("T", bound="VideoOptions")


@_attrs_define
class VideoOptions:
    """
    Attributes:
        sources (list[VideoOptionsSourcesItem]): The values accepted in `CampaignVideo.source`. Values can be
            `IMAGE_ONLY` or `PREVIEW_VIDEO`.
        preview_video (PreviewVideo | Unset):
    """

    sources: list[VideoOptionsSourcesItem]
    preview_video: PreviewVideo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.value
            sources.append(sources_item)

        preview_video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview_video, Unset):
            preview_video = self.preview_video.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sources": sources,
            }
        )
        if preview_video is not UNSET:
            field_dict["previewVideo"] = preview_video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_video import PreviewVideo  # noqa: PLC0415

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = VideoOptionsSourcesItem(sources_item_data)

            sources.append(sources_item)

        _preview_video = d.pop("previewVideo", UNSET)
        preview_video: PreviewVideo | Unset
        if isinstance(_preview_video, Unset):
            preview_video = UNSET
        else:
            preview_video = PreviewVideo.from_dict(_preview_video)

        video_options = cls(
            sources=sources,
            preview_video=preview_video,
        )

        video_options.additional_properties = d
        return video_options

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
