from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_configuration_response import RobloxGroupsApiGroupConfigurationResponse
    from ..models.roblox_groups_api_group_name_change_configuration_response import (
        RobloxGroupsApiGroupNameChangeConfigurationResponse,
    )
    from ..models.roblox_groups_api_recurring_payouts_configuration_response import (
        RobloxGroupsApiRecurringPayoutsConfigurationResponse,
    )
    from ..models.roblox_groups_api_role_configuration_response import RobloxGroupsApiRoleConfigurationResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupConfigurationDisplayOptionsResponse")


@_attrs_define
class RobloxGroupsApiGroupConfigurationDisplayOptionsResponse:
    """A response model for group configuration

    Attributes:
        group_configuration (RobloxGroupsApiGroupConfigurationResponse | Unset): A response model for group
            configuration
        recurring_payouts_configuration (RobloxGroupsApiRecurringPayoutsConfigurationResponse | Unset): A response model
            for recurring payout configuration
        role_configuration (RobloxGroupsApiRoleConfigurationResponse | Unset): A response model for role configuration
        group_name_change_configuration (RobloxGroupsApiGroupNameChangeConfigurationResponse | Unset):
        is_premium_payouts_enabled (bool | Unset): The configuration of premium payouts shows in Group Revenue Summary
            page
        is_default_emblem_policy_enabled (bool | Unset): If set to true, default group emblem policies handled by GUAC
            will be enabled

            If set to false, default group emblem policies will not be enabled
    """

    group_configuration: RobloxGroupsApiGroupConfigurationResponse | Unset = UNSET
    recurring_payouts_configuration: RobloxGroupsApiRecurringPayoutsConfigurationResponse | Unset = UNSET
    role_configuration: RobloxGroupsApiRoleConfigurationResponse | Unset = UNSET
    group_name_change_configuration: RobloxGroupsApiGroupNameChangeConfigurationResponse | Unset = UNSET
    is_premium_payouts_enabled: bool | Unset = UNSET
    is_default_emblem_policy_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_configuration, Unset):
            group_configuration = self.group_configuration.to_dict()

        recurring_payouts_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring_payouts_configuration, Unset):
            recurring_payouts_configuration = self.recurring_payouts_configuration.to_dict()

        role_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_configuration, Unset):
            role_configuration = self.role_configuration.to_dict()

        group_name_change_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_name_change_configuration, Unset):
            group_name_change_configuration = self.group_name_change_configuration.to_dict()

        is_premium_payouts_enabled = self.is_premium_payouts_enabled

        is_default_emblem_policy_enabled = self.is_default_emblem_policy_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_configuration is not UNSET:
            field_dict["groupConfiguration"] = group_configuration
        if recurring_payouts_configuration is not UNSET:
            field_dict["recurringPayoutsConfiguration"] = recurring_payouts_configuration
        if role_configuration is not UNSET:
            field_dict["roleConfiguration"] = role_configuration
        if group_name_change_configuration is not UNSET:
            field_dict["groupNameChangeConfiguration"] = group_name_change_configuration
        if is_premium_payouts_enabled is not UNSET:
            field_dict["isPremiumPayoutsEnabled"] = is_premium_payouts_enabled
        if is_default_emblem_policy_enabled is not UNSET:
            field_dict["isDefaultEmblemPolicyEnabled"] = is_default_emblem_policy_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_configuration_response import RobloxGroupsApiGroupConfigurationResponse
        from ..models.roblox_groups_api_group_name_change_configuration_response import (
            RobloxGroupsApiGroupNameChangeConfigurationResponse,
        )
        from ..models.roblox_groups_api_recurring_payouts_configuration_response import (
            RobloxGroupsApiRecurringPayoutsConfigurationResponse,
        )
        from ..models.roblox_groups_api_role_configuration_response import RobloxGroupsApiRoleConfigurationResponse

        d = dict(src_dict)
        _group_configuration = d.pop("groupConfiguration", UNSET)
        group_configuration: RobloxGroupsApiGroupConfigurationResponse | Unset
        if isinstance(_group_configuration, Unset):
            group_configuration = UNSET
        else:
            group_configuration = RobloxGroupsApiGroupConfigurationResponse.from_dict(_group_configuration)

        _recurring_payouts_configuration = d.pop("recurringPayoutsConfiguration", UNSET)
        recurring_payouts_configuration: RobloxGroupsApiRecurringPayoutsConfigurationResponse | Unset
        if isinstance(_recurring_payouts_configuration, Unset):
            recurring_payouts_configuration = UNSET
        else:
            recurring_payouts_configuration = RobloxGroupsApiRecurringPayoutsConfigurationResponse.from_dict(
                _recurring_payouts_configuration
            )

        _role_configuration = d.pop("roleConfiguration", UNSET)
        role_configuration: RobloxGroupsApiRoleConfigurationResponse | Unset
        if isinstance(_role_configuration, Unset):
            role_configuration = UNSET
        else:
            role_configuration = RobloxGroupsApiRoleConfigurationResponse.from_dict(_role_configuration)

        _group_name_change_configuration = d.pop("groupNameChangeConfiguration", UNSET)
        group_name_change_configuration: RobloxGroupsApiGroupNameChangeConfigurationResponse | Unset
        if isinstance(_group_name_change_configuration, Unset):
            group_name_change_configuration = UNSET
        else:
            group_name_change_configuration = RobloxGroupsApiGroupNameChangeConfigurationResponse.from_dict(
                _group_name_change_configuration
            )

        is_premium_payouts_enabled = d.pop("isPremiumPayoutsEnabled", UNSET)

        is_default_emblem_policy_enabled = d.pop("isDefaultEmblemPolicyEnabled", UNSET)

        roblox_groups_api_group_configuration_display_options_response = cls(
            group_configuration=group_configuration,
            recurring_payouts_configuration=recurring_payouts_configuration,
            role_configuration=role_configuration,
            group_name_change_configuration=group_name_change_configuration,
            is_premium_payouts_enabled=is_premium_payouts_enabled,
            is_default_emblem_policy_enabled=is_default_emblem_policy_enabled,
        )

        return roblox_groups_api_group_configuration_display_options_response
