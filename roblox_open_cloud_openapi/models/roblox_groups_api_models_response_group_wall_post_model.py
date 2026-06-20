from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiModelsResponseGroupWallPostModel")


@_attrs_define
class RobloxGroupsApiModelsResponseGroupWallPostModel:
    """A response model for group wall post information

    Attributes:
        id (int | Unset): The group wall post Id.
        poster (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        body (str | Unset): The group wall post body.
        created (datetime.datetime | Unset): When the group wall post was posted.
        updated (datetime.datetime | Unset): When the group wall post was last updated.
    """

    id: int | Unset = UNSET
    poster: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    body: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        poster: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poster, Unset):
            poster = self.poster.to_dict()

        body = self.body

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if poster is not UNSET:
            field_dict["poster"] = poster
        if body is not UNSET:
            field_dict["body"] = body
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _poster = d.pop("poster", UNSET)
        poster: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_poster, Unset):
            poster = UNSET
        else:
            poster = RobloxGroupsApiModelsResponseUserModel.from_dict(_poster)

        body = d.pop("body", UNSET)

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

        roblox_groups_api_models_response_group_wall_post_model = cls(
            id=id,
            poster=poster,
            body=body,
            created=created,
            updated=updated,
        )

        return roblox_groups_api_models_response_group_wall_post_model
