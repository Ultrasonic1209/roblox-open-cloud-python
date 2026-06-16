from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupConfigurationDetailsResponse")


@_attrs_define
class RobloxGroupsApiGroupConfigurationDetailsResponse:
    """A detailed group response model

    Attributes:
        group_id (int | Unset): The group id
        emblem_id (int | Unset): The group emblem id
        cover_photo_id (int | Unset): The group cover photo id
    """

    group_id: int | Unset = UNSET
    emblem_id: int | Unset = UNSET
    cover_photo_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        emblem_id = self.emblem_id

        cover_photo_id = self.cover_photo_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if emblem_id is not UNSET:
            field_dict["emblemId"] = emblem_id
        if cover_photo_id is not UNSET:
            field_dict["coverPhotoId"] = cover_photo_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        emblem_id = d.pop("emblemId", UNSET)

        cover_photo_id = d.pop("coverPhotoId", UNSET)

        roblox_groups_api_group_configuration_details_response = cls(
            group_id=group_id,
            emblem_id=emblem_id,
            cover_photo_id=cover_photo_id,
        )

        return roblox_groups_api_group_configuration_details_response
