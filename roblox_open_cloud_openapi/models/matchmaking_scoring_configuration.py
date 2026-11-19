from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.matchmaking_scoring_configuration_custom_signals_type_0 import (
        MatchmakingScoringConfigurationCustomSignalsType0,
    )
    from ..models.matchmaking_scoring_configuration_signal_weights_type_0 import (
        MatchmakingScoringConfigurationSignalWeightsType0,
    )


T = TypeVar("T", bound="MatchmakingScoringConfiguration")


@_attrs_define
class MatchmakingScoringConfiguration:
    """The custom scoring configuration for matchmaking.

    Attributes:
        id (None | str): The id of the scoring configuration.
        name (None | str): The name of the scoring configuration. It needs to be unique within a universe.
        signal_weights (MatchmakingScoringConfigurationSignalWeightsType0 | None): The signal weights for the scoring
            configuration.
        custom_signals (MatchmakingScoringConfigurationCustomSignalsType0 | None): The custom signals part of this
            place's scoring configuration.
        created_time (datetime.datetime): The scoring configuration's created time.
        updated_time (datetime.datetime): The scoring configuration's updated time.
    """

    id: None | str
    name: None | str
    signal_weights: MatchmakingScoringConfigurationSignalWeightsType0 | None
    custom_signals: MatchmakingScoringConfigurationCustomSignalsType0 | None
    created_time: datetime.datetime
    updated_time: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.matchmaking_scoring_configuration_custom_signals_type_0 import (
            MatchmakingScoringConfigurationCustomSignalsType0,  # noqa: PLC0415
        )
        from ..models.matchmaking_scoring_configuration_signal_weights_type_0 import (
            MatchmakingScoringConfigurationSignalWeightsType0,  # noqa: PLC0415
        )

        id: None | str
        id = self.id

        name: None | str
        name = self.name

        signal_weights: dict[str, Any] | None
        if isinstance(self.signal_weights, MatchmakingScoringConfigurationSignalWeightsType0):
            signal_weights = self.signal_weights.to_dict()
        else:
            signal_weights = self.signal_weights

        custom_signals: dict[str, Any] | None
        if isinstance(self.custom_signals, MatchmakingScoringConfigurationCustomSignalsType0):
            custom_signals = self.custom_signals.to_dict()
        else:
            custom_signals = self.custom_signals

        created_time = self.created_time.isoformat()

        updated_time = self.updated_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "signalWeights": signal_weights,
                "customSignals": custom_signals,
                "createdTime": created_time,
                "updatedTime": updated_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration_custom_signals_type_0 import (
            MatchmakingScoringConfigurationCustomSignalsType0,  # noqa: PLC0415
        )
        from ..models.matchmaking_scoring_configuration_signal_weights_type_0 import (
            MatchmakingScoringConfigurationSignalWeightsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_signal_weights(data: object) -> MatchmakingScoringConfigurationSignalWeightsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signal_weights_type_0 = MatchmakingScoringConfigurationSignalWeightsType0.from_dict(data)

                return signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchmakingScoringConfigurationSignalWeightsType0 | None, data)

        signal_weights = _parse_signal_weights(d.pop("signalWeights"))

        def _parse_custom_signals(data: object) -> MatchmakingScoringConfigurationCustomSignalsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_signals_type_0 = MatchmakingScoringConfigurationCustomSignalsType0.from_dict(data)

                return custom_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchmakingScoringConfigurationCustomSignalsType0 | None, data)

        custom_signals = _parse_custom_signals(d.pop("customSignals"))

        created_time = datetime.datetime.fromisoformat(d.pop("createdTime"))

        updated_time = datetime.datetime.fromisoformat(d.pop("updatedTime"))

        matchmaking_scoring_configuration = cls(
            id=id,
            name=name,
            signal_weights=signal_weights,
            custom_signals=custom_signals,
            created_time=created_time,
            updated_time=updated_time,
        )

        return matchmaking_scoring_configuration
