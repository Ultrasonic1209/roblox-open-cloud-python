from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsTeamCreateMembershipRequest")


@_attrs_define
class RobloxApiDevelopModelsTeamCreateMembershipRequest:
    """Request model for a TeamCreate membership

    Attributes:
        user_id (int | Unset): The id of the user.
    """

    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        roblox_api_develop_models_team_create_membership_request = cls(
            user_id=user_id,
        )

        return roblox_api_develop_models_team_create_membership_request
