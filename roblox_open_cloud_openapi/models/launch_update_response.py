from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="LaunchUpdateResponse")


@_attrs_define
class LaunchUpdateResponse:
    """Launch Update response.

    Attributes:
        update_id (UUID): An ID for UI to query status of this update
        num_players_to_be_kicked (int): How many players are playing in servers that will be shut down according to the
            update configuration
        instances_to_be_closed (int): How many game instances will be closed according to the update configuration
    """

    update_id: UUID
    num_players_to_be_kicked: int
    instances_to_be_closed: int

    def to_dict(self) -> dict[str, Any]:
        update_id = str(self.update_id)

        num_players_to_be_kicked = self.num_players_to_be_kicked

        instances_to_be_closed = self.instances_to_be_closed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "updateId": update_id,
                "numPlayersToBeKicked": num_players_to_be_kicked,
                "instancesToBeClosed": instances_to_be_closed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_id = UUID(d.pop("updateId"))

        num_players_to_be_kicked = d.pop("numPlayersToBeKicked")

        instances_to_be_closed = d.pop("instancesToBeClosed")

        launch_update_response = cls(
            update_id=update_id,
            num_players_to_be_kicked=num_players_to_be_kicked,
            instances_to_be_closed=instances_to_be_closed,
        )

        return launch_update_response
