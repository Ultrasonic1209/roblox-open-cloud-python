from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsGameUpdateNotificationModel")


@_attrs_define
class RobloxApiNotificationsModelsGameUpdateNotificationModel:
    """Model for a game update message to be displayed in notification stream.

    Attributes:
        universe_id (int | Unset): ID of the game.
        root_place_id (int | Unset): ID of the game.
        created_on (datetime.datetime | Unset): Creation date of the update message.
        created_on_key (str | Unset): Key of Creation date ticks (dynamo table sort key).
        content (str | Unset): Content of the update message.
        universe_name (str | Unset): Name of the game.
    """

    universe_id: int | Unset = UNSET
    root_place_id: int | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    created_on_key: str | Unset = UNSET
    content: str | Unset = UNSET
    universe_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        root_place_id = self.root_place_id

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        created_on_key = self.created_on_key

        content = self.content

        universe_name = self.universe_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if created_on_key is not UNSET:
            field_dict["createdOnKey"] = created_on_key
        if content is not UNSET:
            field_dict["content"] = content
        if universe_name is not UNSET:
            field_dict["universeName"] = universe_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        root_place_id = d.pop("rootPlaceId", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = datetime.datetime.fromisoformat(_created_on)

        created_on_key = d.pop("createdOnKey", UNSET)

        content = d.pop("content", UNSET)

        universe_name = d.pop("universeName", UNSET)

        roblox_api_notifications_models_game_update_notification_model = cls(
            universe_id=universe_id,
            root_place_id=root_place_id,
            created_on=created_on,
            created_on_key=created_on_key,
            content=content,
            universe_name=universe_name,
        )

        return roblox_api_notifications_models_game_update_notification_model
