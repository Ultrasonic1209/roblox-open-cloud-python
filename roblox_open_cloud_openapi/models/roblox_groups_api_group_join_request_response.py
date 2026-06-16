from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel


T = TypeVar("T", bound="RobloxGroupsApiGroupJoinRequestResponse")


@_attrs_define
class RobloxGroupsApiGroupJoinRequestResponse:
    """Response model for a group join request

    Attributes:
        requester (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        created (datetime.datetime | Unset): The DateTime the request was created
    """

    requester: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        requester: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requester, Unset):
            requester = self.requester.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if requester is not UNSET:
            field_dict["requester"] = requester
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel

        d = dict(src_dict)
        _requester = d.pop("requester", UNSET)
        requester: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_requester, Unset):
            requester = UNSET
        else:
            requester = RobloxGroupsApiModelsResponseUserModel.from_dict(_requester)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_groups_api_group_join_request_response = cls(
            requester=requester,
            created=created,
        )

        return roblox_groups_api_group_join_request_response
