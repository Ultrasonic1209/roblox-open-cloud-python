from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration


T = TypeVar("T", bound="ListMatchmakingScoringConfigurationsResponse")


@_attrs_define
class ListMatchmakingScoringConfigurationsResponse:
    """Response to list matchmaking scoring configurations in a universe.

    Attributes:
        scoring_configurations (list[MatchmakingScoringConfiguration] | None | Unset): The scoring configurations.
    """

    scoring_configurations: list[MatchmakingScoringConfiguration] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scoring_configurations: list[dict[str, Any]] | None | Unset
        if isinstance(self.scoring_configurations, Unset):
            scoring_configurations = UNSET
        elif isinstance(self.scoring_configurations, list):
            scoring_configurations = []
            for scoring_configurations_type_0_item_data in self.scoring_configurations:
                scoring_configurations_type_0_item = scoring_configurations_type_0_item_data.to_dict()
                scoring_configurations.append(scoring_configurations_type_0_item)

        else:
            scoring_configurations = self.scoring_configurations

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scoring_configurations is not UNSET:
            field_dict["scoringConfigurations"] = scoring_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration import MatchmakingScoringConfiguration

        d = dict(src_dict)

        def _parse_scoring_configurations(data: object) -> list[MatchmakingScoringConfiguration] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scoring_configurations_type_0 = []
                _scoring_configurations_type_0 = data
                for scoring_configurations_type_0_item_data in _scoring_configurations_type_0:
                    scoring_configurations_type_0_item = MatchmakingScoringConfiguration.from_dict(
                        scoring_configurations_type_0_item_data
                    )

                    scoring_configurations_type_0.append(scoring_configurations_type_0_item)

                return scoring_configurations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MatchmakingScoringConfiguration] | None | Unset, data)

        scoring_configurations = _parse_scoring_configurations(d.pop("scoringConfigurations", UNSET))

        list_matchmaking_scoring_configurations_response = cls(
            scoring_configurations=scoring_configurations,
        )

        return list_matchmaking_scoring_configurations_response
