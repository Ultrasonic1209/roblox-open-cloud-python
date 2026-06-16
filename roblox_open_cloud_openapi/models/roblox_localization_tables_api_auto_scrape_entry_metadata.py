from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_matched_entry import RobloxLocalizationTablesApiMatchedEntry


T = TypeVar("T", bound="RobloxLocalizationTablesApiAutoScrapeEntryMetadata")


@_attrs_define
class RobloxLocalizationTablesApiAutoScrapeEntryMetadata:
    """
    Attributes:
        text (str | Unset):
        user_id (int | Unset):
        os_platform (str | Unset):
        session_id (UUID | Unset):
        matched_entry (RobloxLocalizationTablesApiMatchedEntry | Unset):
    """

    text: str | Unset = UNSET
    user_id: int | Unset = UNSET
    os_platform: str | Unset = UNSET
    session_id: UUID | Unset = UNSET
    matched_entry: RobloxLocalizationTablesApiMatchedEntry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        user_id = self.user_id

        os_platform = self.os_platform

        session_id: str | Unset = UNSET
        if not isinstance(self.session_id, Unset):
            session_id = str(self.session_id)

        matched_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matched_entry, Unset):
            matched_entry = self.matched_entry.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if os_platform is not UNSET:
            field_dict["osPlatform"] = os_platform
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if matched_entry is not UNSET:
            field_dict["matchedEntry"] = matched_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_matched_entry import RobloxLocalizationTablesApiMatchedEntry

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        user_id = d.pop("userId", UNSET)

        os_platform = d.pop("osPlatform", UNSET)

        _session_id = d.pop("sessionId", UNSET)
        session_id: UUID | Unset
        if isinstance(_session_id, Unset):
            session_id = UNSET
        else:
            session_id = UUID(_session_id)

        _matched_entry = d.pop("matchedEntry", UNSET)
        matched_entry: RobloxLocalizationTablesApiMatchedEntry | Unset
        if isinstance(_matched_entry, Unset):
            matched_entry = UNSET
        else:
            matched_entry = RobloxLocalizationTablesApiMatchedEntry.from_dict(_matched_entry)

        roblox_localization_tables_api_auto_scrape_entry_metadata = cls(
            text=text,
            user_id=user_id,
            os_platform=os_platform,
            session_id=session_id,
            matched_entry=matched_entry,
        )

        return roblox_localization_tables_api_auto_scrape_entry_metadata
