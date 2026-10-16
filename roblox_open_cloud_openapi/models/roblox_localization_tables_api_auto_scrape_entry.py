from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_auto_scrape_entry_metadata import (
        RobloxLocalizationTablesApiAutoScrapeEntryMetadata,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiAutoScrapeEntry")


@_attrs_define
class RobloxLocalizationTablesApiAutoScrapeEntry:
    """
    Attributes:
        context (str | Unset):
        source (str | Unset):
        screenshot (str | Unset):
        meta (RobloxLocalizationTablesApiAutoScrapeEntryMetadata | Unset):
    """

    context: str | Unset = UNSET
    source: str | Unset = UNSET
    screenshot: str | Unset = UNSET
    meta: RobloxLocalizationTablesApiAutoScrapeEntryMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        source = self.source

        screenshot = self.screenshot

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if source is not UNSET:
            field_dict["source"] = source
        if screenshot is not UNSET:
            field_dict["screenshot"] = screenshot
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_auto_scrape_entry_metadata import (
            RobloxLocalizationTablesApiAutoScrapeEntryMetadata,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        context = d.pop("context", UNSET)

        source = d.pop("source", UNSET)

        screenshot = d.pop("screenshot", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: RobloxLocalizationTablesApiAutoScrapeEntryMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = RobloxLocalizationTablesApiAutoScrapeEntryMetadata.from_dict(_meta)

        roblox_localization_tables_api_auto_scrape_entry = cls(
            context=context,
            source=source,
            screenshot=screenshot,
            meta=meta,
        )

        return roblox_localization_tables_api_auto_scrape_entry
