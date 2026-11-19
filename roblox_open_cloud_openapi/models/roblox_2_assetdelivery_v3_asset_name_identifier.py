from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3AssetNameIdentifier")


@_attrs_define
class Roblox2AssetdeliveryV3AssetNameIdentifier:
    """
    Attributes:
        name (str):
        universe_id (int | Unset):
    """

    name: str
    universe_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        universe_id = d.pop("universeId", UNSET)

        roblox_2_assetdelivery_v3_asset_name_identifier = cls(
            name=name,
            universe_id=universe_id,
        )

        return roblox_2_assetdelivery_v3_asset_name_identifier
