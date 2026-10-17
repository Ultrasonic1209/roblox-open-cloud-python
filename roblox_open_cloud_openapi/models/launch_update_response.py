from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaunchUpdateResponse")


@_attrs_define
class LaunchUpdateResponse:
    """Launch Update response.

    Attributes:
        update_id (UUID | Unset): An ID for UI to query status of this update
        num_players_to_be_kicked (int | Unset): How many players are playing in servers that will be shut down according
            to the update configuration
        instances_to_be_closed (int | Unset): How many game instances will be closed according to the update
            configuration
    """

    update_id: UUID | Unset = UNSET
    num_players_to_be_kicked: int | Unset = UNSET
    instances_to_be_closed: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_id: str | Unset = UNSET
        if not isinstance(self.update_id, Unset):
            update_id = str(self.update_id)

        num_players_to_be_kicked = self.num_players_to_be_kicked

        instances_to_be_closed = self.instances_to_be_closed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_id is not UNSET:
            field_dict["updateId"] = update_id
        if num_players_to_be_kicked is not UNSET:
            field_dict["numPlayersToBeKicked"] = num_players_to_be_kicked
        if instances_to_be_closed is not UNSET:
            field_dict["instancesToBeClosed"] = instances_to_be_closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _update_id = d.pop("updateId", UNSET)
        update_id: UUID | Unset
        if isinstance(_update_id, Unset):
            update_id = UNSET
        else:
            update_id = UUID(_update_id)

        num_players_to_be_kicked = d.pop("numPlayersToBeKicked", UNSET)

        instances_to_be_closed = d.pop("instancesToBeClosed", UNSET)

        launch_update_response = cls(
            update_id=update_id,
            num_players_to_be_kicked=num_players_to_be_kicked,
            instances_to_be_closed=instances_to_be_closed,
        )

        return launch_update_response
