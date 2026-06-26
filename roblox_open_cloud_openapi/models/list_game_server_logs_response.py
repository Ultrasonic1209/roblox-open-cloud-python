from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_server_log import GameServerLog


T = TypeVar("T", bound="ListGameServerLogsResponse")


@_attrs_define
class ListGameServerLogsResponse:
    """Response model for listing game servers.

    Attributes:
        game_server_logs (list[GameServerLog] | None | Unset): The GameServers from the specified PlaceVersion.
        next_page_token (None | str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    game_server_logs: list[GameServerLog] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_server_logs: list[dict[str, Any]] | None | Unset
        if isinstance(self.game_server_logs, Unset):
            game_server_logs = UNSET
        elif isinstance(self.game_server_logs, list):
            game_server_logs = []
            for game_server_logs_type_0_item_data in self.game_server_logs:
                game_server_logs_type_0_item = game_server_logs_type_0_item_data.to_dict()
                game_server_logs.append(game_server_logs_type_0_item)

        else:
            game_server_logs = self.game_server_logs

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_server_logs is not UNSET:
            field_dict["gameServerLogs"] = game_server_logs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_server_log import GameServerLog

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_game_server_logs(data: object) -> list[GameServerLog] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                game_server_logs_type_0 = []
                _game_server_logs_type_0 = data
                for game_server_logs_type_0_item_data in _game_server_logs_type_0:
                    game_server_logs_type_0_item = GameServerLog.from_dict(game_server_logs_type_0_item_data)

                    game_server_logs_type_0.append(game_server_logs_type_0_item)

                return game_server_logs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GameServerLog] | None | Unset, data)

        game_server_logs = _parse_game_server_logs(d.pop("gameServerLogs", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        list_game_server_logs_response = cls(
            game_server_logs=game_server_logs,
            next_page_token=next_page_token,
        )

        return list_game_server_logs_response
