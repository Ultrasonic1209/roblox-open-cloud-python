from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_friends_api_models_response_friend_response import RobloxFriendsApiModelsResponseFriendResponse


T = TypeVar("T", bound="RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse")


@_attrs_define
class RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse:
    """
    Attributes:
        previous_cursor (str | Unset):
        page_items (list[RobloxFriendsApiModelsResponseFriendResponse] | Unset):
        next_cursor (str | Unset):
        has_more (bool | Unset):
    """

    previous_cursor: str | Unset = UNSET
    page_items: list[RobloxFriendsApiModelsResponseFriendResponse] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    has_more: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        previous_cursor = self.previous_cursor

        page_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.page_items, Unset):
            page_items = []
            for page_items_item_data in self.page_items:
                page_items_item = page_items_item_data.to_dict()
                page_items.append(page_items_item)

        next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if previous_cursor is not UNSET:
            field_dict["PreviousCursor"] = previous_cursor
        if page_items is not UNSET:
            field_dict["PageItems"] = page_items
        if next_cursor is not UNSET:
            field_dict["NextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["HasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_friends_api_models_response_friend_response import (
            RobloxFriendsApiModelsResponseFriendResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        previous_cursor = d.pop("PreviousCursor", UNSET)

        _page_items = d.pop("PageItems", UNSET)
        page_items: list[RobloxFriendsApiModelsResponseFriendResponse] | Unset = UNSET
        if _page_items is not UNSET:
            page_items = []
            for page_items_item_data in _page_items:
                page_items_item = RobloxFriendsApiModelsResponseFriendResponse.from_dict(page_items_item_data)

                page_items.append(page_items_item)

        next_cursor = d.pop("NextCursor", UNSET)

        has_more = d.pop("HasMore", UNSET)

        roblox_paging_cursored_paged_result_roblox_friends_api_models_response_friend_response = cls(
            previous_cursor=previous_cursor,
            page_items=page_items,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        return roblox_paging_cursored_paged_result_roblox_friends_api_models_response_friend_response
