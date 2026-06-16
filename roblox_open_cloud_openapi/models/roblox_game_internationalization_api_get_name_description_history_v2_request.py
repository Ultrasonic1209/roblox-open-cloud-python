from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_get_name_description_history_v2_request_content_type import (
    RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType,
)
from ..models.roblox_game_internationalization_api_get_name_description_history_v2_request_sort_order import (
    RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiGetNameDescriptionHistoryV2Request")


@_attrs_define
class RobloxGameInternationalizationApiGetNameDescriptionHistoryV2Request:
    """A model containing request for getting the translation history of
    a content source type's name or description.

        Attributes:
            content_id (int | Unset):
            content_type (RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType | Unset): The enum
                representing the type of request while requesting name/description history ['UniverseDisplayNames' = 0,
                'UniverseDisplayDescriptions' = 1, 'BadgeDisplayName' = 2, 'BadgeDisplayDescription' = 3,
                'DeveloperProductDisplayName' = 4, 'DeveloperProductDisplayDescription' = 5, 'GamePassDisplayName' = 6,
                'GamePassDisplayDescription' = 7]
            language_code (str | Unset):
            cursor (str | Unset):
            count (int | Unset):
            sort_order (RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder | Unset):  ['Asc' = 1,
                'Desc' = 2]
    """

    content_id: int | Unset = UNSET
    content_type: RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType | Unset = UNSET
    language_code: str | Unset = UNSET
    cursor: str | Unset = UNSET
    count: int | Unset = UNSET
    sort_order: RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content_id = self.content_id

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        language_code = self.language_code

        cursor = self.cursor

        count = self.count

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if content_id is not UNSET:
            field_dict["contentId"] = content_id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if count is not UNSET:
            field_dict["count"] = count
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_id = d.pop("contentId", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestContentType(_content_type)

        language_code = d.pop("languageCode", UNSET)

        cursor = d.pop("cursor", UNSET)

        count = d.pop("count", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder(_sort_order)

        roblox_game_internationalization_api_get_name_description_history_v2_request = cls(
            content_id=content_id,
            content_type=content_type,
            language_code=language_code,
            cursor=cursor,
            count=count,
            sort_order=sort_order,
        )

        return roblox_game_internationalization_api_get_name_description_history_v2_request
