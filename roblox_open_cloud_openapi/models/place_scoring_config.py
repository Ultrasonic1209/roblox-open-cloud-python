from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceScoringConfig")


@_attrs_define
class PlaceScoringConfig:
    """Matchmaking scoring configuration applied to a single place in an experiment variant.

    Attributes:
        place_id (int | Unset): Place ID this scoring config applies to.
        matchmaking_scoring_config_id (None | str | Unset): Matchmaking scoring config ID for this place. Ignored when
            UsePlatformDefault is true.
        use_platform_default (bool | Unset): When true, this place uses the platform default matchmaking scoring config
            instead of
            MatchmakingScoringConfigId.
    """

    place_id: int | Unset = UNSET
    matchmaking_scoring_config_id: None | str | Unset = UNSET
    use_platform_default: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        matchmaking_scoring_config_id: None | str | Unset
        if isinstance(self.matchmaking_scoring_config_id, Unset):
            matchmaking_scoring_config_id = UNSET
        else:
            matchmaking_scoring_config_id = self.matchmaking_scoring_config_id

        use_platform_default = self.use_platform_default

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if matchmaking_scoring_config_id is not UNSET:
            field_dict["matchmakingScoringConfigId"] = matchmaking_scoring_config_id
        if use_platform_default is not UNSET:
            field_dict["usePlatformDefault"] = use_platform_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        def _parse_matchmaking_scoring_config_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        matchmaking_scoring_config_id = _parse_matchmaking_scoring_config_id(d.pop("matchmakingScoringConfigId", UNSET))

        use_platform_default = d.pop("usePlatformDefault", UNSET)

        place_scoring_config = cls(
            place_id=place_id,
            matchmaking_scoring_config_id=matchmaking_scoring_config_id,
            use_platform_default=use_platform_default,
        )

        return place_scoring_config
