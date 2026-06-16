from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_game_server_player_response import RobloxGamesApiGameServerPlayerResponse
    from ..models.roblox_games_api_models_response_verified_badge_user_response import (
        RobloxGamesApiModelsResponseVerifiedBadgeUserResponse,
    )


T = TypeVar("T", bound="RobloxWebResponsesGamesGameServerResponse")


@_attrs_define
class RobloxWebResponsesGamesGameServerResponse:
    """Game server list response model.

    Attributes:
        id (UUID | Unset): The game server ID.
        max_players (int | Unset): The max number of players allowed to enter the server at the same time.
        playing (int | Unset): The number of players actively in the server.
        player_tokens (list[str] | Unset): The thumbnail tokens for all the players in the server.
        players (list[RobloxGamesApiGameServerPlayerResponse] | Unset): The players in the server.
        fps (float | Unset): The current frames per second the server is running at.
        ping (int | Unset): The game server ping time (measured in milliseconds).
        name (str | Unset): The name of the private server.
        vip_server_id (int | Unset): The private server ID.
        access_code (UUID | Unset): The private server access code.
        owner (RobloxGamesApiModelsResponseVerifiedBadgeUserResponse | Unset): A response model specific to multi-get
            user.
    """

    id: UUID | Unset = UNSET
    max_players: int | Unset = UNSET
    playing: int | Unset = UNSET
    player_tokens: list[str] | Unset = UNSET
    players: list[RobloxGamesApiGameServerPlayerResponse] | Unset = UNSET
    fps: float | Unset = UNSET
    ping: int | Unset = UNSET
    name: str | Unset = UNSET
    vip_server_id: int | Unset = UNSET
    access_code: UUID | Unset = UNSET
    owner: RobloxGamesApiModelsResponseVerifiedBadgeUserResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        max_players = self.max_players

        playing = self.playing

        player_tokens: list[str] | Unset = UNSET
        if not isinstance(self.player_tokens, Unset):
            player_tokens = self.player_tokens

        players: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        fps = self.fps

        ping = self.ping

        name = self.name

        vip_server_id = self.vip_server_id

        access_code: str | Unset = UNSET
        if not isinstance(self.access_code, Unset):
            access_code = str(self.access_code)

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

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
        from ..models.roblox_games_api_game_server_player_response import RobloxGamesApiGameServerPlayerResponse
        from ..models.roblox_games_api_models_response_verified_badge_user_response import (
            RobloxGamesApiModelsResponseVerifiedBadgeUserResponse,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        max_players = d.pop("maxPlayers", UNSET)

        playing = d.pop("playing", UNSET)

        player_tokens = cast(list[str], d.pop("playerTokens", UNSET))

        _players = d.pop("players", UNSET)
        players: list[RobloxGamesApiGameServerPlayerResponse] | Unset = UNSET
        if _players is not UNSET:
            players = []
            for players_item_data in _players:
                players_item = RobloxGamesApiGameServerPlayerResponse.from_dict(players_item_data)

                players.append(players_item)

        fps = d.pop("fps", UNSET)

        ping = d.pop("ping", UNSET)

        name = d.pop("name", UNSET)

        vip_server_id = d.pop("vipServerId", UNSET)

        _access_code = d.pop("accessCode", UNSET)
        access_code: UUID | Unset
        if isinstance(_access_code, Unset):
            access_code = UNSET
        else:
            access_code = UUID(_access_code)

        _owner = d.pop("owner", UNSET)
        owner: RobloxGamesApiModelsResponseVerifiedBadgeUserResponse | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxGamesApiModelsResponseVerifiedBadgeUserResponse.from_dict(_owner)

        roblox_web_responses_games_game_server_response = cls(
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

        return roblox_web_responses_games_game_server_response
