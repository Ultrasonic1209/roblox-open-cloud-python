from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
    from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation


T = TypeVar("T", bound="RobloxLocalizationTablesApiModifiedEntry")


@_attrs_define
class RobloxLocalizationTablesApiModifiedEntry:
    """
    Attributes:
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        translations (list[RobloxLocalizationTablesApiTranslation] | Unset):
    """

    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
        from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifier.from_dict(_identifier)

        _translations = d.pop("translations", UNSET)
        translations: list[RobloxLocalizationTablesApiTranslation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = RobloxLocalizationTablesApiTranslation.from_dict(translations_item_data)

                translations.append(translations_item)

        roblox_localization_tables_api_modified_entry = cls(
            identifier=identifier,
            translations=translations,
        )

        return roblox_localization_tables_api_modified_entry
