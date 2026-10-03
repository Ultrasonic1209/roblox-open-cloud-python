from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_invitation import GroupInvitation


T = TypeVar("T", bound="GroupInvitationCursorPageResponse")


@_attrs_define
class GroupInvitationCursorPageResponse:
    """A page of results using groups-api opaque cursor pagination.

    Attributes:
        data (list[GroupInvitation]): The items in this page.
        next_page_cursor (None | str | Unset): Cursor for the next page, if any.
        previous_page_cursor (None | str | Unset): Cursor for the previous page, if any.
    """

    data: list[GroupInvitation]
    next_page_cursor: None | str | Unset = UNSET
    previous_page_cursor: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        previous_page_cursor: None | str | Unset
        if isinstance(self.previous_page_cursor, Unset):
            previous_page_cursor = UNSET
        else:
            previous_page_cursor = self.previous_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_invitation import GroupInvitation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GroupInvitation.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        def _parse_previous_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_cursor = _parse_previous_page_cursor(d.pop("previousPageCursor", UNSET))

        group_invitation_cursor_page_response = cls(
            data=data,
            next_page_cursor=next_page_cursor,
            previous_page_cursor=previous_page_cursor,
        )

        return group_invitation_cursor_page_response
