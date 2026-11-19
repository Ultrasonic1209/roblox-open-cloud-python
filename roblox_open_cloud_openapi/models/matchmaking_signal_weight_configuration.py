from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.matchmaking_signal_type import MatchmakingSignalType

T = TypeVar("T", bound="MatchmakingSignalWeightConfiguration")


@_attrs_define
class MatchmakingSignalWeightConfiguration:
    """The signal weight configuration for matchmaking.

    Attributes:
        weight (float): Weight of signal.
        signal_type (MatchmakingSignalType): The default signal types matchmaking uses.
    """

    weight: float
    signal_type: MatchmakingSignalType

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        signal_type = self.signal_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "weight": weight,
                "signalType": signal_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight")

        signal_type = MatchmakingSignalType(d.pop("signalType"))

        matchmaking_signal_weight_configuration = cls(
            weight=weight,
            signal_type=signal_type,
        )

        return matchmaking_signal_weight_configuration
