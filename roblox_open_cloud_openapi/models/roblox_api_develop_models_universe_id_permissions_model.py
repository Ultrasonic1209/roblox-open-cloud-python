from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseIdPermissionsModel")


@_attrs_define
class RobloxApiDevelopModelsUniverseIdPermissionsModel:
    """A model containing information about a universe permissions

    Attributes:
        universe_id (int | Unset): The universe Id these permissions reference
        can_manage (bool | Unset): Determines whether or not consumer can manage the target universe
        can_cloud_edit (bool | Unset): Determines whether or not consumer can cloud the target universe
            This is only nullable/optional in the context of
            https://develop.roblox.com/docs#!/Universes/get_v1_universes_universeId_context_permissions endpoint which is
            consumed only internally. It should be computed and set for all other usages.
    """

    universe_id: int | Unset = UNSET
    can_manage: bool | Unset = UNSET
    can_cloud_edit: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        can_manage = self.can_manage

        can_cloud_edit = self.can_cloud_edit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if can_manage is not UNSET:
            field_dict["canManage"] = can_manage
        if can_cloud_edit is not UNSET:
            field_dict["canCloudEdit"] = can_cloud_edit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        can_manage = d.pop("canManage", UNSET)

        can_cloud_edit = d.pop("canCloudEdit", UNSET)

        roblox_api_develop_models_universe_id_permissions_model = cls(
            universe_id=universe_id,
            can_manage=can_manage,
            can_cloud_edit=can_cloud_edit,
        )

        return roblox_api_develop_models_universe_id_permissions_model
