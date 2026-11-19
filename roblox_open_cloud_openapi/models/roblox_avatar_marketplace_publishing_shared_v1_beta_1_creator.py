from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_kind_case import (
    RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorKindCase,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_group import (
        RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup,
    )
    from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_user import (
        RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser,
    )


T = TypeVar("T", bound="RobloxAvatarMarketplacePublishingSharedV1Beta1Creator")


@_attrs_define
class RobloxAvatarMarketplacePublishingSharedV1Beta1Creator:
    """
    Attributes:
        user (RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser | Unset):
        group (RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup | Unset):
        kind_case (RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorKindCase | Unset):  ['None' = 0, 'User' = 1,
            'Group' = 2]
    """

    user: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser | Unset = UNSET
    group: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup | Unset = UNSET
    kind_case: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorKindCase | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        kind_case: int | Unset = UNSET
        if not isinstance(self.kind_case, Unset):
            kind_case = self.kind_case.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["User"] = user
        if group is not UNSET:
            field_dict["Group"] = group
        if kind_case is not UNSET:
            field_dict["KindCase"] = kind_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_group import (
            RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup,  # noqa: PLC0415
        )
        from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator_types_user import (
            RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _user = d.pop("User", UNSET)
        user: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesUser.from_dict(_user)

        _group = d.pop("Group", UNSET)
        group: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorTypesGroup.from_dict(_group)

        _kind_case = d.pop("KindCase", UNSET)
        kind_case: RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorKindCase | Unset
        if isinstance(_kind_case, Unset):
            kind_case = UNSET
        else:
            kind_case = RobloxAvatarMarketplacePublishingSharedV1Beta1CreatorKindCase(_kind_case)

        roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator = cls(
            user=user,
            group=group,
            kind_case=kind_case,
        )

        return roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator
