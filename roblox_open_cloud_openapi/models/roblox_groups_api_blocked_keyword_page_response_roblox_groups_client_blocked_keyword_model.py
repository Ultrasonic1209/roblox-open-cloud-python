from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_client_blocked_keyword_model import RobloxGroupsClientBlockedKeywordModel


T = TypeVar("T", bound="RobloxGroupsApiBlockedKeywordPageResponseRobloxGroupsClientBlockedKeywordModel")


@_attrs_define
class RobloxGroupsApiBlockedKeywordPageResponseRobloxGroupsClientBlockedKeywordModel:
    """ApiPageResponse for blocked keywords

    Attributes:
        total_active_keywords_count (int | Unset): Total number of active keywords in the group
        previous_page_cursor (str | Unset):
        next_page_cursor (str | Unset):
        data (list[RobloxGroupsClientBlockedKeywordModel] | Unset):
    """

    total_active_keywords_count: int | Unset = UNSET
    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET
    data: list[RobloxGroupsClientBlockedKeywordModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_active_keywords_count = self.total_active_keywords_count

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_active_keywords_count is not UNSET:
            field_dict["totalActiveKeywordsCount"] = total_active_keywords_count
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_client_blocked_keyword_model import RobloxGroupsClientBlockedKeywordModel

        d = dict(src_dict)
        total_active_keywords_count = d.pop("totalActiveKeywordsCount", UNSET)

        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        _data = d.pop("data", UNSET)
        data: list[RobloxGroupsClientBlockedKeywordModel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxGroupsClientBlockedKeywordModel.from_dict(data_item_data)

                data.append(data_item)

        roblox_groups_api_blocked_keyword_page_response_roblox_groups_client_blocked_keyword_model = cls(
            total_active_keywords_count=total_active_keywords_count,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
            data=data,
        )

        return roblox_groups_api_blocked_keyword_page_response_roblox_groups_client_blocked_keyword_model
