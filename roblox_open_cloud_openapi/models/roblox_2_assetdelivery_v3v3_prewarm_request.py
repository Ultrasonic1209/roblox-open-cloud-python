from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_prewarm_target import Roblox2AssetdeliveryV3PrewarmTarget


T = TypeVar("T", bound="Roblox2AssetdeliveryV3V3PrewarmRequest")


@_attrs_define
class Roblox2AssetdeliveryV3V3PrewarmRequest:
    """
    Attributes:
        target (Roblox2AssetdeliveryV3PrewarmTarget):
    """

    target: Roblox2AssetdeliveryV3PrewarmTarget

    def to_dict(self) -> dict[str, Any]:
        target = self.target.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_prewarm_target import Roblox2AssetdeliveryV3PrewarmTarget  # noqa: PLC0415

        d = dict(src_dict)
        target = Roblox2AssetdeliveryV3PrewarmTarget.from_dict(d.pop("target"))

        roblox_2_assetdelivery_v3v3_prewarm_request = cls(
            target=target,
        )

        return roblox_2_assetdelivery_v3v3_prewarm_request
