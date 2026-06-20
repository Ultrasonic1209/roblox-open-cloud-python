from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0")


@_attrs_define
class UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0:
    """The desired set of weights for each matchmaking signal.

    Attributes:
        invalid (float | Unset):
        occupancy (float | Unset):
        age (float | Unset):
        language (float | Unset):
        latency (float | Unset):
        preferred_players (float | Unset):
        voice_chat (float | Unset):
        device_type (float | Unset):
        play_history (float | Unset):
        text_chat (float | Unset):
    """

    invalid: float | Unset = UNSET
    occupancy: float | Unset = UNSET
    age: float | Unset = UNSET
    language: float | Unset = UNSET
    latency: float | Unset = UNSET
    preferred_players: float | Unset = UNSET
    voice_chat: float | Unset = UNSET
    device_type: float | Unset = UNSET
    play_history: float | Unset = UNSET
    text_chat: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        invalid = self.invalid

        occupancy = self.occupancy

        age = self.age

        language = self.language

        latency = self.latency

        preferred_players = self.preferred_players

        voice_chat = self.voice_chat

        device_type = self.device_type

        play_history = self.play_history

        text_chat = self.text_chat

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        invalid = d.pop("Invalid", UNSET)

        occupancy = d.pop("Occupancy", UNSET)

        age = d.pop("Age", UNSET)

        language = d.pop("Language", UNSET)

        latency = d.pop("Latency", UNSET)

        preferred_players = d.pop("PreferredPlayers", UNSET)

        voice_chat = d.pop("VoiceChat", UNSET)

        device_type = d.pop("DeviceType", UNSET)

        play_history = d.pop("PlayHistory", UNSET)

        text_chat = d.pop("TextChat", UNSET)

        update_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 = cls(
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

        return update_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0
