from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3Options")


@_attrs_define
class Roblox2AssetdeliveryV3Options:
    """
    Attributes:
        metadata (Any | Unset):
    """

    metadata: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata = d.pop("metadata", UNSET)

        roblox_2_assetdelivery_v3_options = cls(
            metadata=metadata,
        )

        return roblox_2_assetdelivery_v3_options
