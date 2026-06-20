from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableEntryCountResponse")


@_attrs_define
class RobloxLocalizationTablesApiGetTableEntryCountResponse:
    """
    Attributes:
        id (UUID | Unset):
        entry_count (int | Unset):
    """

    id: UUID | Unset = UNSET
    entry_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        entry_count = self.entry_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if entry_count is not UNSET:
            field_dict["entryCount"] = entry_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        entry_count = d.pop("entryCount", UNSET)

        roblox_localization_tables_api_get_table_entry_count_response = cls(
            id=id,
            entry_count=entry_count,
        )

        return roblox_localization_tables_api_get_table_entry_count_response
