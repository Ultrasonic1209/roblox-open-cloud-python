from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameContentMetadataResponseModel")


@_attrs_define
class RobloxGamesApiModelsResponseGameContentMetadataResponseModel:
    """Response model for game-level content metadata.

    Attributes:
        badge_position (str | Unset):
        badge_analytics_id (str | Unset):
        badge_type (str | Unset):
        badge_icon (str | Unset):
        badge_component_type (str | Unset):
    """

    badge_position: str | Unset = UNSET
    badge_analytics_id: str | Unset = UNSET
    badge_type: str | Unset = UNSET
    badge_icon: str | Unset = UNSET
    badge_component_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        badge_position = self.badge_position

        badge_analytics_id = self.badge_analytics_id

        badge_type = self.badge_type

        badge_icon = self.badge_icon

        badge_component_type = self.badge_component_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if badge_position is not UNSET:
            field_dict["badgePosition"] = badge_position
        if badge_analytics_id is not UNSET:
            field_dict["badgeAnalyticsId"] = badge_analytics_id
        if badge_type is not UNSET:
            field_dict["badgeType"] = badge_type
        if badge_icon is not UNSET:
            field_dict["badgeIcon"] = badge_icon
        if badge_component_type is not UNSET:
            field_dict["badgeComponentType"] = badge_component_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_position = d.pop("badgePosition", UNSET)

        badge_analytics_id = d.pop("badgeAnalyticsId", UNSET)

        badge_type = d.pop("badgeType", UNSET)

        badge_icon = d.pop("badgeIcon", UNSET)

        badge_component_type = d.pop("badgeComponentType", UNSET)

        roblox_games_api_models_response_game_content_metadata_response_model = cls(
            badge_position=badge_position,
            badge_analytics_id=badge_analytics_id,
            badge_type=badge_type,
            badge_icon=badge_icon,
            badge_component_type=badge_component_type,
        )

        return roblox_games_api_models_response_game_content_metadata_response_model
