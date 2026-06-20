from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponsePlayableUxTreatmentData")


@_attrs_define
class RobloxGamesApiModelsResponsePlayableUxTreatmentData:
    """
    Attributes:
        title_text (str | Unset):
        body_text (str | Unset):
        primary_action_text (str | Unset):
        secondary_action_text (str | Unset):
    """

    title_text: str | Unset = UNSET
    body_text: str | Unset = UNSET
    primary_action_text: str | Unset = UNSET
    secondary_action_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title_text = self.title_text

        body_text = self.body_text

        primary_action_text = self.primary_action_text

        secondary_action_text = self.secondary_action_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title_text is not UNSET:
            field_dict["titleText"] = title_text
        if body_text is not UNSET:
            field_dict["bodyText"] = body_text
        if primary_action_text is not UNSET:
            field_dict["primaryActionText"] = primary_action_text
        if secondary_action_text is not UNSET:
            field_dict["secondaryActionText"] = secondary_action_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        title_text = d.pop("titleText", UNSET)

        body_text = d.pop("bodyText", UNSET)

        primary_action_text = d.pop("primaryActionText", UNSET)

        secondary_action_text = d.pop("secondaryActionText", UNSET)

        roblox_games_api_models_response_playable_ux_treatment_data = cls(
            title_text=title_text,
            body_text=body_text,
            primary_action_text=primary_action_text,
            secondary_action_text=secondary_action_text,
        )

        return roblox_games_api_models_response_playable_ux_treatment_data
