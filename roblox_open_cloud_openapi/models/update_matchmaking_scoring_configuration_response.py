from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration


T = TypeVar("T", bound="UpdateMatchmakingScoringConfigurationResponse")


@_attrs_define
class UpdateMatchmakingScoringConfigurationResponse:
    """Response to update a matchmaking scoring configuration.

    Attributes:
        scoring_configuration (MatchmakingScoringConfiguration): The custom scoring configuration for matchmaking.
    """

    scoring_configuration: MatchmakingScoringConfiguration

    def to_dict(self) -> dict[str, Any]:
        scoring_configuration = self.scoring_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scoringConfiguration": scoring_configuration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        scoring_configuration = MatchmakingScoringConfiguration.from_dict(d.pop("scoringConfiguration"))

        update_matchmaking_scoring_configuration_response = cls(
            scoring_configuration=scoring_configuration,
        )

        return update_matchmaking_scoring_configuration_response
