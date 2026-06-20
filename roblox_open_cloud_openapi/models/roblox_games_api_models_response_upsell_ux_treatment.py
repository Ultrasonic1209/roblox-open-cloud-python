from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_upsell_ux_treatment_data import (
        RobloxGamesApiModelsResponseUpsellUxTreatmentData,
    )


T = TypeVar("T", bound="RobloxGamesApiModelsResponseUpsellUxTreatment")


@_attrs_define
class RobloxGamesApiModelsResponseUpsellUxTreatment:
    """Upsell UX treatment metadata appended to a playability response when an experience is
    currently playable but will be restricted under upcoming Roblox-Core content rules.
    Mirrors the existing Roblox.Games.Api.Models.Response.PlayableUxTreatment contract intentionally so client
    rendering can be unified.

        Attributes:
            treatment (str | Unset): Identifier of the client component to render (currently "ageCheckUpsell").
                Absent when the upsell should not surface.
            data (RobloxGamesApiModelsResponseUpsellUxTreatmentData | Unset): Localized strings for an
                Roblox.Games.Api.Models.Response.UpsellUxTreatment. Currently only carries
                Roblox.Games.Api.Models.Response.UpsellUxTreatmentData.BodyText; structured to allow additional fields without
                breaking the
                JSON contract.
    """

    treatment: str | Unset = UNSET
    data: RobloxGamesApiModelsResponseUpsellUxTreatmentData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        treatment = self.treatment

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if treatment is not UNSET:
            field_dict["treatment"] = treatment
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_upsell_ux_treatment_data import (
            RobloxGamesApiModelsResponseUpsellUxTreatmentData,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        treatment = d.pop("treatment", UNSET)

        _data = d.pop("data", UNSET)
        data: RobloxGamesApiModelsResponseUpsellUxTreatmentData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RobloxGamesApiModelsResponseUpsellUxTreatmentData.from_dict(_data)

        roblox_games_api_models_response_upsell_ux_treatment = cls(
            treatment=treatment,
            data=data,
        )

        return roblox_games_api_models_response_upsell_ux_treatment
