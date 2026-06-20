from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryOperationLimits")


@_attrs_define
class RobloxLocalizationTablesApiEntryOperationLimits:
    """
    Attributes:
        max_context_length (int | Unset): Maximum character limit for entry context
        max_key_length (int | Unset): Maximum character limit for entry key
        max_source_length (int | Unset): Maximum character limit for entry source text
        max_example_length (int | Unset): Maximum character limit for entry example
        max_game_location_path_length (int | Unset): Maximum character limit for game location path
    """

    max_context_length: int | Unset = UNSET
    max_key_length: int | Unset = UNSET
    max_source_length: int | Unset = UNSET
    max_example_length: int | Unset = UNSET
    max_game_location_path_length: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_context_length = self.max_context_length

        max_key_length = self.max_key_length

        max_source_length = self.max_source_length

        max_example_length = self.max_example_length

        max_game_location_path_length = self.max_game_location_path_length

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_context_length is not UNSET:
            field_dict["maxContextLength"] = max_context_length
        if max_key_length is not UNSET:
            field_dict["maxKeyLength"] = max_key_length
        if max_source_length is not UNSET:
            field_dict["maxSourceLength"] = max_source_length
        if max_example_length is not UNSET:
            field_dict["maxExampleLength"] = max_example_length
        if max_game_location_path_length is not UNSET:
            field_dict["maxGameLocationPathLength"] = max_game_location_path_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        max_context_length = d.pop("maxContextLength", UNSET)

        max_key_length = d.pop("maxKeyLength", UNSET)

        max_source_length = d.pop("maxSourceLength", UNSET)

        max_example_length = d.pop("maxExampleLength", UNSET)

        max_game_location_path_length = d.pop("maxGameLocationPathLength", UNSET)

        roblox_localization_tables_api_entry_operation_limits = cls(
            max_context_length=max_context_length,
            max_key_length=max_key_length,
            max_source_length=max_source_length,
            max_example_length=max_example_length,
            max_game_location_path_length=max_game_location_path_length,
        )

        return roblox_localization_tables_api_entry_operation_limits
