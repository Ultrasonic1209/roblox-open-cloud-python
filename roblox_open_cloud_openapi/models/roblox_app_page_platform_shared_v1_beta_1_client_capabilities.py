from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_enabled_capabilities_item import (
    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesEnabledCapabilitiesItem,
)
from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_platform import (
    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesPlatform,
)
from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_registered_action_types_item import (
    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredActionTypesItem,
)
from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_registered_ui_component_types_item import (
    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredUiComponentTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_runtime_flag_values import (
        RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues,
    )


T = TypeVar("T", bound="RobloxAppPagePlatformSharedV1Beta1ClientCapabilities")


@_attrs_define
class RobloxAppPagePlatformSharedV1Beta1ClientCapabilities:
    """
    Attributes:
        enabled_capabilities (list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesEnabledCapabilitiesItem] |
            Unset):
        proto_version (str | Unset):
        platform (RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesPlatform | Unset):  ['Invalid' = 0, 'Web' = 1,
            'App' = 2]
        registered_ui_component_types
            (list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredUiComponentTypesItem] | Unset):
        registered_action_types (list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredActionTypesItem] |
            Unset):
        runtime_flag_values (RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues | Unset):
    """

    enabled_capabilities: list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesEnabledCapabilitiesItem] | Unset = (
        UNSET
    )
    proto_version: str | Unset = UNSET
    platform: RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesPlatform | Unset = UNSET
    registered_ui_component_types: (
        list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredUiComponentTypesItem] | Unset
    ) = UNSET
    registered_action_types: (
        list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredActionTypesItem] | Unset
    ) = UNSET
    runtime_flag_values: RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled_capabilities: list[int] | Unset = UNSET
        if not isinstance(self.enabled_capabilities, Unset):
            enabled_capabilities = []
            for enabled_capabilities_item_data in self.enabled_capabilities:
                enabled_capabilities_item = enabled_capabilities_item_data.value
                enabled_capabilities.append(enabled_capabilities_item)

        proto_version = self.proto_version

        platform: int | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        registered_ui_component_types: list[int] | Unset = UNSET
        if not isinstance(self.registered_ui_component_types, Unset):
            registered_ui_component_types = []
            for registered_ui_component_types_item_data in self.registered_ui_component_types:
                registered_ui_component_types_item = registered_ui_component_types_item_data.value
                registered_ui_component_types.append(registered_ui_component_types_item)

        registered_action_types: list[int] | Unset = UNSET
        if not isinstance(self.registered_action_types, Unset):
            registered_action_types = []
            for registered_action_types_item_data in self.registered_action_types:
                registered_action_types_item = registered_action_types_item_data.value
                registered_action_types.append(registered_action_types_item)

        runtime_flag_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime_flag_values, Unset):
            runtime_flag_values = self.runtime_flag_values.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled_capabilities is not UNSET:
            field_dict["EnabledCapabilities"] = enabled_capabilities
        if proto_version is not UNSET:
            field_dict["ProtoVersion"] = proto_version
        if platform is not UNSET:
            field_dict["Platform"] = platform
        if registered_ui_component_types is not UNSET:
            field_dict["RegisteredUiComponentTypes"] = registered_ui_component_types
        if registered_action_types is not UNSET:
            field_dict["RegisteredActionTypes"] = registered_action_types
        if runtime_flag_values is not UNSET:
            field_dict["RuntimeFlagValues"] = runtime_flag_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities_runtime_flag_values import (
            RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _enabled_capabilities = d.pop("EnabledCapabilities", UNSET)
        enabled_capabilities: (
            list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesEnabledCapabilitiesItem] | Unset
        ) = UNSET
        if _enabled_capabilities is not UNSET:
            enabled_capabilities = []
            for enabled_capabilities_item_data in _enabled_capabilities:
                enabled_capabilities_item = RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesEnabledCapabilitiesItem(
                    enabled_capabilities_item_data
                )

                enabled_capabilities.append(enabled_capabilities_item)

        proto_version = d.pop("ProtoVersion", UNSET)

        _platform = d.pop("Platform", UNSET)
        platform: RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesPlatform(_platform)

        _registered_ui_component_types = d.pop("RegisteredUiComponentTypes", UNSET)
        registered_ui_component_types: (
            list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredUiComponentTypesItem] | Unset
        ) = UNSET
        if _registered_ui_component_types is not UNSET:
            registered_ui_component_types = []
            for registered_ui_component_types_item_data in _registered_ui_component_types:
                registered_ui_component_types_item = (
                    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredUiComponentTypesItem(
                        registered_ui_component_types_item_data
                    )
                )

                registered_ui_component_types.append(registered_ui_component_types_item)

        _registered_action_types = d.pop("RegisteredActionTypes", UNSET)
        registered_action_types: (
            list[RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredActionTypesItem] | Unset
        ) = UNSET
        if _registered_action_types is not UNSET:
            registered_action_types = []
            for registered_action_types_item_data in _registered_action_types:
                registered_action_types_item = (
                    RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRegisteredActionTypesItem(
                        registered_action_types_item_data
                    )
                )

                registered_action_types.append(registered_action_types_item)

        _runtime_flag_values = d.pop("RuntimeFlagValues", UNSET)
        runtime_flag_values: RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues | Unset
        if isinstance(_runtime_flag_values, Unset):
            runtime_flag_values = UNSET
        else:
            runtime_flag_values = RobloxAppPagePlatformSharedV1Beta1ClientCapabilitiesRuntimeFlagValues.from_dict(
                _runtime_flag_values
            )

        roblox_app_page_platform_shared_v1_beta_1_client_capabilities = cls(
            enabled_capabilities=enabled_capabilities,
            proto_version=proto_version,
            platform=platform,
            registered_ui_component_types=registered_ui_component_types,
            registered_action_types=registered_action_types,
            runtime_flag_values=runtime_flag_values,
        )

        return roblox_app_page_platform_shared_v1_beta_1_client_capabilities
