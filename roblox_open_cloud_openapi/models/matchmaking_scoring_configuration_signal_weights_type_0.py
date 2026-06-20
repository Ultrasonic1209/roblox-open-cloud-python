from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_signal_weight_configuration import MatchmakingSignalWeightConfiguration


T = TypeVar("T", bound="MatchmakingScoringConfigurationSignalWeightsType0")


@_attrs_define
class MatchmakingScoringConfigurationSignalWeightsType0:
    """The signal weights for the scoring configuration.

    Attributes:
        invalid (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        occupancy (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        age (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        language (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        latency (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        preferred_players (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for
            matchmaking.
        voice_chat (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        device_type (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        play_history (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
        text_chat (MatchmakingSignalWeightConfiguration | Unset): The signal weight configuration for matchmaking.
    """

    invalid: MatchmakingSignalWeightConfiguration | Unset = UNSET
    occupancy: MatchmakingSignalWeightConfiguration | Unset = UNSET
    age: MatchmakingSignalWeightConfiguration | Unset = UNSET
    language: MatchmakingSignalWeightConfiguration | Unset = UNSET
    latency: MatchmakingSignalWeightConfiguration | Unset = UNSET
    preferred_players: MatchmakingSignalWeightConfiguration | Unset = UNSET
    voice_chat: MatchmakingSignalWeightConfiguration | Unset = UNSET
    device_type: MatchmakingSignalWeightConfiguration | Unset = UNSET
    play_history: MatchmakingSignalWeightConfiguration | Unset = UNSET
    text_chat: MatchmakingSignalWeightConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        invalid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invalid, Unset):
            invalid = self.invalid.to_dict()

        occupancy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = self.occupancy.to_dict()

        age: dict[str, Any] | Unset = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        latency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latency, Unset):
            latency = self.latency.to_dict()

        preferred_players: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preferred_players, Unset):
            preferred_players = self.preferred_players.to_dict()

        voice_chat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voice_chat, Unset):
            voice_chat = self.voice_chat.to_dict()

        device_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.to_dict()

        play_history: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_history, Unset):
            play_history = self.play_history.to_dict()

        text_chat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_chat, Unset):
            text_chat = self.text_chat.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if invalid is not UNSET:
            field_dict["Invalid"] = invalid
        if occupancy is not UNSET:
            field_dict["Occupancy"] = occupancy
        if age is not UNSET:
            field_dict["Age"] = age
        if language is not UNSET:
            field_dict["Language"] = language
        if latency is not UNSET:
            field_dict["Latency"] = latency
        if preferred_players is not UNSET:
            field_dict["PreferredPlayers"] = preferred_players
        if voice_chat is not UNSET:
            field_dict["VoiceChat"] = voice_chat
        if device_type is not UNSET:
            field_dict["DeviceType"] = device_type
        if play_history is not UNSET:
            field_dict["PlayHistory"] = play_history
        if text_chat is not UNSET:
            field_dict["TextChat"] = text_chat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_signal_weight_configuration import MatchmakingSignalWeightConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _invalid = d.pop("Invalid", UNSET)
        invalid: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_invalid, Unset):
            invalid = UNSET
        else:
            invalid = MatchmakingSignalWeightConfiguration.from_dict(_invalid)

        _occupancy = d.pop("Occupancy", UNSET)
        occupancy: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_occupancy, Unset):
            occupancy = UNSET
        else:
            occupancy = MatchmakingSignalWeightConfiguration.from_dict(_occupancy)

        _age = d.pop("Age", UNSET)
        age: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = MatchmakingSignalWeightConfiguration.from_dict(_age)

        _language = d.pop("Language", UNSET)
        language: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = MatchmakingSignalWeightConfiguration.from_dict(_language)

        _latency = d.pop("Latency", UNSET)
        latency: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_latency, Unset):
            latency = UNSET
        else:
            latency = MatchmakingSignalWeightConfiguration.from_dict(_latency)

        _preferred_players = d.pop("PreferredPlayers", UNSET)
        preferred_players: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_preferred_players, Unset):
            preferred_players = UNSET
        else:
            preferred_players = MatchmakingSignalWeightConfiguration.from_dict(_preferred_players)

        _voice_chat = d.pop("VoiceChat", UNSET)
        voice_chat: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_voice_chat, Unset):
            voice_chat = UNSET
        else:
            voice_chat = MatchmakingSignalWeightConfiguration.from_dict(_voice_chat)

        _device_type = d.pop("DeviceType", UNSET)
        device_type: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = MatchmakingSignalWeightConfiguration.from_dict(_device_type)

        _play_history = d.pop("PlayHistory", UNSET)
        play_history: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_play_history, Unset):
            play_history = UNSET
        else:
            play_history = MatchmakingSignalWeightConfiguration.from_dict(_play_history)

        _text_chat = d.pop("TextChat", UNSET)
        text_chat: MatchmakingSignalWeightConfiguration | Unset
        if isinstance(_text_chat, Unset):
            text_chat = UNSET
        else:
            text_chat = MatchmakingSignalWeightConfiguration.from_dict(_text_chat)

        matchmaking_scoring_configuration_signal_weights_type_0 = cls(
            invalid=invalid,
            occupancy=occupancy,
            age=age,
            language=language,
            latency=latency,
            preferred_players=preferred_players,
            voice_chat=voice_chat,
            device_type=device_type,
            play_history=play_history,
            text_chat=text_chat,
        )

        return matchmaking_scoring_configuration_signal_weights_type_0
