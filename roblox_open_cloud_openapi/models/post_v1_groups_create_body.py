from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostV1GroupsCreateBody")


@_attrs_define
class PostV1GroupsCreateBody:
    """
    Attributes:
        name (str | Unset): The name of the group.
        description (str | Unset): The group description.
        public_group (bool | Unset): Whether or not the group is open for anyone to join.
        builders_club_members_only (bool | Unset): Whether or not the group is only open to join for builders club
            members.
        files (File | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    public_group: bool | Unset = UNSET
    builders_club_members_only: bool | Unset = UNSET
    files: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        public_group = self.public_group

        builders_club_members_only = self.builders_club_members_only

        files: FileTypes | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_group is not UNSET:
            field_dict["publicGroup"] = public_group
        if builders_club_members_only is not UNSET:
            field_dict["buildersClubMembersOnly"] = builders_club_members_only
        if files is not UNSET:
            field_dict["Files"] = files

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.public_group, Unset):
            files.append(("publicGroup", (None, str(self.public_group).encode(), "text/plain")))

        if not isinstance(self.builders_club_members_only, Unset):
            files.append(
                ("buildersClubMembersOnly", (None, str(self.builders_club_members_only).encode(), "text/plain"))
            )

        if not isinstance(self.files, Unset):
            files.append(("Files", self.files.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        public_group = d.pop("publicGroup", UNSET)

        builders_club_members_only = d.pop("buildersClubMembersOnly", UNSET)

        _files = d.pop("Files", UNSET)
        files: File | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = File(payload=BytesIO(_files))

        post_v1_groups_create_body = cls(
            name=name,
            description=description,
            public_group=public_group,
            builders_club_members_only=builders_club_members_only,
            files=files,
        )

        post_v1_groups_create_body.additional_properties = d
        return post_v1_groups_create_body

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
