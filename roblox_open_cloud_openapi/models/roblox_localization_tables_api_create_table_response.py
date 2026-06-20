from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiCreateTableResponse")


@_attrs_define
class RobloxLocalizationTablesApiCreateTableResponse:
    """
    Attributes:
        id (UUID | Unset):
        asset_id (int | Unset):
    """

    id: UUID | Unset = UNSET
    asset_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        asset_id = d.pop("assetId", UNSET)

        roblox_localization_tables_api_create_table_response = cls(
            id=id,
            asset_id=asset_id,
        )

        return roblox_localization_tables_api_create_table_response
