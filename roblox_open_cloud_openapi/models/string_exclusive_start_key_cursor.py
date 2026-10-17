from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cursor_paging_direction import CursorPagingDirection
from ..models.private_servers_api_sort_order import PrivateServersApiSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="StringExclusiveStartKeyCursor")


@_attrs_define
class StringExclusiveStartKeyCursor:
    """
    Attributes:
        discriminator (None | str | Unset):
        count (int | Unset):
        key (None | str | Unset):
        sort_order (PrivateServersApiSortOrder | Unset):
        paging_direction (CursorPagingDirection | Unset):
        page_number (int | Unset):
    """

    discriminator: None | str | Unset = UNSET
    count: int | Unset = UNSET
    key: None | str | Unset = UNSET
    sort_order: PrivateServersApiSortOrder | Unset = UNSET
    paging_direction: CursorPagingDirection | Unset = UNSET
    page_number: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        discriminator: None | str | Unset
        if isinstance(self.discriminator, Unset):
            discriminator = UNSET
        else:
            discriminator = self.discriminator

        count = self.count

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        paging_direction: str | Unset = UNSET
        if not isinstance(self.paging_direction, Unset):
            paging_direction = self.paging_direction.value

        page_number = self.page_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator
        if count is not UNSET:
            field_dict["count"] = count
        if key is not UNSET:
            field_dict["key"] = key
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if paging_direction is not UNSET:
            field_dict["pagingDirection"] = paging_direction
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_discriminator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discriminator = _parse_discriminator(d.pop("discriminator", UNSET))

        count = d.pop("count", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: PrivateServersApiSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = PrivateServersApiSortOrder(_sort_order)

        _paging_direction = d.pop("pagingDirection", UNSET)
        paging_direction: CursorPagingDirection | Unset
        if isinstance(_paging_direction, Unset):
            paging_direction = UNSET
        else:
            paging_direction = CursorPagingDirection(_paging_direction)

        page_number = d.pop("pageNumber", UNSET)

        string_exclusive_start_key_cursor = cls(
            discriminator=discriminator,
            count=count,
            key=key,
            sort_order=sort_order,
            paging_direction=paging_direction,
            page_number=page_number,
        )

        return string_exclusive_start_key_cursor
