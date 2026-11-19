from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Roblox2AssetdeliveryV3StableVersion")


@_attrs_define
class Roblox2AssetdeliveryV3StableVersion:
    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_2_assetdelivery_v3_stable_version = cls()

        return roblox_2_assetdelivery_v3_stable_version
