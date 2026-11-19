from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3InsertContext")


@_attrs_define
class Roblox2AssetdeliveryV3InsertContext:
    """
    Attributes:
        script_insert (bool | Unset):
        client_insert (bool | Unset):
        server_place_id (int | Unset):
    """

    script_insert: bool | Unset = UNSET
    client_insert: bool | Unset = UNSET
    server_place_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        script_insert = self.script_insert

        client_insert = self.client_insert

        server_place_id = self.server_place_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if script_insert is not UNSET:
            field_dict["scriptInsert"] = script_insert
        if client_insert is not UNSET:
            field_dict["clientInsert"] = client_insert
        if server_place_id is not UNSET:
            field_dict["serverPlaceId"] = server_place_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        script_insert = d.pop("scriptInsert", UNSET)

        client_insert = d.pop("clientInsert", UNSET)

        server_place_id = d.pop("serverPlaceId", UNSET)

        roblox_2_assetdelivery_v3_insert_context = cls(
            script_insert=script_insert,
            client_insert=client_insert,
            server_place_id=server_place_id,
        )

        return roblox_2_assetdelivery_v3_insert_context
