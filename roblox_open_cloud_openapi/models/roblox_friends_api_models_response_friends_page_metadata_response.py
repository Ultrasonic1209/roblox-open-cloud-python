from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseFriendsPageMetadataResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseFriendsPageMetadataResponse:
    """
    Attributes:
        is_friends_filter_bar_enabled (bool | Unset):
        is_friends_page_sort_experiment_enabled (bool | Unset):
        is_friends_user_data_store_cache_enabled (bool | Unset):
        frequent_friend_sort_rollout (int | Unset):
        user_name (str | Unset):
        display_name (str | Unset):
    """

    is_friends_filter_bar_enabled: bool | Unset = UNSET
    is_friends_page_sort_experiment_enabled: bool | Unset = UNSET
    is_friends_user_data_store_cache_enabled: bool | Unset = UNSET
    frequent_friend_sort_rollout: int | Unset = UNSET
    user_name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_friends_filter_bar_enabled = self.is_friends_filter_bar_enabled

        is_friends_page_sort_experiment_enabled = self.is_friends_page_sort_experiment_enabled

        is_friends_user_data_store_cache_enabled = self.is_friends_user_data_store_cache_enabled

        frequent_friend_sort_rollout = self.frequent_friend_sort_rollout

        user_name = self.user_name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_friends_filter_bar_enabled is not UNSET:
            field_dict["isFriendsFilterBarEnabled"] = is_friends_filter_bar_enabled
        if is_friends_page_sort_experiment_enabled is not UNSET:
            field_dict["isFriendsPageSortExperimentEnabled"] = is_friends_page_sort_experiment_enabled
        if is_friends_user_data_store_cache_enabled is not UNSET:
            field_dict["isFriendsUserDataStoreCacheEnabled"] = is_friends_user_data_store_cache_enabled
        if frequent_friend_sort_rollout is not UNSET:
            field_dict["frequentFriendSortRollout"] = frequent_friend_sort_rollout
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_friends_filter_bar_enabled = d.pop("isFriendsFilterBarEnabled", UNSET)

        is_friends_page_sort_experiment_enabled = d.pop("isFriendsPageSortExperimentEnabled", UNSET)

        is_friends_user_data_store_cache_enabled = d.pop("isFriendsUserDataStoreCacheEnabled", UNSET)

        frequent_friend_sort_rollout = d.pop("frequentFriendSortRollout", UNSET)

        user_name = d.pop("userName", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_friends_api_models_response_friends_page_metadata_response = cls(
            is_friends_filter_bar_enabled=is_friends_filter_bar_enabled,
            is_friends_page_sort_experiment_enabled=is_friends_page_sort_experiment_enabled,
            is_friends_user_data_store_cache_enabled=is_friends_user_data_store_cache_enabled,
            frequent_friend_sort_rollout=frequent_friend_sort_rollout,
            user_name=user_name,
            display_name=display_name,
        )

        return roblox_friends_api_models_response_friends_page_metadata_response
