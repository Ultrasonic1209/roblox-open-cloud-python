from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_media_asset_response_state import (
    RobloxGameInternationalizationApiMediaAssetResponseState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiMediaAssetResponse")


@_attrs_define
class RobloxGameInternationalizationApiMediaAssetResponse:
    """
    Attributes:
        media_asset_id (str | Unset):
        media_asset_alt_text (str | Unset):
        state (RobloxGameInternationalizationApiMediaAssetResponseState | Unset): Enum for image status. ['Approved' =
            0, 'PendingReview' = 1, 'UnAvailable' = 2, 'Rejected' = 3, 'Error' = 4]
        media_asset_url (str | Unset):
    """

    media_asset_id: str | Unset = UNSET
    media_asset_alt_text: str | Unset = UNSET
    state: RobloxGameInternationalizationApiMediaAssetResponseState | Unset = UNSET
    media_asset_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_asset_id = self.media_asset_id

        media_asset_alt_text = self.media_asset_alt_text

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        media_asset_url = self.media_asset_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_asset_id is not UNSET:
            field_dict["mediaAssetId"] = media_asset_id
        if media_asset_alt_text is not UNSET:
            field_dict["mediaAssetAltText"] = media_asset_alt_text
        if state is not UNSET:
            field_dict["state"] = state
        if media_asset_url is not UNSET:
            field_dict["mediaAssetUrl"] = media_asset_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_asset_id = d.pop("mediaAssetId", UNSET)

        media_asset_alt_text = d.pop("mediaAssetAltText", UNSET)

        _state = d.pop("state", UNSET)
        state: RobloxGameInternationalizationApiMediaAssetResponseState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RobloxGameInternationalizationApiMediaAssetResponseState(_state)

        media_asset_url = d.pop("mediaAssetUrl", UNSET)

        roblox_game_internationalization_api_media_asset_response = cls(
            media_asset_id=media_asset_id,
            media_asset_alt_text=media_asset_alt_text,
            state=state,
            media_asset_url=media_asset_url,
        )

        return roblox_game_internationalization_api_media_asset_response
