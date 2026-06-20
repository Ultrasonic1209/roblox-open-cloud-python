from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiShoutResponse")


@_attrs_define
class RobloxGroupsApiShoutResponse:
    """
    Attributes:
        body (str | Unset): The shout's message
        poster (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        created (datetime.datetime | Unset): The shout's created time
        updated (datetime.datetime | Unset): The shout's last updated time
    """

    body: str | Unset = UNSET
    poster: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        poster: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poster, Unset):
            poster = self.poster.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if poster is not UNSET:
            field_dict["poster"] = poster
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        body = d.pop("body", UNSET)

        _poster = d.pop("poster", UNSET)
        poster: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_poster, Unset):
            poster = UNSET
        else:
            poster = RobloxGroupsApiModelsResponseUserModel.from_dict(_poster)

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

        roblox_groups_api_shout_response = cls(
            body=body,
            poster=poster,
            created=created,
            updated=updated,
        )

        return roblox_groups_api_shout_response
