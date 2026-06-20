from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0 import (
        ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0,
    )


T = TypeVar("T", bound="ListPlaceMatchmakingScoringConfigurationsResponse")


@_attrs_define
class ListPlaceMatchmakingScoringConfigurationsResponse:
    """Response to list all places with scoring configuration in a universe.

    Attributes:
        place_scoring_configurations (ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0 |
            None | Unset): The scoring configurations for places.
    """

    place_scoring_configurations: (
        ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0 | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0 import (
            ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0,
        )

        place_scoring_configurations: dict[str, Any] | None | Unset
        if isinstance(self.place_scoring_configurations, Unset):
            place_scoring_configurations = UNSET
        elif isinstance(
            self.place_scoring_configurations,
            ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0,
        ):
            place_scoring_configurations = self.place_scoring_configurations.to_dict()
        else:
            place_scoring_configurations = self.place_scoring_configurations

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_scoring_configurations is not UNSET:
            field_dict["placeScoringConfigurations"] = place_scoring_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0 import (
            ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_place_scoring_configurations(
            data: object,
        ) -> ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_scoring_configurations_type_0 = (
                    ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0.from_dict(data)
                )

                return place_scoring_configurations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0 | None | Unset, data
            )

        place_scoring_configurations = _parse_place_scoring_configurations(d.pop("placeScoringConfigurations", UNSET))

        list_place_matchmaking_scoring_configurations_response = cls(
            place_scoring_configurations=place_scoring_configurations,
        )

        return list_place_matchmaking_scoring_configurations_response
