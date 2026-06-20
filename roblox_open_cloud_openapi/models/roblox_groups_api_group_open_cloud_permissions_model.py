from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupOpenCloudPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupOpenCloudPermissionsModel:
    """
    Attributes:
        use_cloud_authentication (bool | Unset): Permission to create and use API keys on the group's resources.
        administer_cloud_authentication (bool | Unset): Permission to administer all of the group's API keys.
    """

    use_cloud_authentication: bool | Unset = UNSET
    administer_cloud_authentication: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        use_cloud_authentication = self.use_cloud_authentication

        administer_cloud_authentication = self.administer_cloud_authentication

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if use_cloud_authentication is not UNSET:
            field_dict["useCloudAuthentication"] = use_cloud_authentication
        if administer_cloud_authentication is not UNSET:
            field_dict["administerCloudAuthentication"] = administer_cloud_authentication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        use_cloud_authentication = d.pop("useCloudAuthentication", UNSET)

        administer_cloud_authentication = d.pop("administerCloudAuthentication", UNSET)

        roblox_groups_api_group_open_cloud_permissions_model = cls(
            use_cloud_authentication=use_cloud_authentication,
            administer_cloud_authentication=administer_cloud_authentication,
        )

        return roblox_groups_api_group_open_cloud_permissions_model
