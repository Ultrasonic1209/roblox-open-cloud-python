from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewAssetsModelType0")


@_attrs_define
class PreviewAssetsModelType0:
    """Grouped preview asset ids for an item, separated by media type.

    Attributes:
        image_preview_assets (list[int] | None | Unset): Ordered list of image preview asset ids.
        video_preview_assets (list[int] | None | Unset): Ordered list of video preview asset ids.
    """

    image_preview_assets: list[int] | None | Unset = UNSET
    video_preview_assets: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_preview_assets: list[int] | None | Unset
        if isinstance(self.image_preview_assets, Unset):
            image_preview_assets = UNSET
        elif isinstance(self.image_preview_assets, list):
            image_preview_assets = self.image_preview_assets

        else:
            image_preview_assets = self.image_preview_assets

        video_preview_assets: list[int] | None | Unset
        if isinstance(self.video_preview_assets, Unset):
            video_preview_assets = UNSET
        elif isinstance(self.video_preview_assets, list):
            video_preview_assets = self.video_preview_assets

        else:
            video_preview_assets = self.video_preview_assets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if image_preview_assets is not UNSET:
            field_dict["imagePreviewAssets"] = image_preview_assets
        if video_preview_assets is not UNSET:
            field_dict["videoPreviewAssets"] = video_preview_assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_image_preview_assets(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_preview_assets_type_0 = cast(list[int], data)

                return image_preview_assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        image_preview_assets = _parse_image_preview_assets(d.pop("imagePreviewAssets", UNSET))

        def _parse_video_preview_assets(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                video_preview_assets_type_0 = cast(list[int], data)

                return video_preview_assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        video_preview_assets = _parse_video_preview_assets(d.pop("videoPreviewAssets", UNSET))

        preview_assets_model_type_0 = cls(
            image_preview_assets=image_preview_assets,
            video_preview_assets=video_preview_assets,
        )

        return preview_assets_model_type_0
