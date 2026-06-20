from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_patch_entry import RobloxLocalizationTablesApiPatchEntry


T = TypeVar("T", bound="RobloxLocalizationTablesApiUpdateTableContentsRequest")


@_attrs_define
class RobloxLocalizationTablesApiUpdateTableContentsRequest:
    """
    Attributes:
        name (str | Unset):
        entries (list[RobloxLocalizationTablesApiPatchEntry] | Unset):
    """

    name: str | Unset = UNSET
    entries: list[RobloxLocalizationTablesApiPatchEntry] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_patch_entry import RobloxLocalizationTablesApiPatchEntry

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiPatchEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiPatchEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        roblox_localization_tables_api_update_table_contents_request = cls(
            name=name,
            entries=entries,
        )

        return roblox_localization_tables_api_update_table_contents_request
