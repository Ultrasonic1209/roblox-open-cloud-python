from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

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
        id (None | str | Unset): The id of the scoring configuration.
        name (None | str | Unset): The name of the scoring configuration. It needs to be unique within a universe.
        signal_weights (MatchmakingScoringConfigurationSignalWeightsType0 | None | Unset): The signal weights for the
            scoring configuration.
        custom_signals (MatchmakingScoringConfigurationCustomSignalsType0 | None | Unset): The custom signals part of
            this place's scoring configuration.
        created_time (datetime.datetime | Unset): The scoring configuration's created time.
        updated_time (datetime.datetime | Unset): The scoring configuration's updated time.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    signal_weights: MatchmakingScoringConfigurationSignalWeightsType0 | None | Unset = UNSET
    custom_signals: MatchmakingScoringConfigurationCustomSignalsType0 | None | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.matchmaking_scoring_configuration_custom_signals_type_0 import (
            MatchmakingScoringConfigurationCustomSignalsType0,
        )
        from ..models.matchmaking_scoring_configuration_signal_weights_type_0 import (
            MatchmakingScoringConfigurationSignalWeightsType0,
        )

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        signal_weights: dict[str, Any] | None | Unset
        if isinstance(self.signal_weights, Unset):
            signal_weights = UNSET
        elif isinstance(self.signal_weights, MatchmakingScoringConfigurationSignalWeightsType0):
            signal_weights = self.signal_weights.to_dict()
        else:
            signal_weights = self.signal_weights

        custom_signals: dict[str, Any] | None | Unset
        if isinstance(self.custom_signals, Unset):
            custom_signals = UNSET
        elif isinstance(self.custom_signals, MatchmakingScoringConfigurationCustomSignalsType0):
            custom_signals = self.custom_signals.to_dict()
        else:
            custom_signals = self.custom_signals

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if signal_weights is not UNSET:
            field_dict["signalWeights"] = signal_weights
        if custom_signals is not UNSET:
            field_dict["customSignals"] = custom_signals
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_scoring_configuration_custom_signals_type_0 import (
            MatchmakingScoringConfigurationCustomSignalsType0,
        )
        from ..models.matchmaking_scoring_configuration_signal_weights_type_0 import (
            MatchmakingScoringConfigurationSignalWeightsType0,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_signal_weights(data: object) -> MatchmakingScoringConfigurationSignalWeightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signal_weights_type_0 = MatchmakingScoringConfigurationSignalWeightsType0.from_dict(data)

                return signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchmakingScoringConfigurationSignalWeightsType0 | None | Unset, data)

        signal_weights = _parse_signal_weights(d.pop("signalWeights", UNSET))

        def _parse_custom_signals(data: object) -> MatchmakingScoringConfigurationCustomSignalsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_signals_type_0 = MatchmakingScoringConfigurationCustomSignalsType0.from_dict(data)

                return custom_signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchmakingScoringConfigurationCustomSignalsType0 | None | Unset, data)

        custom_signals = _parse_custom_signals(d.pop("customSignals", UNSET))

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = datetime.datetime.fromisoformat(_updated_time)

        matchmaking_scoring_configuration = cls(
            id=id,
            name=name,
            signal_weights=signal_weights,
            custom_signals=custom_signals,
            created_time=created_time,
            updated_time=updated_time,
        )

        return matchmaking_scoring_configuration
