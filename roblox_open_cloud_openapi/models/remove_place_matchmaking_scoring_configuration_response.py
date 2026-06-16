from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RemovePlaceMatchmakingScoringConfigurationResponse")


@_attrs_define
class RemovePlaceMatchmakingScoringConfigurationResponse:
    """Response to remove scoring configuration for a place."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        remove_place_matchmaking_scoring_configuration_response = cls()

        return remove_place_matchmaking_scoring_configuration_response
