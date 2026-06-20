from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiTableOperationLimits")


@_attrs_define
class RobloxLocalizationTablesApiTableOperationLimits:
    """
    Attributes:
        max_entries_per_update (int | Unset): Maximum number of entries for a patch request
    """

    max_entries_per_update: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_entries_per_update = self.max_entries_per_update

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_entries_per_update is not UNSET:
            field_dict["maxEntriesPerUpdate"] = max_entries_per_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        max_entries_per_update = d.pop("maxEntriesPerUpdate", UNSET)

        roblox_localization_tables_api_table_operation_limits = cls(
            max_entries_per_update=max_entries_per_update,
        )

        return roblox_localization_tables_api_table_operation_limits
