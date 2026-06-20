from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetPlaceMatchmakingScoringConfigurationRequest")


@_attrs_define
class SetPlaceMatchmakingScoringConfigurationRequest:
    """Request to set the matchmaking scoring configuration for a place.

    Attributes:
        place_id (int | Unset): The place ID of the desired scoring configuration to set.
        scoring_configuration_id (None | str | Unset): The ID of the scoring configuration.
    """

    place_id: int | Unset = UNSET
    scoring_configuration_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        scoring_configuration_id: None | str | Unset
        if isinstance(self.scoring_configuration_id, Unset):
            scoring_configuration_id = UNSET
        else:
            scoring_configuration_id = self.scoring_configuration_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if scoring_configuration_id is not UNSET:
            field_dict["scoringConfigurationId"] = scoring_configuration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        def _parse_scoring_configuration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scoring_configuration_id = _parse_scoring_configuration_id(d.pop("scoringConfigurationId", UNSET))

        set_place_matchmaking_scoring_configuration_request = cls(
            place_id=place_id,
            scoring_configuration_id=scoring_configuration_id,
        )

        return set_place_matchmaking_scoring_configuration_request
