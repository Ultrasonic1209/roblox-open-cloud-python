from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_create_table_request_owner_type import (
    RobloxLocalizationTablesApiCreateTableRequestOwnerType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiCreateTableRequest")


@_attrs_define
class RobloxLocalizationTablesApiCreateTableRequest:
    """
    Attributes:
        name (str | Unset):
        owner_type (RobloxLocalizationTablesApiCreateTableRequestOwnerType | Unset):
        owner_id (int | Unset):
    """

    name: str | Unset = UNSET
    owner_type: RobloxLocalizationTablesApiCreateTableRequestOwnerType | Unset = UNSET
    owner_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_type: str | Unset = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type.value

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        _owner_type = d.pop("ownerType", UNSET)
        owner_type: RobloxLocalizationTablesApiCreateTableRequestOwnerType | Unset
        if isinstance(_owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = RobloxLocalizationTablesApiCreateTableRequestOwnerType(_owner_type)

        owner_id = d.pop("ownerId", UNSET)

        roblox_localization_tables_api_create_table_request = cls(
            name=name,
            owner_type=owner_type,
            owner_id=owner_id,
        )

        return roblox_localization_tables_api_create_table_request
