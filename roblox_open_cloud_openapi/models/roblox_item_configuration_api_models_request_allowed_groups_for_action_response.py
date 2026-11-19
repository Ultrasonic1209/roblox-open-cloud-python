from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_group_info import (
        RobloxItemConfigurationApiModelsResponseGroupInfo,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse:
    """The response DTO for the allowed groups for a specified Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.

    Attributes:
        allowed_groups (list[RobloxItemConfigurationApiModelsResponseGroupInfo] | Unset): The list of groups allowed for
            the user for the given action.
    """

    allowed_groups: list[RobloxItemConfigurationApiModelsResponseGroupInfo] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowed_groups, Unset):
            allowed_groups = []
            for allowed_groups_item_data in self.allowed_groups:
                allowed_groups_item = allowed_groups_item_data.to_dict()
                allowed_groups.append(allowed_groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_groups is not UNSET:
            field_dict["allowedGroups"] = allowed_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_group_info import (
            RobloxItemConfigurationApiModelsResponseGroupInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _allowed_groups = d.pop("allowedGroups", UNSET)
        allowed_groups: list[RobloxItemConfigurationApiModelsResponseGroupInfo] | Unset = UNSET
        if _allowed_groups is not UNSET:
            allowed_groups = []
            for allowed_groups_item_data in _allowed_groups:
                allowed_groups_item = RobloxItemConfigurationApiModelsResponseGroupInfo.from_dict(
                    allowed_groups_item_data
                )

                allowed_groups.append(allowed_groups_item)

        roblox_item_configuration_api_models_request_allowed_groups_for_action_response = cls(
            allowed_groups=allowed_groups,
        )

        return roblox_item_configuration_api_models_request_allowed_groups_for_action_response
