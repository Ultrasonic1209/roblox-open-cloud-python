from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_latest_version import Roblox2AssetdeliveryV3LatestVersion
    from ..models.roblox_2_assetdelivery_v3_pinned_version import Roblox2AssetdeliveryV3PinnedVersion
    from ..models.roblox_2_assetdelivery_v3_stable_version import Roblox2AssetdeliveryV3StableVersion


T = TypeVar("T", bound="Roblox2AssetdeliveryV3VersionStrategy")


@_attrs_define
class Roblox2AssetdeliveryV3VersionStrategy:
    """
    Attributes:
        stable (Roblox2AssetdeliveryV3StableVersion | Unset):
        pinned (Roblox2AssetdeliveryV3PinnedVersion | Unset):
        latest (Roblox2AssetdeliveryV3LatestVersion | Unset):
    """

    stable: Roblox2AssetdeliveryV3StableVersion | Unset = UNSET
    pinned: Roblox2AssetdeliveryV3PinnedVersion | Unset = UNSET
    latest: Roblox2AssetdeliveryV3LatestVersion | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        stable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stable, Unset):
            stable = self.stable.to_dict()

        pinned: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pinned, Unset):
            pinned = self.pinned.to_dict()

        latest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if stable is not UNSET:
            field_dict["stable"] = stable
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if latest is not UNSET:
            field_dict["latest"] = latest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_latest_version import Roblox2AssetdeliveryV3LatestVersion  # noqa: PLC0415
        from ..models.roblox_2_assetdelivery_v3_pinned_version import Roblox2AssetdeliveryV3PinnedVersion  # noqa: PLC0415
        from ..models.roblox_2_assetdelivery_v3_stable_version import Roblox2AssetdeliveryV3StableVersion  # noqa: PLC0415

        d = dict(src_dict)
        _stable = d.pop("stable", UNSET)
        stable: Roblox2AssetdeliveryV3StableVersion | Unset
        if isinstance(_stable, Unset):
            stable = UNSET
        else:
            stable = Roblox2AssetdeliveryV3StableVersion.from_dict(_stable)

        _pinned = d.pop("pinned", UNSET)
        pinned: Roblox2AssetdeliveryV3PinnedVersion | Unset
        if isinstance(_pinned, Unset):
            pinned = UNSET
        else:
            pinned = Roblox2AssetdeliveryV3PinnedVersion.from_dict(_pinned)

        _latest = d.pop("latest", UNSET)
        latest: Roblox2AssetdeliveryV3LatestVersion | Unset
        if isinstance(_latest, Unset):
            latest = UNSET
        else:
            latest = Roblox2AssetdeliveryV3LatestVersion.from_dict(_latest)

        roblox_2_assetdelivery_v3_version_strategy = cls(
            stable=stable,
            pinned=pinned,
            latest=latest,
        )

        return roblox_2_assetdelivery_v3_version_strategy
