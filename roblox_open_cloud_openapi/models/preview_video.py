from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewVideo")


@_attrs_define
class PreviewVideo:
    """
    Attributes:
        available (bool): Whether the experience has a preview video eligible to be shown.
        video_asset_id (str | Unset): The preview video's asset ID, as a decimal string. Present only when available is
            true.
    """

    available: bool
    video_asset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        video_asset_id = self.video_asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available": available,
            }
        )
        if video_asset_id is not UNSET:
            field_dict["videoAssetId"] = video_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        video_asset_id = d.pop("videoAssetId", UNSET)

        preview_video = cls(
            available=available,
            video_asset_id=video_asset_id,
        )

        preview_video.additional_properties = d
        return preview_video

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
