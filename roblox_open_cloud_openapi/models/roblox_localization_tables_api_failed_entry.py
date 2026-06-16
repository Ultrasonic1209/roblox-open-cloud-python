from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
    from ..models.roblox_localization_tables_api_entry_metadata import RobloxLocalizationTablesApiEntryMetadata
    from ..models.roblox_localization_tables_api_error import RobloxLocalizationTablesApiError
    from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation


T = TypeVar("T", bound="RobloxLocalizationTablesApiFailedEntry")


@_attrs_define
class RobloxLocalizationTablesApiFailedEntry:
    """
    Attributes:
        error (RobloxLocalizationTablesApiError | Unset):
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        metadata (RobloxLocalizationTablesApiEntryMetadata | Unset):
        translations (list[RobloxLocalizationTablesApiTranslation] | Unset):
        created_time (datetime.datetime | Unset):
    """

    error: RobloxLocalizationTablesApiError | Unset = UNSET
    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    metadata: RobloxLocalizationTablesApiEntryMetadata | Unset = UNSET
    translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if translations is not UNSET:
            field_dict["translations"] = translations
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
        from ..models.roblox_localization_tables_api_entry_metadata import RobloxLocalizationTablesApiEntryMetadata
        from ..models.roblox_localization_tables_api_error import RobloxLocalizationTablesApiError
        from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: RobloxLocalizationTablesApiError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = RobloxLocalizationTablesApiError.from_dict(_error)

        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifier.from_dict(_identifier)

        _metadata = d.pop("metadata", UNSET)
        metadata: RobloxLocalizationTablesApiEntryMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RobloxLocalizationTablesApiEntryMetadata.from_dict(_metadata)

        _translations = d.pop("translations", UNSET)
        translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = RobloxLocalizationTablesApiTranslation.from_dict(translations_item_data)

                translations.append(translations_item)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        roblox_localization_tables_api_failed_entry = cls(
            error=error,
            identifier=identifier,
            metadata=metadata,
            translations=translations,
            created_time=created_time,
        )

        return roblox_localization_tables_api_failed_entry
