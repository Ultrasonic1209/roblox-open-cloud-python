from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_target_target_type import (
    RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1TargetTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target")


@_attrs_define
class RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target:
    """
    Attributes:
        target_type (RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1TargetTargetType |
            Unset):  ['Invalid' = 0, 'Asset' = 1, 'Bundle' = 2, 'AvatarMarketplaceToken' = 3, 'Look' = 4]
        id (str | Unset):
    """

    target_type: RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1TargetTargetType | Unset = (
        UNSET
    )
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["TargetType"] = target_type
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("TargetType", UNSET)
        target_type: RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1TargetTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1TargetTargetType(
                _target_type
            )

        id = d.pop("Id", UNSET)

        roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_target = cls(
            target_type=target_type,
            id=id,
        )

        return roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_target
