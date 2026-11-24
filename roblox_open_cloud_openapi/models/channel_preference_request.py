from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.channel_content_preference import ChannelContentPreference

T = TypeVar("T", bound="ChannelPreferenceRequest")


@_attrs_define
class ChannelPreferenceRequest:
    """Request format for POST /v1/channel-preference

    Attributes:
        user_id (int): The User ID of the requesting user.
        place_id (int): The place the channel is associated with.
        channel_id (str): The channel the preference is being added to.
        channel_content_preference (ChannelContentPreference): Type of preference. Used to determine what types of
            notifications a user is sent for a given channel.

            0 = None

            1 = All

            2 = Unknown
    """

    user_id: int
    place_id: int
    channel_id: str
    channel_content_preference: ChannelContentPreference

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        place_id = self.place_id

        channel_id = self.channel_id

        channel_content_preference = self.channel_content_preference.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
                "placeId": place_id,
                "channelId": channel_id,
                "channelContentPreference": channel_content_preference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        place_id = d.pop("placeId")

        channel_id = d.pop("channelId")

        channel_content_preference = ChannelContentPreference(d.pop("channelContentPreference"))

        channel_preference_request = cls(
            user_id=user_id,
            place_id=place_id,
            channel_id=channel_id,
            channel_content_preference=channel_content_preference,
        )

        return channel_preference_request
