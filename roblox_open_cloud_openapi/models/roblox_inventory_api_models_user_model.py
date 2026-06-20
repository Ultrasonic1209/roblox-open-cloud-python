from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_inventory_api_models_user_model_builders_club_membership_type import (
    RobloxInventoryApiModelsUserModelBuildersClubMembershipType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiModelsUserModel")


@_attrs_define
class RobloxInventoryApiModelsUserModel:
    """A model representing data about an Roblox.Platform.Membership.IUser

    Attributes:
        user_id (int | Unset): The user id
        username (str | Unset): The username
        builders_club_membership_type (RobloxInventoryApiModelsUserModelBuildersClubMembershipType | Unset): The user's
            builders club membership type ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium' = 4]
    """

    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    builders_club_membership_type: RobloxInventoryApiModelsUserModelBuildersClubMembershipType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        username = self.username

        builders_club_membership_type: int | Unset = UNSET
        if not isinstance(self.builders_club_membership_type, Unset):
            builders_club_membership_type = self.builders_club_membership_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if builders_club_membership_type is not UNSET:
            field_dict["buildersClubMembershipType"] = builders_club_membership_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        _builders_club_membership_type = d.pop("buildersClubMembershipType", UNSET)
        builders_club_membership_type: RobloxInventoryApiModelsUserModelBuildersClubMembershipType | Unset
        if isinstance(_builders_club_membership_type, Unset):
            builders_club_membership_type = UNSET
        else:
            builders_club_membership_type = RobloxInventoryApiModelsUserModelBuildersClubMembershipType(
                _builders_club_membership_type
            )

        roblox_inventory_api_models_user_model = cls(
            user_id=user_id,
            username=username,
            builders_club_membership_type=builders_club_membership_type,
        )

        return roblox_inventory_api_models_user_model
