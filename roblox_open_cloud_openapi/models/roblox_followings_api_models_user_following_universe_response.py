from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFollowingsApiModelsUserFollowingUniverseResponse")


@_attrs_define
class RobloxFollowingsApiModelsUserFollowingUniverseResponse:
    """Model for a user following a universe controller responses

    Attributes:
        universe_id (int | Unset): The id of the universe being followed
        user_id (int | Unset): The id of the user that is following
    """

    universe_id: int | Unset = UNSET
    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        user_id = d.pop("userId", UNSET)

        roblox_followings_api_models_user_following_universe_response = cls(
            universe_id=universe_id,
            user_id=user_id,
        )

        return roblox_followings_api_models_user_following_universe_response
