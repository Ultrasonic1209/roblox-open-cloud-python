from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RollbackAssetVersionRequest")


@_attrs_define
class RollbackAssetVersionRequest:
    """Request to roll back an asset to a previous version.

    Attributes:
        asset_version (str): The asset version path in the format of `assets/{assetId}/versions/{versionNumber}`.
    """

    asset_version: str

    def to_dict(self) -> dict[str, Any]:
        asset_version = self.asset_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assetVersion": asset_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_version = d.pop("assetVersion")

        rollback_asset_version_request = cls(
            asset_version=asset_version,
        )

        return rollback_asset_version_request
