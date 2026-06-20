from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_get_table_response_owner_type import (
    RobloxLocalizationTablesApiGetTableResponseOwnerType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableResponse")


@_attrs_define
class RobloxLocalizationTablesApiGetTableResponse:
    """
    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        owner_type (RobloxLocalizationTablesApiGetTableResponseOwnerType | Unset): Enum for valid OwnerTypes. ['User' =
            0, 'Group' = 1]
        owner_id (int | Unset):
        asset_id (int | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    owner_type: RobloxLocalizationTablesApiGetTableResponseOwnerType | Unset = UNSET
    owner_id: int | Unset = UNSET
    asset_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        owner_type: str | Unset = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type.value

        owner_id = self.owner_id

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
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

        name = d.pop("name", UNSET)

        _owner_type = d.pop("ownerType", UNSET)
        owner_type: RobloxLocalizationTablesApiGetTableResponseOwnerType | Unset
        if isinstance(_owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = RobloxLocalizationTablesApiGetTableResponseOwnerType(_owner_type)

        owner_id = d.pop("ownerId", UNSET)

        asset_id = d.pop("assetId", UNSET)

        roblox_localization_tables_api_get_table_response = cls(
            id=id,
            name=name,
            owner_type=owner_type,
            owner_id=owner_id,
            asset_id=asset_id,
        )

        return roblox_localization_tables_api_get_table_response
