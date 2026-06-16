from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_playable_ux_treatment_data import (
        RobloxGamesApiModelsResponsePlayableUxTreatmentData,
    )


T = TypeVar("T", bound="RobloxGamesApiModelsResponsePlayableUxTreatment")


@_attrs_define
class RobloxGamesApiModelsResponsePlayableUxTreatment:
    """
    Attributes:
        treatment (str | Unset):
        data (RobloxGamesApiModelsResponsePlayableUxTreatmentData | Unset):
    """

    treatment: str | Unset = UNSET
    data: RobloxGamesApiModelsResponsePlayableUxTreatmentData | Unset = UNSET

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
        from ..models.roblox_games_api_models_response_playable_ux_treatment_data import (
            RobloxGamesApiModelsResponsePlayableUxTreatmentData,
        )

        d = dict(src_dict)
        treatment = d.pop("treatment", UNSET)

        _data = d.pop("data", UNSET)
        data: RobloxGamesApiModelsResponsePlayableUxTreatmentData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RobloxGamesApiModelsResponsePlayableUxTreatmentData.from_dict(_data)

        roblox_games_api_models_response_playable_ux_treatment = cls(
            treatment=treatment,
            data=data,
        )

        return roblox_games_api_models_response_playable_ux_treatment
