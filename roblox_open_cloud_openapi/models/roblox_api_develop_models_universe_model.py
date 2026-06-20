from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_universe_model_audiences_item import (
    RobloxApiDevelopModelsUniverseModelAudiencesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseModel")


@_attrs_define
class RobloxApiDevelopModelsUniverseModel:
    """Represents a universe in API endpoint results.

    Attributes:
        id (int | Unset): The universe Id.
        name (str | Unset): The name of the universe
        description (str | Unset): The description of the universe
        is_archived (bool | Unset): Is this universe archived
        root_place_id (int | Unset): The universe's root place id
        is_active (bool | Unset): Is this universe active
        privacy_type (str | Unset): The universe's privacy type.
        creator_type (str | Unset): The creator type, either "User" or "Group"
        creator_target_id (int | Unset): The id of the user or group that created this universe.
        creator_name (str | Unset): The name of the creator of the universe.
        created (datetime.datetime | Unset): The created System.DateTime
        updated (datetime.datetime | Unset): The updated System.DateTime
        audiences (list[RobloxApiDevelopModelsUniverseModelAudiencesItem] | Unset): The audiences this universe is
            visible to (e.g. Editors, PlayTesters, Friends, Public).
            Always non-null; may be empty when audience visibility has not been configured.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    root_place_id: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    privacy_type: str | Unset = UNSET
    creator_type: str | Unset = UNSET
    creator_target_id: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    audiences: list[RobloxApiDevelopModelsUniverseModelAudiencesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_archived = self.is_archived

        root_place_id = self.root_place_id

        is_active = self.is_active

        privacy_type = self.privacy_type

        creator_type = self.creator_type

        creator_target_id = self.creator_target_id

        creator_name = self.creator_name

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        audiences: list[int] | Unset = UNSET
        if not isinstance(self.audiences, Unset):
            audiences = []
            for audiences_item_data in self.audiences:
                audiences_item = audiences_item_data.value
                audiences.append(audiences_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if privacy_type is not UNSET:
            field_dict["privacyType"] = privacy_type
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_target_id is not UNSET:
            field_dict["creatorTargetId"] = creator_target_id
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if audiences is not UNSET:
            field_dict["audiences"] = audiences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        root_place_id = d.pop("rootPlaceId", UNSET)

        is_active = d.pop("isActive", UNSET)

        privacy_type = d.pop("privacyType", UNSET)

        creator_type = d.pop("creatorType", UNSET)

        creator_target_id = d.pop("creatorTargetId", UNSET)

        creator_name = d.pop("creatorName", UNSET)

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

        _audiences = d.pop("audiences", UNSET)
        audiences: list[RobloxApiDevelopModelsUniverseModelAudiencesItem] | Unset = UNSET
        if _audiences is not UNSET:
            audiences = []
            for audiences_item_data in _audiences:
                audiences_item = RobloxApiDevelopModelsUniverseModelAudiencesItem(audiences_item_data)

                audiences.append(audiences_item)

        roblox_api_develop_models_universe_model = cls(
            id=id,
            name=name,
            description=description,
            is_archived=is_archived,
            root_place_id=root_place_id,
            is_active=is_active,
            privacy_type=privacy_type,
            creator_type=creator_type,
            creator_target_id=creator_target_id,
            creator_name=creator_name,
            created=created,
            updated=updated,
            audiences=audiences,
        )

        return roblox_api_develop_models_universe_model
