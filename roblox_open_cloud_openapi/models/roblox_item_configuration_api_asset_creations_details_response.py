from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_asset_creations_details_response_creator_type import (
    RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType,
)
from ..models.roblox_item_configuration_api_asset_creations_details_response_status import (
    RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiAssetCreationsDetailsResponse")


@_attrs_define
class RobloxItemConfigurationApiAssetCreationsDetailsResponse:
    """
    Attributes:
        asset_id (int | Unset): The asset Id.
        name (str | Unset): The asset name.
        status (RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus | Unset): The asset status. ['Unknown' =
            0, 'ReviewPending' = 1, 'Moderated' = 2, 'ReviewApproved' = 3, 'OnSale' = 4, 'OffSale' = 5, 'DelayedRelease' =
            6, 'Free' = 7]
        description (str | Unset): The asset description.
        creator_type (RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType | Unset): The creator type.
            ['Unknown' = 0, 'User' = 1, 'Group' = 2]
        creator_target_id (int | Unset): The creator target Id.
        is_archived (bool | Unset): Is the asset archived.
        asset_type (str | Unset): Type of the asset.
        created (datetime.datetime | Unset): Date asset was created.
        updated (datetime.datetime | Unset): Date asset was created.
        is_delisted (bool | Unset): If the asset is delisted.
        is_created_for_bundle (bool | Unset): If the asset is part of a bundle.
    """

    asset_id: int | Unset = UNSET
    name: str | Unset = UNSET
    status: RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus | Unset = UNSET
    description: str | Unset = UNSET
    creator_type: RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType | Unset = UNSET
    creator_target_id: int | Unset = UNSET
    is_archived: bool | Unset = UNSET
    asset_type: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    is_delisted: bool | Unset = UNSET
    is_created_for_bundle: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        creator_type: str | Unset = UNSET
        if not isinstance(self.creator_type, Unset):
            creator_type = self.creator_type.value

        creator_target_id = self.creator_target_id

        is_archived = self.is_archived

        asset_type = self.asset_type

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        is_delisted = self.is_delisted

        is_created_for_bundle = self.is_created_for_bundle

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_target_id is not UNSET:
            field_dict["creatorTargetId"] = creator_target_id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if is_delisted is not UNSET:
            field_dict["isDelisted"] = is_delisted
        if is_created_for_bundle is not UNSET:
            field_dict["isCreatedForBundle"] = is_created_for_bundle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus(_status)

        description = d.pop("description", UNSET)

        _creator_type = d.pop("creatorType", UNSET)
        creator_type: RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType | Unset
        if isinstance(_creator_type, Unset):
            creator_type = UNSET
        else:
            creator_type = RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType(_creator_type)

        creator_target_id = d.pop("creatorTargetId", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        asset_type = d.pop("assetType", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        is_delisted = d.pop("isDelisted", UNSET)

        is_created_for_bundle = d.pop("isCreatedForBundle", UNSET)

        roblox_item_configuration_api_asset_creations_details_response = cls(
            asset_id=asset_id,
            name=name,
            status=status,
            description=description,
            creator_type=creator_type,
            creator_target_id=creator_target_id,
            is_archived=is_archived,
            asset_type=asset_type,
            created=created,
            updated=updated,
            is_delisted=is_delisted,
            is_created_for_bundle=is_created_for_bundle,
        )

        return roblox_item_configuration_api_asset_creations_details_response
