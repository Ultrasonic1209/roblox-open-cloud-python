from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupContentModerationPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupContentModerationPermissionsModel:
    """A model representing group content moderation permissions

    Attributes:
        manage_keyword_block_list (bool | Unset): Manage keyword block list permission
        view_keyword_block_list (bool | Unset): View keyword block list permission
    """

    manage_keyword_block_list: bool | Unset = UNSET
    view_keyword_block_list: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        manage_keyword_block_list = self.manage_keyword_block_list

        view_keyword_block_list = self.view_keyword_block_list

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if manage_keyword_block_list is not UNSET:
            field_dict["manageKeywordBlockList"] = manage_keyword_block_list
        if view_keyword_block_list is not UNSET:
            field_dict["viewKeywordBlockList"] = view_keyword_block_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manage_keyword_block_list = d.pop("manageKeywordBlockList", UNSET)

        view_keyword_block_list = d.pop("viewKeywordBlockList", UNSET)

        roblox_groups_api_group_content_moderation_permissions_model = cls(
            manage_keyword_block_list=manage_keyword_block_list,
            view_keyword_block_list=view_keyword_block_list,
        )

        return roblox_groups_api_group_content_moderation_permissions_model
