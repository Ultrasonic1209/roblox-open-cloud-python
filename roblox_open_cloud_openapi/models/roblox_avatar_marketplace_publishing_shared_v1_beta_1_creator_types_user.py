from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser")


@_attrs_define
class RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser:
    """
    Attributes:
        user_id (int | Unset):
    """

    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("UserId", UNSET)

        roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_user = cls(
            user_id=user_id,
        )

        return roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_user
