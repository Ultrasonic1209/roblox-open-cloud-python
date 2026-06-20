from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiGroupPayoutResponse")


@_attrs_define
class RobloxGroupsApiGroupPayoutResponse:
    """A group payout response

    Attributes:
        user (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        percentage (int | Unset): The group payout percentage for the user
    """

    user: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    percentage: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user = d.pop("user", UNSET)
        user: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxGroupsApiModelsResponseUserModel.from_dict(_user)

        percentage = d.pop("percentage", UNSET)

        roblox_groups_api_group_payout_response = cls(
            user=user,
            percentage=percentage,
        )

        return roblox_groups_api_group_payout_response
