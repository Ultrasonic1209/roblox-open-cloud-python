from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponseMetadataPermissions:
    """Permissions for configured metadata values. Key is MetadataName string (e.g., "EmissiveResult").
    Absent keys are unrestricted (allowed). Null when metadata permissions are not available.

    """

    additional_properties: dict[str, bool] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response_metadata_permissions = (
            cls()
        )

        roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response_metadata_permissions.additional_properties = d
        return (
            roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response_metadata_permissions
        )

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
