from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
    from ..models.roblox_localization_tables_api_translation_history import (
        RobloxLocalizationTablesApiTranslationHistory,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryTranslationHistoryPaged")


@_attrs_define
class RobloxLocalizationTablesApiEntryTranslationHistoryPaged:
    """
    Attributes:
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        history (list[RobloxLocalizationTablesApiTranslationHistory] | Unset): A batch of TranslationHistory for the
            given entry identifier.
        next_cursor (str | Unset): The cursor to send up on the next request if more history data is required.
    """

    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    history: list[RobloxLocalizationTablesApiTranslationHistory] | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if history is not UNSET:
            field_dict["history"] = history
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
        from ..models.roblox_localization_tables_api_translation_history import (
            RobloxLocalizationTablesApiTranslationHistory,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifier.from_dict(_identifier)

        _history = d.pop("history", UNSET)
        history: list[RobloxLocalizationTablesApiTranslationHistory] | Unset = UNSET
        if _history is not UNSET:
            history = []
            for history_item_data in _history:
                history_item = RobloxLocalizationTablesApiTranslationHistory.from_dict(history_item_data)

                history.append(history_item)

        next_cursor = d.pop("nextCursor", UNSET)

        roblox_localization_tables_api_entry_translation_history_paged = cls(
            identifier=identifier,
            history=history,
            next_cursor=next_cursor,
        )

        return roblox_localization_tables_api_entry_translation_history_paged
