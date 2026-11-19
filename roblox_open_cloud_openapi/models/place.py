from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Place")


@_attrs_define
class Place:
    """Represents a Roblox place.

    Attributes:
        template_place (str): The resource path of the template place used to initialize the place on
            creation.
            The newly created place will be a clone of this template.
            A list of the valid template places can be obtained from
            ListTemplatePlaces. Format: universes/{universe_id}/places/{place_id}
        path (str | Unset): The resource path of the place.

            Format: `universes/{universe_id}/places/{place_id}`
        create_time (datetime.datetime | Unset): The timestamp at which the place was created.
        update_time (datetime.datetime | Unset): The timestamp at which the place was updated.
        display_name (str | Unset): The name of the place.
        description (str | Unset): The description of the place.
        server_size (int | Unset): The maximum number of allowed users in a single server.
        root (bool | Unset): Whether this place is its parent universe's root place or not.
            Each universe has exactly one root place.
        universe_runtime_creation (bool | Unset): Whether this place was created through in-experience creation.
            If true, the place was created by calling AssetService::CreatePlaceAsync()
            from a script.
    """

    template_place: str
    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    server_size: int | Unset = UNSET
    root: bool | Unset = UNSET
    universe_runtime_creation: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_place = self.template_place

        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        display_name = self.display_name

        description = self.description

        server_size = self.server_size

        root = self.root

        universe_runtime_creation = self.universe_runtime_creation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "templatePlace": template_place,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if server_size is not UNSET:
            field_dict["serverSize"] = server_size
        if root is not UNSET:
            field_dict["root"] = root
        if universe_runtime_creation is not UNSET:
            field_dict["universeRuntimeCreation"] = universe_runtime_creation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_place = d.pop("templatePlace")

        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        server_size = d.pop("serverSize", UNSET)

        root = d.pop("root", UNSET)

        universe_runtime_creation = d.pop("universeRuntimeCreation", UNSET)

        place = cls(
            template_place=template_place,
            path=path,
            create_time=create_time,
            update_time=update_time,
            display_name=display_name,
            description=description,
            server_size=server_size,
            root=root,
            universe_runtime_creation=universe_runtime_creation,
        )

        return place
