from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3PinnedVersion")


@_attrs_define
class Roblox2AssetdeliveryV3PinnedVersion:
    """
    Attributes:
        version_number (int | Unset):
    """

    version_number: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version_number = self.version_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version_number = d.pop("versionNumber", UNSET)

        roblox_2_assetdelivery_v3_pinned_version = cls(
            version_number=version_number,
        )

        return roblox_2_assetdelivery_v3_pinned_version
