from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_cursor_entry_identifier_sort_order import (
    RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier


T = TypeVar("T", bound="RobloxLocalizationTablesApiCursorEntryIdentifier")


@_attrs_define
class RobloxLocalizationTablesApiCursorEntryIdentifier:
    """A model that contains an entry identifier and an associated cursor for paged lookups.

    Attributes:
        cursor (str | Unset): The location to begin our query.
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        count (int | Unset): The translation history count to get.
        sort_order (RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder | Unset): In which order the data is
            sorted. ['Asc' = 1, 'Desc' = 2]
    """

    cursor: str | Unset = UNSET
    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    count: int | Unset = UNSET
    sort_order: RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        count = self.count

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if count is not UNSET:
            field_dict["count"] = count
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        cursor = d.pop("cursor", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifier.from_dict(_identifier)

        count = d.pop("count", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder(_sort_order)

        roblox_localization_tables_api_cursor_entry_identifier = cls(
            cursor=cursor,
            identifier=identifier,
            count=count,
            sort_order=sort_order,
        )

        return roblox_localization_tables_api_cursor_entry_identifier
