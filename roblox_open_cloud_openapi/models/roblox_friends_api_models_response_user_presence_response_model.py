from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseUserPresenceResponseModel")


@_attrs_define
class RobloxFriendsApiModelsResponseUserPresenceResponseModel:
    """Response model for !:IUserPresence objects

    Attributes:
        user_presence_type (str | Unset): User Presence Type
        user_location_type (str | Unset): Location Type
        last_location (str | Unset): Last Location
        place_id (int | Unset): Place Id
        root_place_id (int | Unset): Root Place Id
        game_instance_id (UUID | Unset): Game Instance Id
        universe_id (int | Unset): Universe Id
        last_online (datetime.datetime | Unset): Most recent time online
    """

    user_presence_type: str | Unset = UNSET
    user_location_type: str | Unset = UNSET
    last_location: str | Unset = UNSET
    place_id: int | Unset = UNSET
    root_place_id: int | Unset = UNSET
    game_instance_id: UUID | Unset = UNSET
    universe_id: int | Unset = UNSET
    last_online: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_presence_type = self.user_presence_type

        user_location_type = self.user_location_type

        last_location = self.last_location

        place_id = self.place_id

        root_place_id = self.root_place_id

        game_instance_id: str | Unset = UNSET
        if not isinstance(self.game_instance_id, Unset):
            game_instance_id = str(self.game_instance_id)

        universe_id = self.universe_id

        last_online: str | Unset = UNSET
        if not isinstance(self.last_online, Unset):
            last_online = self.last_online.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_presence_type is not UNSET:
            field_dict["UserPresenceType"] = user_presence_type
        if user_location_type is not UNSET:
            field_dict["UserLocationType"] = user_location_type
        if last_location is not UNSET:
            field_dict["lastLocation"] = last_location
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id
        if game_instance_id is not UNSET:
            field_dict["gameInstanceId"] = game_instance_id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if last_online is not UNSET:
            field_dict["lastOnline"] = last_online

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_presence_type = d.pop("UserPresenceType", UNSET)

        user_location_type = d.pop("UserLocationType", UNSET)

        last_location = d.pop("lastLocation", UNSET)

        place_id = d.pop("placeId", UNSET)

        root_place_id = d.pop("rootPlaceId", UNSET)

        _game_instance_id = d.pop("gameInstanceId", UNSET)
        game_instance_id: UUID | Unset
        if isinstance(_game_instance_id, Unset):
            game_instance_id = UNSET
        else:
            game_instance_id = UUID(_game_instance_id)

        universe_id = d.pop("universeId", UNSET)

        _last_online = d.pop("lastOnline", UNSET)
        last_online: datetime.datetime | Unset
        if isinstance(_last_online, Unset):
            last_online = UNSET
        else:
            last_online = datetime.datetime.fromisoformat(_last_online)

        roblox_friends_api_models_response_user_presence_response_model = cls(
            user_presence_type=user_presence_type,
            user_location_type=user_location_type,
            last_location=last_location,
            place_id=place_id,
            root_place_id=root_place_id,
            game_instance_id=game_instance_id,
            universe_id=universe_id,
            last_online=last_online,
        )

        return roblox_friends_api_models_response_user_presence_response_model
