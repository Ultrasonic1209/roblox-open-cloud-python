from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseUpsellUxTreatmentData")


@_attrs_define
class RobloxGamesApiModelsResponseUpsellUxTreatmentData:
    """Localized strings for an Roblox.Games.Api.Models.Response.UpsellUxTreatment. Currently only carries
    Roblox.Games.Api.Models.Response.UpsellUxTreatmentData.BodyText; structured to allow additional fields without
    breaking the
    JSON contract.

        Attributes:
            body_text (str | Unset): Localized body text for the upsell banner (e.g. "You'll soon need an age check to
                join this game.").
    """

    body_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        body_text = self.body_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if body_text is not UNSET:
            field_dict["bodyText"] = body_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        body_text = d.pop("bodyText", UNSET)

        roblox_games_api_models_response_upsell_ux_treatment_data = cls(
            body_text=body_text,
        )

        return roblox_games_api_models_response_upsell_ux_treatment_data
