from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_event_response import GameEventResponse


T = TypeVar("T", bound="PaginatedGameEventsResponse")


@_attrs_define
class PaginatedGameEventsResponse:
    """Paginated response for v3 LIST. Page tokens are null at the collection boundaries.

    Attributes:
        game_events (list[GameEventResponse] | None | Unset):
        next_page_token (None | str | Unset):
        previous_page_token (None | str | Unset):
    """

    game_events: list[GameEventResponse] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET
    previous_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_events: list[dict[str, Any]] | None | Unset
        if isinstance(self.game_events, Unset):
            game_events = UNSET
        elif isinstance(self.game_events, list):
            game_events = []
            for game_events_type_0_item_data in self.game_events:
                game_events_type_0_item = game_events_type_0_item_data.to_dict()
                game_events.append(game_events_type_0_item)

        else:
            game_events = self.game_events

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_events is not UNSET:
            field_dict["gameEvents"] = game_events
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if previous_page_token is not UNSET:
            field_dict["previousPageToken"] = previous_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_event_response import GameEventResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_game_events(data: object) -> list[GameEventResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                game_events_type_0 = []
                _game_events_type_0 = data
                for game_events_type_0_item_data in _game_events_type_0:
                    game_events_type_0_item = GameEventResponse.from_dict(game_events_type_0_item_data)

                    game_events_type_0.append(game_events_type_0_item)

                return game_events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GameEventResponse] | None | Unset, data)

        game_events = _parse_game_events(d.pop("gameEvents", UNSET))

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

        paginated_game_events_response = cls(
            game_events=game_events,
            next_page_token=next_page_token,
            previous_page_token=previous_page_token,
        )

        return paginated_game_events_response
