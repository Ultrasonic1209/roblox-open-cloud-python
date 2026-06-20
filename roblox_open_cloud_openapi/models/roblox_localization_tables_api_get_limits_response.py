from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_operation_limits import (
        RobloxLocalizationTablesApiEntryOperationLimits,
    )
    from ..models.roblox_localization_tables_api_table_operation_limits import (
        RobloxLocalizationTablesApiTableOperationLimits,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiGetLimitsResponse")


@_attrs_define
class RobloxLocalizationTablesApiGetLimitsResponse:
    """
    Attributes:
        entry_operation_limits (RobloxLocalizationTablesApiEntryOperationLimits | Unset):
        table_operation_limits (RobloxLocalizationTablesApiTableOperationLimits | Unset):
    """

    entry_operation_limits: RobloxLocalizationTablesApiEntryOperationLimits | Unset = UNSET
    table_operation_limits: RobloxLocalizationTablesApiTableOperationLimits | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entry_operation_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entry_operation_limits, Unset):
            entry_operation_limits = self.entry_operation_limits.to_dict()

        table_operation_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_operation_limits, Unset):
            table_operation_limits = self.table_operation_limits.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entry_operation_limits is not UNSET:
            field_dict["entryOperationLimits"] = entry_operation_limits
        if table_operation_limits is not UNSET:
            field_dict["tableOperationLimits"] = table_operation_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_operation_limits import (
            RobloxLocalizationTablesApiEntryOperationLimits,
        )
        from ..models.roblox_localization_tables_api_table_operation_limits import (
            RobloxLocalizationTablesApiTableOperationLimits,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _entry_operation_limits = d.pop("entryOperationLimits", UNSET)
        entry_operation_limits: RobloxLocalizationTablesApiEntryOperationLimits | Unset
        if isinstance(_entry_operation_limits, Unset):
            entry_operation_limits = UNSET
        else:
            entry_operation_limits = RobloxLocalizationTablesApiEntryOperationLimits.from_dict(_entry_operation_limits)

        _table_operation_limits = d.pop("tableOperationLimits", UNSET)
        table_operation_limits: RobloxLocalizationTablesApiTableOperationLimits | Unset
        if isinstance(_table_operation_limits, Unset):
            table_operation_limits = UNSET
        else:
            table_operation_limits = RobloxLocalizationTablesApiTableOperationLimits.from_dict(_table_operation_limits)

        roblox_localization_tables_api_get_limits_response = cls(
            entry_operation_limits=entry_operation_limits,
            table_operation_limits=table_operation_limits,
        )

        return roblox_localization_tables_api_get_limits_response
