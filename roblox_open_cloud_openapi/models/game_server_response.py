from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.private_server_player_response import PrivateServerPlayerResponse
    from ..models.verified_badge_user_response import VerifiedBadgeUserResponse


T = TypeVar("T", bound="GameServerResponse")


@_attrs_define
class GameServerResponse:
    """
    Attributes:
        id (None | Unset | UUID):
        max_players (int | Unset):
        playing (int | Unset):
        player_tokens (list[str] | None | Unset):
        players (list[PrivateServerPlayerResponse] | None | Unset):
        fps (float | Unset):
        ping (int | Unset):
        name (None | str | Unset):
        vip_server_id (int | None | Unset):
        access_code (None | Unset | UUID):
        owner (None | Unset | VerifiedBadgeUserResponse):
    """

    id: None | Unset | UUID = UNSET
    max_players: int | Unset = UNSET
    playing: int | Unset = UNSET
    player_tokens: list[str] | None | Unset = UNSET
    players: list[PrivateServerPlayerResponse] | None | Unset = UNSET
    fps: float | Unset = UNSET
    ping: int | Unset = UNSET
    name: None | str | Unset = UNSET
    vip_server_id: int | None | Unset = UNSET
    access_code: None | Unset | UUID = UNSET
    owner: None | Unset | VerifiedBadgeUserResponse = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.verified_badge_user_response import VerifiedBadgeUserResponse

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

        fps = self.fps

        ping = self.ping

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
        from ..models.private_server_player_response import PrivateServerPlayerResponse
        from ..models.verified_badge_user_response import VerifiedBadgeUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

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

        def _parse_players(data: object) -> list[PrivateServerPlayerResponse] | None | Unset:
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
                    players_type_0_item = PrivateServerPlayerResponse.from_dict(players_type_0_item_data)

                    players_type_0.append(players_type_0_item)

                return players_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrivateServerPlayerResponse] | None | Unset, data)

        players = _parse_players(d.pop("players", UNSET))

        fps = d.pop("fps", UNSET)

        ping = d.pop("ping", UNSET)

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

        game_server_response = cls(
            id=id,
            max_players=max_players,
            playing=playing,
            player_tokens=player_tokens,
            players=players,
            fps=fps,
            ping=ping,
            name=name,
            vip_server_id=vip_server_id,
            access_code=access_code,
            owner=owner,
        )

        return game_server_response
