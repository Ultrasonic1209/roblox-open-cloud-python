from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MockServerSignalValues")


@_attrs_define
class MockServerSignalValues:
    """Mock server signal values.

    Attributes:
        capacity (int | Unset): The capacity of the mock server.
        occupancy (int | Unset): The occupancy of the mock server.
        has_preferred_players (bool | Unset): If the game has preferred players.
        player_age (int | Unset): The joining player's age.
        server_average_player_age (int | Unset): The server's age for the mock server.
        common_language_players (int | Unset): The number of player's in the mock server that have a common language.
        latency (int | Unset): The latency of the mock server.
        common_device_players (int | Unset): The number of player's in the mock server that have a common device.
        player_play_history (float | Unset): The joining player's play history. The value is a log10 transformation of
            the player's playtime in minutes during last 28 days.
        server_average_play_history (float | Unset): The server's play history for the mock server.
        common_voice_players (int | None | Unset): The number of player's in the mock server that have voice chat
            enabled.
        common_text_chat_players (int | Unset): The number of player's in the mock server that can commonly text chat
            with the joining player.
    """

    capacity: int | Unset = UNSET
    occupancy: int | Unset = UNSET
    has_preferred_players: bool | Unset = UNSET
    player_age: int | Unset = UNSET
    server_average_player_age: int | Unset = UNSET
    common_language_players: int | Unset = UNSET
    latency: int | Unset = UNSET
    common_device_players: int | Unset = UNSET
    player_play_history: float | Unset = UNSET
    server_average_play_history: float | Unset = UNSET
    common_voice_players: int | None | Unset = UNSET
    common_text_chat_players: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        capacity = self.capacity

        occupancy = self.occupancy

        has_preferred_players = self.has_preferred_players

        player_age = self.player_age

        server_average_player_age = self.server_average_player_age

        common_language_players = self.common_language_players

        latency = self.latency

        common_device_players = self.common_device_players

        player_play_history = self.player_play_history

        server_average_play_history = self.server_average_play_history

        common_voice_players: int | None | Unset
        if isinstance(self.common_voice_players, Unset):
            common_voice_players = UNSET
        else:
            common_voice_players = self.common_voice_players

        common_text_chat_players = self.common_text_chat_players

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if has_preferred_players is not UNSET:
            field_dict["hasPreferredPlayers"] = has_preferred_players
        if player_age is not UNSET:
            field_dict["playerAge"] = player_age
        if server_average_player_age is not UNSET:
            field_dict["serverAveragePlayerAge"] = server_average_player_age
        if common_language_players is not UNSET:
            field_dict["commonLanguagePlayers"] = common_language_players
        if latency is not UNSET:
            field_dict["latency"] = latency
        if common_device_players is not UNSET:
            field_dict["commonDevicePlayers"] = common_device_players
        if player_play_history is not UNSET:
            field_dict["playerPlayHistory"] = player_play_history
        if server_average_play_history is not UNSET:
            field_dict["serverAveragePlayHistory"] = server_average_play_history
        if common_voice_players is not UNSET:
            field_dict["commonVoicePlayers"] = common_voice_players
        if common_text_chat_players is not UNSET:
            field_dict["commonTextChatPlayers"] = common_text_chat_players

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        capacity = d.pop("capacity", UNSET)

        occupancy = d.pop("occupancy", UNSET)

        has_preferred_players = d.pop("hasPreferredPlayers", UNSET)

        player_age = d.pop("playerAge", UNSET)

        server_average_player_age = d.pop("serverAveragePlayerAge", UNSET)

        common_language_players = d.pop("commonLanguagePlayers", UNSET)

        latency = d.pop("latency", UNSET)

        common_device_players = d.pop("commonDevicePlayers", UNSET)

        player_play_history = d.pop("playerPlayHistory", UNSET)

        server_average_play_history = d.pop("serverAveragePlayHistory", UNSET)

        def _parse_common_voice_players(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        common_voice_players = _parse_common_voice_players(d.pop("commonVoicePlayers", UNSET))

        common_text_chat_players = d.pop("commonTextChatPlayers", UNSET)

        mock_server_signal_values = cls(
            capacity=capacity,
            occupancy=occupancy,
            has_preferred_players=has_preferred_players,
            player_age=player_age,
            server_average_player_age=server_average_player_age,
            common_language_players=common_language_players,
            latency=latency,
            common_device_players=common_device_players,
            player_play_history=player_play_history,
            server_average_play_history=server_average_play_history,
            common_voice_players=common_voice_players,
            common_text_chat_players=common_text_chat_players,
        )

        return mock_server_signal_values
