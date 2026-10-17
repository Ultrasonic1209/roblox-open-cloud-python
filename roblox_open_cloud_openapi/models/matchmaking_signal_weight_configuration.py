from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.matchmaking_signal_type import MatchmakingSignalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchmakingSignalWeightConfiguration")


@_attrs_define
class MatchmakingSignalWeightConfiguration:
    """The signal weight configuration for matchmaking.

    Attributes:
        weight (float | Unset): Weight of signal.
        signal_type (MatchmakingSignalType | Unset): The default signal types matchmaking uses.
    """

    weight: float | Unset = UNSET
    signal_type: MatchmakingSignalType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        signal_type: str | Unset = UNSET
        if not isinstance(self.signal_type, Unset):
            signal_type = self.signal_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if signal_type is not UNSET:
            field_dict["signalType"] = signal_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight", UNSET)

        _signal_type = d.pop("signalType", UNSET)
        signal_type: MatchmakingSignalType | Unset
        if isinstance(_signal_type, Unset):
            signal_type = UNSET
        else:
            signal_type = MatchmakingSignalType(_signal_type)

        matchmaking_signal_weight_configuration = cls(
            weight=weight,
            signal_type=signal_type,
        )

        return matchmaking_signal_weight_configuration
