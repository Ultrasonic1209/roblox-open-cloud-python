from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupSearchMetadataResponse")


@_attrs_define
class RobloxGroupsApiGroupSearchMetadataResponse:
    """Response Model For Group Search Metadata Endpoint

    Attributes:
        suggested_group_keywords (list[str] | Unset): Suggested Group Category translation keys
        show_friends_groups_sort (bool | Unset): Whether or not the Friends' Groups sort should show for the
            authenticated user
    """

    suggested_group_keywords: list[str] | Unset = UNSET
    show_friends_groups_sort: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        suggested_group_keywords: list[str] | Unset = UNSET
        if not isinstance(self.suggested_group_keywords, Unset):
            suggested_group_keywords = self.suggested_group_keywords

        show_friends_groups_sort = self.show_friends_groups_sort

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if suggested_group_keywords is not UNSET:
            field_dict["SuggestedGroupKeywords"] = suggested_group_keywords
        if show_friends_groups_sort is not UNSET:
            field_dict["ShowFriendsGroupsSort"] = show_friends_groups_sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        suggested_group_keywords = cast(list[str], d.pop("SuggestedGroupKeywords", UNSET))

        show_friends_groups_sort = d.pop("ShowFriendsGroupsSort", UNSET)

        roblox_groups_api_group_search_metadata_response = cls(
            suggested_group_keywords=suggested_group_keywords,
            show_friends_groups_sort=show_friends_groups_sort,
        )

        return roblox_groups_api_group_search_metadata_response
