from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiMatchedEntry")


@_attrs_define
class RobloxLocalizationTablesApiMatchedEntry:
    """
    Attributes:
        source (str | Unset):
        matched_param_index (int | Unset):
    """

    source: str | Unset = UNSET
    matched_param_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        matched_param_index = self.matched_param_index

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if matched_param_index is not UNSET:
            field_dict["matchedParamIndex"] = matched_param_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        source = d.pop("source", UNSET)

        matched_param_index = d.pop("matchedParamIndex", UNSET)

        roblox_localization_tables_api_matched_entry = cls(
            source=source,
            matched_param_index=matched_param_index,
        )

        return roblox_localization_tables_api_matched_entry
