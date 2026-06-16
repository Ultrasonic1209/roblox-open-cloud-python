from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_get_game_pass_icon_response_state import (
    RobloxGameInternationalizationApiGetGamePassIconResponseState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiGetGamePassIconResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetGamePassIconResponse:
    """A response model for getting game pass icon

    Attributes:
        image_id (str | Unset):
        image_url (str | Unset):
        state (RobloxGameInternationalizationApiGetGamePassIconResponseState | Unset): Enum for image status.
            ['Approved' = 0, 'PendingReview' = 1, 'UnAvailable' = 2, 'Rejected' = 3, 'Error' = 4]
        language_code (str | Unset):
    """

    image_id: str | Unset = UNSET
    image_url: str | Unset = UNSET
    state: RobloxGameInternationalizationApiGetGamePassIconResponseState | Unset = UNSET
    language_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_id = self.image_id

        image_url = self.image_url

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        language_code = self.language_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if state is not UNSET:
            field_dict["state"] = state
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_id = d.pop("imageId", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        _state = d.pop("state", UNSET)
        state: RobloxGameInternationalizationApiGetGamePassIconResponseState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RobloxGameInternationalizationApiGetGamePassIconResponseState(_state)

        language_code = d.pop("languageCode", UNSET)

        roblox_game_internationalization_api_get_game_pass_icon_response = cls(
            image_id=image_id,
            image_url=image_url,
            state=state,
            language_code=language_code,
        )

        return roblox_game_internationalization_api_get_game_pass_icon_response
