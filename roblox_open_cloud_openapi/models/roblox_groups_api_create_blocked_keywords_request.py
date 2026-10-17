from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiCreateBlockedKeywordsRequest")


@_attrs_define
class RobloxGroupsApiCreateBlockedKeywordsRequest:
    """
    Attributes:
        keywords (str | Unset):
        is_private (bool | Unset):
    """

    keywords: str | Unset = UNSET
    is_private: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        is_private = self.is_private

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords", UNSET)

        is_private = d.pop("isPrivate", UNSET)

        roblox_groups_api_create_blocked_keywords_request = cls(
            keywords=keywords,
            is_private=is_private,
        )

        return roblox_groups_api_create_blocked_keywords_request
