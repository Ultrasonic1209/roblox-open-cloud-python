from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
        ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
    )


T = TypeVar("T", bound="RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse")


@_attrs_define
class RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse:
    """
    Attributes:
        data (list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset):
    """

    data: list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
            ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data = d.pop("data", UNSET)
        data: list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(data_item_data)

                data.append(data_item)

        roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response = cls(
            data=data,
        )

        return roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response
