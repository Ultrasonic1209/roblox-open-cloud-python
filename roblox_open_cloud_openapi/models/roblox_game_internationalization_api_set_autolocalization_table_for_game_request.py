from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest")


@_attrs_define
class RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest:
    """
    Attributes:
        table_id (UUID | Unset):
    """

    table_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if table_id is not UNSET:
            field_dict["tableId"] = table_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id, Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)

        roblox_game_internationalization_api_set_autolocalization_table_for_game_request = cls(
            table_id=table_id,
        )

        return roblox_game_internationalization_api_set_autolocalization_table_for_game_request
