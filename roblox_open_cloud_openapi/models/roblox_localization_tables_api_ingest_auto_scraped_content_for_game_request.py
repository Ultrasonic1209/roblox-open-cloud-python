from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_auto_scrape_entry import RobloxLocalizationTablesApiAutoScrapeEntry
    from ..models.roblox_localization_tables_api_ingest_content_metadata import (
        RobloxLocalizationTablesApiIngestContentMetadata,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest")


@_attrs_define
class RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest:
    """An ingest content request to IngestAutoScrapedContentForGame.

    Attributes:
        entries (list[RobloxLocalizationTablesApiAutoScrapeEntry] | Unset): The entries of an ingest content request.
        metadata (RobloxLocalizationTablesApiIngestContentMetadata | Unset): The metadata of an ingest content request.
    """

    entries: list[RobloxLocalizationTablesApiAutoScrapeEntry] | Unset = UNSET
    metadata: RobloxLocalizationTablesApiIngestContentMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_auto_scrape_entry import RobloxLocalizationTablesApiAutoScrapeEntry
        from ..models.roblox_localization_tables_api_ingest_content_metadata import (
            RobloxLocalizationTablesApiIngestContentMetadata,
        )

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiAutoScrapeEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiAutoScrapeEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: RobloxLocalizationTablesApiIngestContentMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RobloxLocalizationTablesApiIngestContentMetadata.from_dict(_metadata)

        roblox_localization_tables_api_ingest_auto_scraped_content_for_game_request = cls(
            entries=entries,
            metadata=metadata,
        )

        return roblox_localization_tables_api_ingest_auto_scraped_content_for_game_request
