from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_asset_name_identifier import Roblox2AssetdeliveryV3AssetNameIdentifier


T = TypeVar("T", bound="Roblox2AssetdeliveryV3AssetIdentifier")


@_attrs_define
class Roblox2AssetdeliveryV3AssetIdentifier:
    """
    Attributes:
        asset_id (int | Unset):
        hash_ (str | Unset):
        asset_version_id (int | Unset):
        asset_name (Roblox2AssetdeliveryV3AssetNameIdentifier | Unset):
    """

    asset_id: int | Unset = UNSET
    hash_: str | Unset = UNSET
    asset_version_id: int | Unset = UNSET
    asset_name: Roblox2AssetdeliveryV3AssetNameIdentifier | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        hash_ = self.hash_

        asset_version_id = self.asset_version_id

        asset_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_name, Unset):
            asset_name = self.asset_name.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if asset_version_id is not UNSET:
            field_dict["assetVersionId"] = asset_version_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_asset_name_identifier import Roblox2AssetdeliveryV3AssetNameIdentifier  # noqa: PLC0415

        d = dict(src_dict)
        asset_id = d.pop("assetId", UNSET)

        hash_ = d.pop("hash", UNSET)

        asset_version_id = d.pop("assetVersionId", UNSET)

        _asset_name = d.pop("assetName", UNSET)
        asset_name: Roblox2AssetdeliveryV3AssetNameIdentifier | Unset
        if isinstance(_asset_name, Unset):
            asset_name = UNSET
        else:
            asset_name = Roblox2AssetdeliveryV3AssetNameIdentifier.from_dict(_asset_name)

        roblox_2_assetdelivery_v3_asset_identifier = cls(
            asset_id=asset_id,
            hash_=hash_,
            asset_version_id=asset_version_id,
            asset_name=asset_name,
        )

        return roblox_2_assetdelivery_v3_asset_identifier
