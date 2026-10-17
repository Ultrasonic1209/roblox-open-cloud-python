from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cursor_paging_direction import CursorPagingDirection
from ..models.transaction_records_api_sort_order import TransactionRecordsApiSortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="Int64ExclusiveStartKeyCursor")


@_attrs_define
class Int64ExclusiveStartKeyCursor:
    """
    Attributes:
        key (int | Unset):
        sort_order (TransactionRecordsApiSortOrder | Unset):
        paging_direction (CursorPagingDirection | Unset):
        page_number (int | Unset):
        discriminator (None | str | Unset):
        count (int | Unset):
    """

    key: int | Unset = UNSET
    sort_order: TransactionRecordsApiSortOrder | Unset = UNSET
    paging_direction: CursorPagingDirection | Unset = UNSET
    page_number: int | Unset = UNSET
    discriminator: None | str | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        paging_direction: str | Unset = UNSET
        if not isinstance(self.paging_direction, Unset):
            paging_direction = self.paging_direction.value

        page_number = self.page_number

        discriminator: None | str | Unset
        if isinstance(self.discriminator, Unset):
            discriminator = UNSET
        else:
            discriminator = self.discriminator

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if paging_direction is not UNSET:
            field_dict["pagingDirection"] = paging_direction
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: TransactionRecordsApiSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = TransactionRecordsApiSortOrder(_sort_order)

        _paging_direction = d.pop("pagingDirection", UNSET)
        paging_direction: CursorPagingDirection | Unset
        if isinstance(_paging_direction, Unset):
            paging_direction = UNSET
        else:
            paging_direction = CursorPagingDirection(_paging_direction)

        page_number = d.pop("pageNumber", UNSET)

        def _parse_discriminator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discriminator = _parse_discriminator(d.pop("discriminator", UNSET))

        count = d.pop("count", UNSET)

        int_64_exclusive_start_key_cursor = cls(
            key=key,
            sort_order=sort_order,
            paging_direction=paging_direction,
            page_number=page_number,
            discriminator=discriminator,
            count=count,
        )

        return int_64_exclusive_start_key_cursor
