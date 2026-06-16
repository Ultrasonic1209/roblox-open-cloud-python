from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_management_service_game_server import ServerManagementServiceGameServer


T = TypeVar("T", bound="ServerManagementServiceListGameServersResponse")


@_attrs_define
class ServerManagementServiceListGameServersResponse:
    """Response model for listing game servers.

    Attributes:
        game_servers (list[ServerManagementServiceGameServer] | None | Unset): The GameServers from the specified
            PlaceVersion.
        next_page_token (None | str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
        previous_page_token (None | str | Unset): A token that you can send as a `pageToken` parameter to retrieve the
            previous
            page (reverse cursor). If this field is omitted, there are no prior pages.
        total_count (int | None | Unset): Total number of game servers that match the filter (across all pages).
            Omitted if the backend does not provide a total count.
    """

    game_servers: list[ServerManagementServiceGameServer] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    previous_page_token: None | str | Unset = UNSET
    total_count: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_servers: list[dict[str, Any]] | None | Unset
        if isinstance(self.game_servers, Unset):
            game_servers = UNSET
        elif isinstance(self.game_servers, list):
            game_servers = []
            for game_servers_type_0_item_data in self.game_servers:
                game_servers_type_0_item = game_servers_type_0_item_data.to_dict()
                game_servers.append(game_servers_type_0_item)

        else:
            game_servers = self.game_servers

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        previous_page_token: None | str | Unset
        if isinstance(self.previous_page_token, Unset):
            previous_page_token = UNSET
        else:
            previous_page_token = self.previous_page_token

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_servers is not UNSET:
            field_dict["gameServers"] = game_servers
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if previous_page_token is not UNSET:
            field_dict["previousPageToken"] = previous_page_token
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_management_service_game_server import ServerManagementServiceGameServer

        d = dict(src_dict)

        def _parse_game_servers(data: object) -> list[ServerManagementServiceGameServer] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                game_servers_type_0 = []
                _game_servers_type_0 = data
                for game_servers_type_0_item_data in _game_servers_type_0:
                    game_servers_type_0_item = ServerManagementServiceGameServer.from_dict(
                        game_servers_type_0_item_data
                    )

                    game_servers_type_0.append(game_servers_type_0_item)

                return game_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ServerManagementServiceGameServer] | None | Unset, data)

        game_servers = _parse_game_servers(d.pop("gameServers", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_previous_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_token = _parse_previous_page_token(d.pop("previousPageToken", UNSET))

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("totalCount", UNSET))

        server_management_service_list_game_servers_response = cls(
            game_servers=game_servers,
            next_page_token=next_page_token,
            previous_page_token=previous_page_token,
            total_count=total_count,
        )

        return server_management_service_list_game_servers_response
