from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.place_content_preference import PlaceContentPreference

T = TypeVar("T", bound="PlacePreferenceRequest")


@_attrs_define
class PlacePreferenceRequest:
    """Request format for POST /v1/place-preference

    Attributes:
        user_id (int): The User ID of the requesting user.
        place_id (int): The place the preference is being added to.
        place_content_preference (PlaceContentPreference): Type of preference. Used to determine what types of
            notifications a user is sent for a given place.

            0 = None

            1 = All

            2 = MentionsAndReplies

            3 = Unknown
    """

    user_id: int
    place_id: int
    place_content_preference: PlaceContentPreference

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        place_id = self.place_id

        place_content_preference = self.place_content_preference.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
                "placeId": place_id,
                "placeContentPreference": place_content_preference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        place_id = d.pop("placeId")

        place_content_preference = PlaceContentPreference(d.pop("placeContentPreference"))

        place_preference_request = cls(
            user_id=user_id,
            place_id=place_id,
            place_content_preference=place_content_preference,
        )

        return place_preference_request
