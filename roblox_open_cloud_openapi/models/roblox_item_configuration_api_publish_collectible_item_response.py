from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_publish_collectible_item_response_status import (
    RobloxItemConfigurationApiPublishCollectibleItemResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiPublishCollectibleItemResponse")


@_attrs_define
class RobloxItemConfigurationApiPublishCollectibleItemResponse:
    """Response model for publishing a new CollectibleItem.

    Attributes:
        status (RobloxItemConfigurationApiPublishCollectibleItemResponseStatus | Unset): The status of the collectible
            being published. ['Succeeded' = 0, 'Failed' = 1, 'InProgress' = 2]
    """

    status: RobloxItemConfigurationApiPublishCollectibleItemResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RobloxItemConfigurationApiPublishCollectibleItemResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxItemConfigurationApiPublishCollectibleItemResponseStatus(_status)

        roblox_item_configuration_api_publish_collectible_item_response = cls(
            status=status,
        )

        return roblox_item_configuration_api_publish_collectible_item_response
