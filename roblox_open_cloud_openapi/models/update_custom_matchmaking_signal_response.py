from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration


T = TypeVar("T", bound="UpdateCustomMatchmakingSignalResponse")


@_attrs_define
class UpdateCustomMatchmakingSignalResponse:
    """Response to update a custom matchmaking signal.

    Attributes:
        scoring_configuration (MatchmakingScoringConfiguration | Unset): The custom scoring configuration for
            matchmaking.
    """

    scoring_configuration: MatchmakingScoringConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scoring_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scoring_configuration, Unset):
            scoring_configuration = self.scoring_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scoring_configuration is not UNSET:
            field_dict["scoringConfiguration"] = scoring_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _scoring_configuration = d.pop("scoringConfiguration", UNSET)
        scoring_configuration: MatchmakingScoringConfiguration | Unset
        if isinstance(_scoring_configuration, Unset):
            scoring_configuration = UNSET
        else:
            scoring_configuration = MatchmakingScoringConfiguration.from_dict(_scoring_configuration)

        update_custom_matchmaking_signal_response = cls(
            scoring_configuration=scoring_configuration,
        )

        return update_custom_matchmaking_signal_response
