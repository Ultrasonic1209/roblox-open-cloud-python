from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateBlockedKeywordRequest")


@_attrs_define
class RobloxGroupsApiUpdateBlockedKeywordRequest:
    """
    Attributes:
        keyword (str | Unset):
        is_private (bool | Unset):
    """

    keyword: str | Unset = UNSET
    is_private: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        is_private = self.is_private

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = d.pop("keyword", UNSET)

        is_private = d.pop("isPrivate", UNSET)

        roblox_groups_api_update_blocked_keyword_request = cls(
            keyword=keyword,
            is_private=is_private,
        )

        return roblox_groups_api_update_blocked_keyword_request
