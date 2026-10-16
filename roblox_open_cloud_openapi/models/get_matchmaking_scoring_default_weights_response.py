from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_matchmaking_scoring_default_weights_response_weights_type_0 import (
        GetMatchmakingScoringDefaultWeightsResponseWeightsType0,
    )


T = TypeVar("T", bound="GetMatchmakingScoringDefaultWeightsResponse")


@_attrs_define
class GetMatchmakingScoringDefaultWeightsResponse:
    """Response containing the weights of the current default matchmaking scoring weights

    Attributes:
        weights (GetMatchmakingScoringDefaultWeightsResponseWeightsType0 | None | Unset): The weights of the current
            default matchmaking scoring weights.
    """

    weights: GetMatchmakingScoringDefaultWeightsResponseWeightsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_matchmaking_scoring_default_weights_response_weights_type_0 import (
            GetMatchmakingScoringDefaultWeightsResponseWeightsType0,
        )

        weights: dict[str, Any] | None | Unset
        if isinstance(self.weights, Unset):
            weights = UNSET
        elif isinstance(self.weights, GetMatchmakingScoringDefaultWeightsResponseWeightsType0):
            weights = self.weights.to_dict()
        else:
            weights = self.weights

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if weights is not UNSET:
            field_dict["weights"] = weights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_matchmaking_scoring_default_weights_response_weights_type_0 import (
            GetMatchmakingScoringDefaultWeightsResponseWeightsType0,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_weights(data: object) -> GetMatchmakingScoringDefaultWeightsResponseWeightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weights_type_0 = GetMatchmakingScoringDefaultWeightsResponseWeightsType0.from_dict(data)

                return weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMatchmakingScoringDefaultWeightsResponseWeightsType0 | None | Unset, data)

        weights = _parse_weights(d.pop("weights", UNSET))

        get_matchmaking_scoring_default_weights_response = cls(
            weights=weights,
        )

        return get_matchmaking_scoring_default_weights_response
