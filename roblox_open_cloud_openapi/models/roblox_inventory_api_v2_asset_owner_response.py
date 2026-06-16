from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_related_entity_type_response_roblox_agents_agent_type import (
        RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType,
    )


T = TypeVar("T", bound="RobloxInventoryApiV2AssetOwnerResponse")


@_attrs_define
class RobloxInventoryApiV2AssetOwnerResponse:
    """
    Attributes:
        id (int | Unset):
        collectible_item_instance_id (str | Unset):
        serial_number (int | Unset):
        owner (RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset):
        created (datetime.datetime | Unset):
        updated (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    collectible_item_instance_id: str | Unset = UNSET
    serial_number: int | Unset = UNSET
    owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        collectible_item_instance_id = self.collectible_item_instance_id

        serial_number = self.serial_number

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if collectible_item_instance_id is not UNSET:
            field_dict["collectibleItemInstanceId"] = collectible_item_instance_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if owner is not UNSET:
            field_dict["owner"] = owner
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_related_entity_type_response_roblox_agents_agent_type import (
            RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        collectible_item_instance_id = d.pop("collectibleItemInstanceId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxWebResponsesRelatedEntityTypeResponseRobloxAgentsAgentType.from_dict(_owner)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        roblox_inventory_api_v2_asset_owner_response = cls(
            id=id,
            collectible_item_instance_id=collectible_item_instance_id,
            serial_number=serial_number,
            owner=owner,
            created=created,
            updated=updated,
        )

        return roblox_inventory_api_v2_asset_owner_response
