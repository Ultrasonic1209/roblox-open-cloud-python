from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.groups_api_roblox_web_responses_related_entity_type_response_roblox_platform_assets_asset_type import (
        GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType,
    )
    from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_core_creator_type import (
        RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType,
    )


T = TypeVar("T", bound="RobloxGroupsApiModelsResponseGroupExperienceResponse")


@_attrs_define
class RobloxGroupsApiModelsResponseGroupExperienceResponse:
    """A response model representing an experience/game.

    Attributes:
        id (int | Unset): The game (universe) Id.
        name (str | Unset): The game name.
        description (str | Unset): The game description.
        creator (RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType | Unset):
        root_place (GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType | Unset):
        created (datetime.datetime | Unset): When the game was created.
        updated (datetime.datetime | Unset): When the game was last updated.
        place_visits (int | Unset): The number of place visits for this game.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    creator: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType | Unset = UNSET
    root_place: GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    place_visits: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        root_place: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_place, Unset):
            root_place = self.root_place.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        place_visits = self.place_visits

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if root_place is not UNSET:
            field_dict["rootPlace"] = root_place
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if place_visits is not UNSET:
            field_dict["placeVisits"] = place_visits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.groups_api_roblox_web_responses_related_entity_type_response_roblox_platform_assets_asset_type import (
            GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType,
        )
        from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_core_creator_type import (
            RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType.from_dict(_creator)

        _root_place = d.pop("rootPlace", UNSET)
        root_place: GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType | Unset
        if isinstance(_root_place, Unset):
            root_place = UNSET
        else:
            root_place = GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformAssetsAssetType.from_dict(
                _root_place
            )

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

        place_visits = d.pop("placeVisits", UNSET)

        roblox_groups_api_models_response_group_experience_response = cls(
            id=id,
            name=name,
            description=description,
            creator=creator,
            root_place=root_place,
            created=created,
            updated=updated,
            place_visits=place_visits,
        )

        return roblox_groups_api_models_response_group_experience_response
