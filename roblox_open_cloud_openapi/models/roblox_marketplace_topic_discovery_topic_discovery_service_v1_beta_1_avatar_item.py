from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_avatar_item_item_type import (
    RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItemItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem")


@_attrs_define
class RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem:
    """
    Attributes:
        target_id (int | Unset):
        item_type (RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItemItemType | Unset):  ['Invalid' =
            0, 'Asset' = 1, 'Bundle' = 2]
    """

    target_id: int | Unset = UNSET
    item_type: RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItemItemType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        item_type: int | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_id is not UNSET:
            field_dict["TargetId"] = target_id
        if item_type is not UNSET:
            field_dict["ItemType"] = item_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_id = d.pop("TargetId", UNSET)

        _item_type = d.pop("ItemType", UNSET)
        item_type: RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItemItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItemItemType(_item_type)

        roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_avatar_item = cls(
            target_id=target_id,
            item_type=item_type,
        )

        return roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_avatar_item
