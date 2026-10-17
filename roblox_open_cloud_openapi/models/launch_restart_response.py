from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaunchRestartResponse")


@_attrs_define
class LaunchRestartResponse:
    """Response model for launching a game restart.

    Attributes:
        id (None | str | Unset): ID of the restart.
        players_impacted (int | Unset): Number of players in instances that will be shut down.
        instances_impacted (int | Unset): Number of game instances that will be closed.
    """

    id: None | str | Unset = UNSET
    players_impacted: int | Unset = UNSET
    instances_impacted: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        players_impacted = self.players_impacted

        instances_impacted = self.instances_impacted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if players_impacted is not UNSET:
            field_dict["playersImpacted"] = players_impacted
        if instances_impacted is not UNSET:
            field_dict["instancesImpacted"] = instances_impacted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        players_impacted = d.pop("playersImpacted", UNSET)

        instances_impacted = d.pop("instancesImpacted", UNSET)

        launch_restart_response = cls(
            id=id,
            players_impacted=players_impacted,
            instances_impacted=instances_impacted,
        )

        return launch_restart_response
