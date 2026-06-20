from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiRaiseEventForAutoScrapedEntriesCleanupRequest")


@_attrs_define
class RobloxLocalizationTablesApiRaiseEventForAutoScrapedEntriesCleanupRequest:
    """
    Attributes:
        max_age_for_flush (str | Unset): The time range to remove entries from. Following ISO 8601 Durations format
    """

    max_age_for_flush: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_age_for_flush = self.max_age_for_flush

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_age_for_flush is not UNSET:
            field_dict["maxAgeForFlush"] = max_age_for_flush

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        max_age_for_flush = d.pop("maxAgeForFlush", UNSET)

        roblox_localization_tables_api_raise_event_for_auto_scraped_entries_cleanup_request = cls(
            max_age_for_flush=max_age_for_flush,
        )

        return roblox_localization_tables_api_raise_event_for_auto_scraped_entries_cleanup_request
