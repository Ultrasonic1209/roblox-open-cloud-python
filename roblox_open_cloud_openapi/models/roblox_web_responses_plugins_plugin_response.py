from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesPluginsPluginResponse")


@_attrs_define
class RobloxWebResponsesPluginsPluginResponse:
    """Represents information about a plugin.

    Attributes:
        id (int | Unset): The plugin Id.
        name (str | Unset): The plugin name.
        description (str | Unset): The plugin description.
        comments_enabled (bool | Unset): Whether or not the plugin allows comments to be posted.
        version_id (int | Unset): plugin version id
        created (datetime.datetime | Unset): The time the plugin was created.
        updated (datetime.datetime | Unset): The last time the plugin was updated.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    comments_enabled: bool | Unset = UNSET
    version_id: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        comments_enabled = self.comments_enabled

        version_id = self.version_id

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
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if comments_enabled is not UNSET:
            field_dict["commentsEnabled"] = comments_enabled
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        comments_enabled = d.pop("commentsEnabled", UNSET)

        version_id = d.pop("versionId", UNSET)

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

        roblox_web_responses_plugins_plugin_response = cls(
            id=id,
            name=name,
            description=description,
            comments_enabled=comments_enabled,
            version_id=version_id,
            created=created,
            updated=updated,
        )

        return roblox_web_responses_plugins_plugin_response
