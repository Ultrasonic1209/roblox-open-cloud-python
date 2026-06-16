from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_friends_api_models_response_user_presence_response_model import (
        RobloxFriendsApiModelsResponseUserPresenceResponseModel,
    )


T = TypeVar("T", bound="RobloxFriendsApiModelsResponseUserPresenceResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseUserPresenceResponse:
    """A response model representing user presence information.

    Attributes:
        user_presence (RobloxFriendsApiModelsResponseUserPresenceResponseModel | Unset): Response model for
            !:IUserPresence objects
        sort_score (float | Unset): Carousel sort score
        id (int | Unset): The user Id.
        name (str | Unset): The user name.
        display_name (str | Unset): The user DisplayName.
    """

    user_presence: RobloxFriendsApiModelsResponseUserPresenceResponseModel | Unset = UNSET
    sort_score: float | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_presence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_presence, Unset):
            user_presence = self.user_presence.to_dict()

        sort_score = self.sort_score

        id = self.id

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_presence is not UNSET:
            field_dict["userPresence"] = user_presence
        if sort_score is not UNSET:
            field_dict["sortScore"] = sort_score
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_friends_api_models_response_user_presence_response_model import (
            RobloxFriendsApiModelsResponseUserPresenceResponseModel,
        )

        d = dict(src_dict)
        _user_presence = d.pop("userPresence", UNSET)
        user_presence: RobloxFriendsApiModelsResponseUserPresenceResponseModel | Unset
        if isinstance(_user_presence, Unset):
            user_presence = UNSET
        else:
            user_presence = RobloxFriendsApiModelsResponseUserPresenceResponseModel.from_dict(_user_presence)

        sort_score = d.pop("sortScore", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_friends_api_models_response_user_presence_response = cls(
            user_presence=user_presence,
            sort_score=sort_score,
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_friends_api_models_response_user_presence_response
