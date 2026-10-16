from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupConfigurationResponse")


@_attrs_define
class RobloxGroupsApiGroupConfigurationResponse:
    """A response model for group configuration

    Attributes:
        name_max_length (int | Unset): The maximum length of a group name
        description_max_length (int | Unset): The maximum length of a group description
        icon_max_file_size_mb (int | Unset): The maximum file size of the group icon in megabytes
        cover_photo_max_file_size_mb (int | Unset): The maximum file size of the group cover photo in megabytes
        valid_cover_photo_dimensions (str | Unset): The valid dimensions of the group cover photo in CSV format
        cost (int | Unset): The cost of purchasing a group
        is_using_two_step_webview_component (bool | Unset): Should the frontend use the 2sv webview component (as
            opposed to the built-in 2sv pop up)
    """

    name_max_length: int | Unset = UNSET
    description_max_length: int | Unset = UNSET
    icon_max_file_size_mb: int | Unset = UNSET
    cover_photo_max_file_size_mb: int | Unset = UNSET
    valid_cover_photo_dimensions: str | Unset = UNSET
    cost: int | Unset = UNSET
    is_using_two_step_webview_component: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name_max_length = self.name_max_length

        description_max_length = self.description_max_length

        icon_max_file_size_mb = self.icon_max_file_size_mb

        cover_photo_max_file_size_mb = self.cover_photo_max_file_size_mb

        valid_cover_photo_dimensions = self.valid_cover_photo_dimensions

        cost = self.cost

        is_using_two_step_webview_component = self.is_using_two_step_webview_component

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name_max_length is not UNSET:
            field_dict["nameMaxLength"] = name_max_length
        if description_max_length is not UNSET:
            field_dict["descriptionMaxLength"] = description_max_length
        if icon_max_file_size_mb is not UNSET:
            field_dict["iconMaxFileSizeMb"] = icon_max_file_size_mb
        if cover_photo_max_file_size_mb is not UNSET:
            field_dict["coverPhotoMaxFileSizeMb"] = cover_photo_max_file_size_mb
        if valid_cover_photo_dimensions is not UNSET:
            field_dict["validCoverPhotoDimensions"] = valid_cover_photo_dimensions
        if cost is not UNSET:
            field_dict["cost"] = cost
        if is_using_two_step_webview_component is not UNSET:
            field_dict["isUsingTwoStepWebviewComponent"] = is_using_two_step_webview_component

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name_max_length = d.pop("nameMaxLength", UNSET)

        description_max_length = d.pop("descriptionMaxLength", UNSET)

        icon_max_file_size_mb = d.pop("iconMaxFileSizeMb", UNSET)

        cover_photo_max_file_size_mb = d.pop("coverPhotoMaxFileSizeMb", UNSET)

        valid_cover_photo_dimensions = d.pop("validCoverPhotoDimensions", UNSET)

        cost = d.pop("cost", UNSET)

        is_using_two_step_webview_component = d.pop("isUsingTwoStepWebviewComponent", UNSET)

        roblox_groups_api_group_configuration_response = cls(
            name_max_length=name_max_length,
            description_max_length=description_max_length,
            icon_max_file_size_mb=icon_max_file_size_mb,
            cover_photo_max_file_size_mb=cover_photo_max_file_size_mb,
            valid_cover_photo_dimensions=valid_cover_photo_dimensions,
            cost=cost,
            is_using_two_step_webview_component=is_using_two_step_webview_component,
        )

        return roblox_groups_api_group_configuration_response
