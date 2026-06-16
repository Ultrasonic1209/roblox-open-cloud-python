from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_followings_api_models_follows_by_type_response_follower_type import (
    RobloxFollowingsApiModelsFollowsByTypeResponseFollowerType,
)
from ..models.roblox_followings_api_models_follows_by_type_response_source_type import (
    RobloxFollowingsApiModelsFollowsByTypeResponseSourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_followings_api_models_follows_by_type_response_followed_sources import (
        RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources,
    )


T = TypeVar("T", bound="RobloxFollowingsApiModelsFollowsByTypeResponse")


@_attrs_define
class RobloxFollowingsApiModelsFollowsByTypeResponse:
    """Data model containing collection of all followed sources of a specific type.

    Attributes:
        follower_type (RobloxFollowingsApiModelsFollowsByTypeResponseFollowerType | Unset): Type of the follower entity.
            ['Invalid' = 0, 'User' = 1]
        follower_id (int | Unset): ID of the follower entity.
        source_type (RobloxFollowingsApiModelsFollowsByTypeResponseSourceType | Unset): Type of the source entity.
            ['Invalid' = 0, 'Universe' = 1]
        followed_sources (RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources | Unset): Followed sources: map
            of (source ID => follow date)
    """

    follower_type: RobloxFollowingsApiModelsFollowsByTypeResponseFollowerType | Unset = UNSET
    follower_id: int | Unset = UNSET
    source_type: RobloxFollowingsApiModelsFollowsByTypeResponseSourceType | Unset = UNSET
    followed_sources: RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        follower_type: int | Unset = UNSET
        if not isinstance(self.follower_type, Unset):
            follower_type = self.follower_type.value

        follower_id = self.follower_id

        source_type: int | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        followed_sources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.followed_sources, Unset):
            followed_sources = self.followed_sources.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if follower_type is not UNSET:
            field_dict["followerType"] = follower_type
        if follower_id is not UNSET:
            field_dict["followerId"] = follower_id
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if followed_sources is not UNSET:
            field_dict["followedSources"] = followed_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_followings_api_models_follows_by_type_response_followed_sources import (
            RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources,
        )

        d = dict(src_dict)
        _follower_type = d.pop("followerType", UNSET)
        follower_type: RobloxFollowingsApiModelsFollowsByTypeResponseFollowerType | Unset
        if isinstance(_follower_type, Unset):
            follower_type = UNSET
        else:
            follower_type = RobloxFollowingsApiModelsFollowsByTypeResponseFollowerType(_follower_type)

        follower_id = d.pop("followerId", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: RobloxFollowingsApiModelsFollowsByTypeResponseSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = RobloxFollowingsApiModelsFollowsByTypeResponseSourceType(_source_type)

        _followed_sources = d.pop("followedSources", UNSET)
        followed_sources: RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources | Unset
        if isinstance(_followed_sources, Unset):
            followed_sources = UNSET
        else:
            followed_sources = RobloxFollowingsApiModelsFollowsByTypeResponseFollowedSources.from_dict(
                _followed_sources
            )

        roblox_followings_api_models_follows_by_type_response = cls(
            follower_type=follower_type,
            follower_id=follower_id,
            source_type=source_type,
            followed_sources=followed_sources,
        )

        return roblox_followings_api_models_follows_by_type_response
