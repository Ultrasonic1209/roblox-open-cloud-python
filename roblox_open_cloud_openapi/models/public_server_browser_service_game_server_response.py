from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.ping_signal_level import PingSignalLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_server_player_response import GameServerPlayerResponse
    from ..models.verified_badge_user_response import VerifiedBadgeUserResponse


T = TypeVar("T", bound="PublicServerBrowserServiceGameServerResponse")


@_attrs_define
class PublicServerBrowserServiceGameServerResponse:
    """
    Attributes:
        id (None | Unset | UUID):
        max_players (int | Unset):
        playing (int | Unset):
        player_tokens (list[str] | None | Unset):
        players (list[GameServerPlayerResponse] | None | Unset):
        fps (float | None | Unset):
        ping (int | None | Unset):
        language_match_count (int | None | Unset):
        ping_signal_level (None | PingSignalLevel | Unset):
        friend_count (int | None | Unset):
        name (None | str | Unset):
        vip_server_id (int | None | Unset):
        access_code (None | Unset | UUID):
        owner (None | Unset | VerifiedBadgeUserResponse):
    """

    id: None | Unset | UUID = UNSET
    max_players: int | Unset = UNSET
    playing: int | Unset = UNSET
    player_tokens: list[str] | None | Unset = UNSET
    players: list[GameServerPlayerResponse] | None | Unset = UNSET
    fps: float | None | Unset = UNSET
    ping: int | None | Unset = UNSET
    language_match_count: int | None | Unset = UNSET
    ping_signal_level: None | PingSignalLevel | Unset = UNSET
    friend_count: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    vip_server_id: int | None | Unset = UNSET
    access_code: None | Unset | UUID = UNSET
    owner: None | Unset | VerifiedBadgeUserResponse = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.verified_badge_user_response import VerifiedBadgeUserResponse  # noqa: PLC0415

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        max_players = self.max_players

        playing = self.playing

        player_tokens: list[str] | None | Unset
        if isinstance(self.player_tokens, Unset):
            player_tokens = UNSET
        elif isinstance(self.player_tokens, list):
            player_tokens = self.player_tokens

        else:
            player_tokens = self.player_tokens

        players: list[dict[str, Any]] | None | Unset
        if isinstance(self.players, Unset):
            players = UNSET
        elif isinstance(self.players, list):
            players = []
            for players_type_0_item_data in self.players:
                players_type_0_item = players_type_0_item_data.to_dict()
                players.append(players_type_0_item)

        else:
            players = self.players

        fps: float | None | Unset
        if isinstance(self.fps, Unset):
            fps = UNSET
        else:
            fps = self.fps

        ping: int | None | Unset
        if isinstance(self.ping, Unset):
            ping = UNSET
        else:
            ping = self.ping

        language_match_count: int | None | Unset
        if isinstance(self.language_match_count, Unset):
            language_match_count = UNSET
        else:
            language_match_count = self.language_match_count

        ping_signal_level: None | str | Unset
        if isinstance(self.ping_signal_level, Unset):
            ping_signal_level = UNSET
        elif isinstance(self.ping_signal_level, PingSignalLevel):
            ping_signal_level = self.ping_signal_level.value
        else:
            ping_signal_level = self.ping_signal_level

        friend_count: int | None | Unset
        if isinstance(self.friend_count, Unset):
            friend_count = UNSET
        else:
            friend_count = self.friend_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vip_server_id: int | None | Unset
        if isinstance(self.vip_server_id, Unset):
            vip_server_id = UNSET
        else:
            vip_server_id = self.vip_server_id

        access_code: None | str | Unset
        if isinstance(self.access_code, Unset):
            access_code = UNSET
        elif isinstance(self.access_code, UUID):
            access_code = str(self.access_code)
        else:
            access_code = self.access_code

        owner: dict[str, Any] | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        elif isinstance(self.owner, VerifiedBadgeUserResponse):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if max_players is not UNSET:
            field_dict["maxPlayers"] = max_players
        if playing is not UNSET:
            field_dict["playing"] = playing
        if player_tokens is not UNSET:
            field_dict["playerTokens"] = player_tokens
        if players is not UNSET:
            field_dict["players"] = players
        if fps is not UNSET:
            field_dict["fps"] = fps
        if ping is not UNSET:
            field_dict["ping"] = ping
        if language_match_count is not UNSET:
            field_dict["languageMatchCount"] = language_match_count
        if ping_signal_level is not UNSET:
            field_dict["pingSignalLevel"] = ping_signal_level
        if friend_count is not UNSET:
            field_dict["friendCount"] = friend_count
        if name is not UNSET:
            field_dict["name"] = name
        if vip_server_id is not UNSET:
            field_dict["vipServerId"] = vip_server_id
        if access_code is not UNSET:
            field_dict["accessCode"] = access_code
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_server_player_response import GameServerPlayerResponse  # noqa: PLC0415
        from ..models.verified_badge_user_response import VerifiedBadgeUserResponse  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        max_players = d.pop("maxPlayers", UNSET)

        playing = d.pop("playing", UNSET)

        def _parse_player_tokens(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_tokens_type_0 = cast(list[str], data)

                return player_tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        player_tokens = _parse_player_tokens(d.pop("playerTokens", UNSET))

        def _parse_players(data: object) -> list[GameServerPlayerResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                players_type_0 = []
                _players_type_0 = data
                for players_type_0_item_data in _players_type_0:
                    players_type_0_item = GameServerPlayerResponse.from_dict(players_type_0_item_data)

                    players_type_0.append(players_type_0_item)

                return players_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GameServerPlayerResponse] | None | Unset, data)

        players = _parse_players(d.pop("players", UNSET))

        def _parse_fps(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fps = _parse_fps(d.pop("fps", UNSET))

        def _parse_ping(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ping = _parse_ping(d.pop("ping", UNSET))

        def _parse_language_match_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        language_match_count = _parse_language_match_count(d.pop("languageMatchCount", UNSET))

        def _parse_ping_signal_level(data: object) -> None | PingSignalLevel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ping_signal_level_type_1 = PingSignalLevel(data)

                return ping_signal_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PingSignalLevel | Unset, data)

        ping_signal_level = _parse_ping_signal_level(d.pop("pingSignalLevel", UNSET))

        def _parse_friend_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        friend_count = _parse_friend_count(d.pop("friendCount", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_vip_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vip_server_id = _parse_vip_server_id(d.pop("vipServerId", UNSET))

        def _parse_access_code(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_code_type_0 = UUID(data)

                return access_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        access_code = _parse_access_code(d.pop("accessCode", UNSET))

        def _parse_owner(data: object) -> None | Unset | VerifiedBadgeUserResponse:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_type_1 = VerifiedBadgeUserResponse.from_dict(data)

                return owner_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VerifiedBadgeUserResponse, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        public_server_browser_service_game_server_response = cls(
            id=id,
            max_players=max_players,
            playing=playing,
            player_tokens=player_tokens,
            players=players,
            fps=fps,
            ping=ping,
            language_match_count=language_match_count,
            ping_signal_level=ping_signal_level,
            friend_count=friend_count,
            name=name,
            vip_server_id=vip_server_id,
            access_code=access_code,
            owner=owner,
        )

        return public_server_browser_service_game_server_response
