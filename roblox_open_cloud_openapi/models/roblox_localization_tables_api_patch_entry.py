from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
    from ..models.roblox_localization_tables_api_entry_metadata import RobloxLocalizationTablesApiEntryMetadata
    from ..models.roblox_localization_tables_api_patch_translation import RobloxLocalizationTablesApiPatchTranslation


T = TypeVar("T", bound="RobloxLocalizationTablesApiPatchEntry")


@_attrs_define
class RobloxLocalizationTablesApiPatchEntry:
    """
    Attributes:
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        metadata (RobloxLocalizationTablesApiEntryMetadata | Unset):
        translations (list[RobloxLocalizationTablesApiPatchTranslation] | Unset):
        delete (bool | Unset):
    """

    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    metadata: RobloxLocalizationTablesApiEntryMetadata | Unset = UNSET
    translations: list[RobloxLocalizationTablesApiPatchTranslation] | Unset = UNSET
    delete: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        delete = self.delete

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if translations is not UNSET:
            field_dict["translations"] = translations
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
        from ..models.roblox_localization_tables_api_entry_metadata import RobloxLocalizationTablesApiEntryMetadata
        from ..models.roblox_localization_tables_api_patch_translation import (
            RobloxLocalizationTablesApiPatchTranslation,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
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
        translations: list[RobloxLocalizationTablesApiPatchTranslation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = RobloxLocalizationTablesApiPatchTranslation.from_dict(translations_item_data)

                translations.append(translations_item)

        delete = d.pop("delete", UNSET)

        roblox_localization_tables_api_patch_entry = cls(
            identifier=identifier,
            metadata=metadata,
            translations=translations,
            delete=delete,
        )

        return roblox_localization_tables_api_patch_entry
