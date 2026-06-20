from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_models_response_user_model_builders_club_membership_type import (
    RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiModelsResponseUserModel")


@_attrs_define
class RobloxGroupsApiModelsResponseUserModel:
    """A model representing data about an Roblox.Platform.Membership.IUser

    Attributes:
        builders_club_membership_type (RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType | Unset): The
            user's builders club membership type
        has_verified_badge (bool | Unset): The user's verified badge status.
        user_id (int | Unset):
        username (str | Unset):
        display_name (str | Unset):
    """

    builders_club_membership_type: RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    user_id: int | Unset = UNSET
    username: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        builders_club_membership_type: int | Unset = UNSET
        if not isinstance(self.builders_club_membership_type, Unset):
            builders_club_membership_type = self.builders_club_membership_type.value

        has_verified_badge = self.has_verified_badge

        user_id = self.user_id

        username = self.username

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if builders_club_membership_type is not UNSET:
            field_dict["buildersClubMembershipType"] = builders_club_membership_type
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _builders_club_membership_type = d.pop("buildersClubMembershipType", UNSET)
        builders_club_membership_type: RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType | Unset
        if isinstance(_builders_club_membership_type, Unset):
            builders_club_membership_type = UNSET
        else:
            builders_club_membership_type = RobloxGroupsApiModelsResponseUserModelBuildersClubMembershipType(
                _builders_club_membership_type
            )

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_groups_api_models_response_user_model = cls(
            builders_club_membership_type=builders_club_membership_type,
            has_verified_badge=has_verified_badge,
            user_id=user_id,
            username=username,
            display_name=display_name,
        )

        return roblox_groups_api_models_response_user_model
