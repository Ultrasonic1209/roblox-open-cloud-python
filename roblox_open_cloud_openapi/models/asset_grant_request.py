from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetGrantRequest")


@_attrs_define
class AssetGrantRequest:
    """Asset grant requests with additional options to grant to dependencies.

    Attributes:
        asset_id (int | Unset): The asset ID to grant permission to.
        grant_to_dependencies (bool | Unset): Whether to extend the permission grant to dependencies of the asset. This
            will be done asynchronously after the main grant.
        parent_version_number (int | Unset): The version number of 'assetId' to use for determining asset dependencies.
    """

    asset_id: int | Unset = UNSET
    grant_to_dependencies: bool | Unset = UNSET
    parent_version_number: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        grant_to_dependencies = self.grant_to_dependencies

        parent_version_number = self.parent_version_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if grant_to_dependencies is not UNSET:
            field_dict["grantToDependencies"] = grant_to_dependencies
        if parent_version_number is not UNSET:
            field_dict["parentVersionNumber"] = parent_version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        grant_to_dependencies = d.pop("grantToDependencies", UNSET)

        parent_version_number = d.pop("parentVersionNumber", UNSET)

        asset_grant_request = cls(
            asset_id=asset_id,
            grant_to_dependencies=grant_to_dependencies,
            parent_version_number=parent_version_number,
        )

        return asset_grant_request
