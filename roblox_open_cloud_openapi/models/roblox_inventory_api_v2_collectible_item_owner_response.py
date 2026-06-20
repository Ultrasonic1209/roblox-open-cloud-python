from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_related_entity_type_response_roblox_agents_agent_type import (
        RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType,
    )


T = TypeVar("T", bound="RobloxInventoryApiV2CollectibleItemOwnerResponse")


@_attrs_define
class RobloxInventoryApiV2CollectibleItemOwnerResponse:
    """
    Attributes:
        collectible_item_instance_id (str | Unset):
        serial_number (int | Unset):
        owner (RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset):
    """

    collectible_item_instance_id: str | Unset = UNSET
    serial_number: int | Unset = UNSET
    owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collectible_item_instance_id = self.collectible_item_instance_id

        serial_number = self.serial_number

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collectible_item_instance_id is not UNSET:
            field_dict["collectibleItemInstanceId"] = collectible_item_instance_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_related_entity_type_response_roblox_agents_agent_type import (
            RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        collectible_item_instance_id = d.pop("collectibleItemInstanceId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType.from_dict(_owner)

        roblox_inventory_api_v2_collectible_item_owner_response = cls(
            collectible_item_instance_id=collectible_item_instance_id,
            serial_number=serial_number,
            owner=owner,
        )

        return roblox_inventory_api_v2_collectible_item_owner_response
