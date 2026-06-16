from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_client_blocked_keyword_model import RobloxGroupsClientBlockedKeywordModel


T = TypeVar("T", bound="RobloxGroupsClientCreateBlockedKeywordsResponse")


@_attrs_define
class RobloxGroupsClientCreateBlockedKeywordsResponse:
    """
    Attributes:
        created_keywords (list[RobloxGroupsClientBlockedKeywordModel] | Unset):
        had_moderated_keywords (bool | Unset):
        had_duplicate_keywords (bool | Unset):
    """

    created_keywords: list[RobloxGroupsClientBlockedKeywordModel] | Unset = UNSET
    had_moderated_keywords: bool | Unset = UNSET
    had_duplicate_keywords: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_keywords: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.created_keywords, Unset):
            created_keywords = []
            for created_keywords_item_data in self.created_keywords:
                created_keywords_item = created_keywords_item_data.to_dict()
                created_keywords.append(created_keywords_item)

        had_moderated_keywords = self.had_moderated_keywords

        had_duplicate_keywords = self.had_duplicate_keywords

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if created_keywords is not UNSET:
            field_dict["createdKeywords"] = created_keywords
        if had_moderated_keywords is not UNSET:
            field_dict["hadModeratedKeywords"] = had_moderated_keywords
        if had_duplicate_keywords is not UNSET:
            field_dict["hadDuplicateKeywords"] = had_duplicate_keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_client_blocked_keyword_model import RobloxGroupsClientBlockedKeywordModel

        d = dict(src_dict)
        _created_keywords = d.pop("createdKeywords", UNSET)
        created_keywords: list[RobloxGroupsClientBlockedKeywordModel] | Unset = UNSET
        if _created_keywords is not UNSET:
            created_keywords = []
            for created_keywords_item_data in _created_keywords:
                created_keywords_item = RobloxGroupsClientBlockedKeywordModel.from_dict(created_keywords_item_data)

                created_keywords.append(created_keywords_item)

        had_moderated_keywords = d.pop("hadModeratedKeywords", UNSET)

        had_duplicate_keywords = d.pop("hadDuplicateKeywords", UNSET)

        roblox_groups_client_create_blocked_keywords_response = cls(
            created_keywords=created_keywords,
            had_moderated_keywords=had_moderated_keywords,
            had_duplicate_keywords=had_duplicate_keywords,
        )

        return roblox_groups_client_create_blocked_keywords_response
