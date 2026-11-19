from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_item_delisting_status_status import (
    RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatusStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_target import (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target,
    )


T = TypeVar("T", bound="RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus")


@_attrs_define
class RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus:
    """
    Attributes:
        target (RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target | Unset):
        status (RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatusStatus |
            Unset):  ['Invalid' = 0, 'Delisted' = 1, 'NotDelisted' = 2]
    """

    target: RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target | Unset = UNSET
    status: (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatusStatus | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target is not UNSET:
            field_dict["Target"] = target
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_target import (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _target = d.pop("Target", UNSET)
        target: RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1Target.from_dict(_target)

        _status = d.pop("Status", UNSET)
        status: (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatusStatus | Unset
        )
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = (
                RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatusStatus(
                    _status
                )
            )

        roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_item_delisting_status = (
            cls(
                target=target,
                status=status,
            )
        )

        return (
            roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_item_delisting_status
        )
