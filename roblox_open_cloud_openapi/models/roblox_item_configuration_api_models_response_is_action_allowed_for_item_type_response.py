from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response_metadata_permissions import (
        RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse:
    """Result of checking whether a marketplace action is allowed for a specific item type for the agent.

    Attributes:
        is_action_allowed (bool | Unset): Whether the action is allowed for the given item type and agent.
        metadata_permissions
            (RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions | Unset):
            Permissions for configured metadata values. Key is MetadataName string (e.g., "EmissiveResult").
            Absent keys are unrestricted (allowed). Null when metadata permissions are not available.
    """

    is_action_allowed: bool | Unset = UNSET
    metadata_permissions: (
        RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_action_allowed = self.is_action_allowed

        metadata_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_permissions, Unset):
            metadata_permissions = self.metadata_permissions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_action_allowed is not UNSET:
            field_dict["isActionAllowed"] = is_action_allowed
        if metadata_permissions is not UNSET:
            field_dict["metadataPermissions"] = metadata_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response_metadata_permissions import (
            RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions,  # noqa: PLC0415
        )

        d = dict(src_dict)
        is_action_allowed = d.pop("isActionAllowed", UNSET)

        _metadata_permissions = d.pop("metadataPermissions", UNSET)
        metadata_permissions: (
            RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions | Unset
        )
        if isinstance(_metadata_permissions, Unset):
            metadata_permissions = UNSET
        else:
            metadata_permissions = (
                RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions.from_dict(
                    _metadata_permissions
                )
            )

        roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response = cls(
            is_action_allowed=is_action_allowed,
            metadata_permissions=metadata_permissions,
        )

        return roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response
