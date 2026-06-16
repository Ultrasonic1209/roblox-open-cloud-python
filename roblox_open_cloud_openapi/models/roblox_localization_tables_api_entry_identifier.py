from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_entry_identifier_entry_format import (
    RobloxLocalizationTablesApiEntryIdentifierEntryFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryIdentifier")


@_attrs_define
class RobloxLocalizationTablesApiEntryIdentifier:
    """
    Attributes:
        key (str | Unset):
        context (str | Unset):
        source (str | Unset):
        entry_format (RobloxLocalizationTablesApiEntryIdentifierEntryFormat | Unset):
    """

    key: str | Unset = UNSET
    context: str | Unset = UNSET
    source: str | Unset = UNSET
    entry_format: RobloxLocalizationTablesApiEntryIdentifierEntryFormat | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        context = self.context

        source = self.source

        entry_format: str | Unset = UNSET
        if not isinstance(self.entry_format, Unset):
            entry_format = self.entry_format.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if context is not UNSET:
            field_dict["context"] = context
        if source is not UNSET:
            field_dict["source"] = source
        if entry_format is not UNSET:
            field_dict["entryFormat"] = entry_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        context = d.pop("context", UNSET)

        source = d.pop("source", UNSET)

        _entry_format = d.pop("entryFormat", UNSET)
        entry_format: RobloxLocalizationTablesApiEntryIdentifierEntryFormat | Unset
        if isinstance(_entry_format, Unset):
            entry_format = UNSET
        else:
            entry_format = RobloxLocalizationTablesApiEntryIdentifierEntryFormat(_entry_format)

        roblox_localization_tables_api_entry_identifier = cls(
            key=key,
            context=context,
            source=source,
            entry_format=entry_format,
        )

        return roblox_localization_tables_api_entry_identifier
