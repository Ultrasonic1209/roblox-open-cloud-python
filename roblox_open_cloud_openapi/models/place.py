from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
            ListTemplatePlaces. Format: universes/{universe_id}/places/{place_id} Example:
            universes/{universe_id}/places/{place_id}.
        path (str | Unset): The resource path of the place.

            Format: `universes/{universe_id}/places/{place_id}` Example: universes/123/places/123.
        create_time (datetime.datetime | Unset): The timestamp at which the place was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp at which the place was updated. Example:
            2023-07-05T12:34:56Z.
        display_name (str | Unset): The name of the place. Example: ROBLOX Battle [OPEN].
        description (str | Unset): The description of the place. Example: OPEN SOURCE!
             Feel free to check out how we made this game and ask us about it!.
        server_size (int | Unset): The maximum number of allowed users in a single server.
        root (bool | Unset): Whether this place is its parent universe's root place or not.
            Each universe has exactly one root place. Example: True.
        universe_runtime_creation (bool | Unset): Whether this place was created through in-experience creation.
            If true, the place was created by calling AssetService::CreatePlaceAsync()
            from a script. Example: True.
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
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

        place.additional_properties = d
        return place

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
