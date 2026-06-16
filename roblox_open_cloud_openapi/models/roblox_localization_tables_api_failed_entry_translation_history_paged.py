from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
    from ..models.roblox_localization_tables_api_error import RobloxLocalizationTablesApiError


T = TypeVar("T", bound="RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged")


@_attrs_define
class RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged:
    """
    Attributes:
        identifier (RobloxLocalizationTablesApiEntryIdentifier | Unset):
        count (int | Unset):
        error (RobloxLocalizationTablesApiError | Unset):
    """

    identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset = UNSET
    count: int | Unset = UNSET
    error: RobloxLocalizationTablesApiError | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        count = self.count

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if count is not UNSET:
            field_dict["count"] = count
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier import RobloxLocalizationTablesApiEntryIdentifier
        from ..models.roblox_localization_tables_api_error import RobloxLocalizationTablesApiError

        d = dict(src_dict)
        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifier | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifier.from_dict(_identifier)

        count = d.pop("count", UNSET)

        _error = d.pop("error", UNSET)
        error: RobloxLocalizationTablesApiError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = RobloxLocalizationTablesApiError.from_dict(_error)

        roblox_localization_tables_api_failed_entry_translation_history_paged = cls(
            identifier=identifier,
            count=count,
            error=error,
        )

        return roblox_localization_tables_api_failed_entry_translation_history_paged
