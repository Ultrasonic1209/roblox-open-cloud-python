from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.private_servers_api_game_server_response import PrivateServersApiGameServerResponse


T = TypeVar("T", bound="GetPrivateServerListResponse")


@_attrs_define
class GetPrivateServerListResponse:
    """
    Attributes:
        data (list[PrivateServersApiGameServerResponse] | None | Unset):
        previous_page_cursor (None | str | Unset):
        next_page_cursor (None | str | Unset):
        game_join_restricted (bool | Unset):
    """

    data: list[PrivateServersApiGameServerResponse] | None | Unset = UNSET
    previous_page_cursor: None | str | Unset = UNSET
    next_page_cursor: None | str | Unset = UNSET
    game_join_restricted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        previous_page_cursor: None | str | Unset
        if isinstance(self.previous_page_cursor, Unset):
            previous_page_cursor = UNSET
        else:
            previous_page_cursor = self.previous_page_cursor

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        game_join_restricted = self.game_join_restricted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if game_join_restricted is not UNSET:
            field_dict["gameJoinRestricted"] = game_join_restricted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_servers_api_game_server_response import PrivateServersApiGameServerResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_data(data: object) -> list[PrivateServersApiGameServerResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = PrivateServersApiGameServerResponse.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrivateServersApiGameServerResponse] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_previous_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_cursor = _parse_previous_page_cursor(d.pop("previousPageCursor", UNSET))

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        game_join_restricted = d.pop("gameJoinRestricted", UNSET)

        get_private_server_list_response = cls(
            data=data,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
            game_join_restricted=game_join_restricted,
        )

        return get_private_server_list_response
