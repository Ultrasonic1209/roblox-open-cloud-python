from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopAssetVersion")


@_attrs_define
class RobloxApiDevelopAssetVersion:
    """Model of an asset version.

    Attributes:
        id (int | Unset): The VersionID of the asset version.
        asset_id (int | Unset): The ID of the asset.
        asset_version_number (int | Unset): The version number.
        creator_type (str | Unset): Type of the asset version creator.
        creator_target_id (int | Unset): ID of the asset version creator.
        creating_universe_id (int | Unset): ID of the universe this asset version was created in.
        created (datetime.datetime | Unset): The created date of this asset version.
        is_equal_to_current_published_version (bool | Unset): Indicates if this version is same to current published
            version.
            This property is available on /v1/{assetId}/published-versions and /v1/{assetId}/version/{versionNumber}.
        is_published (bool | Unset): Indicates if this version is / was published.
            This property is available on /v1/{assetId}/saved-versions.
            This should be true for all assets coming from GetAssetPublishedVersionsByAssetId
    """

    id: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    asset_version_number: int | Unset = UNSET
    creator_type: str | Unset = UNSET
    creator_target_id: int | Unset = UNSET
    creating_universe_id: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    is_equal_to_current_published_version: bool | Unset = UNSET
    is_published: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        asset_id = self.asset_id

        asset_version_number = self.asset_version_number

        creator_type = self.creator_type

        creator_target_id = self.creator_target_id

        creating_universe_id = self.creating_universe_id

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        is_equal_to_current_published_version = self.is_equal_to_current_published_version

        is_published = self.is_published

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_version_number is not UNSET:
            field_dict["assetVersionNumber"] = asset_version_number
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_target_id is not UNSET:
            field_dict["creatorTargetId"] = creator_target_id
        if creating_universe_id is not UNSET:
            field_dict["creatingUniverseId"] = creating_universe_id
        if created is not UNSET:
            field_dict["created"] = created
        if is_equal_to_current_published_version is not UNSET:
            field_dict["isEqualToCurrentPublishedVersion"] = is_equal_to_current_published_version
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("Id", UNSET)

        asset_id = d.pop("assetId", UNSET)

        asset_version_number = d.pop("assetVersionNumber", UNSET)

        creator_type = d.pop("creatorType", UNSET)

        creator_target_id = d.pop("creatorTargetId", UNSET)

        creating_universe_id = d.pop("creatingUniverseId", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        is_equal_to_current_published_version = d.pop("isEqualToCurrentPublishedVersion", UNSET)

        is_published = d.pop("isPublished", UNSET)

        roblox_api_develop_asset_version = cls(
            id=id,
            asset_id=asset_id,
            asset_version_number=asset_version_number,
            creator_type=creator_type,
            creator_target_id=creator_target_id,
            creating_universe_id=creating_universe_id,
            created=created,
            is_equal_to_current_published_version=is_equal_to_current_published_version,
            is_published=is_published,
        )

        return roblox_api_develop_asset_version
