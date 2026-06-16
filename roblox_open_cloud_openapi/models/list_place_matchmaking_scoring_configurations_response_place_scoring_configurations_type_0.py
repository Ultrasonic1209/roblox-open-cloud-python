from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration


T = TypeVar("T", bound="ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0")


@_attrs_define
class ListPlaceMatchmakingScoringConfigurationsResponsePlaceScoringConfigurationsType0:
    """The scoring configurations for places."""

    additional_properties: dict[str, MatchmakingScoringConfiguration] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration

        d = dict(src_dict)
        list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = MatchmakingScoringConfiguration.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0.additional_properties = additional_properties
        return list_place_matchmaking_scoring_configurations_response_place_scoring_configurations_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> MatchmakingScoringConfiguration:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: MatchmakingScoringConfiguration) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
