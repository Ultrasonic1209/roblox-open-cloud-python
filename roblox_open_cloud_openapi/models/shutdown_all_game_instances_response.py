from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShutdownAllGameInstancesResponse")


@_attrs_define
class ShutdownAllGameInstancesResponse:
    """Shutdown All Game Instances response.

    Attributes:
        place_id (int | Unset): The place ID to shut down.
        replace_instances (bool | Unset): Whether to replace instances or not.
    """

    place_id: int | Unset = UNSET
    replace_instances: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        replace_instances = self.replace_instances

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if replace_instances is not UNSET:
            field_dict["replaceInstances"] = replace_instances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        replace_instances = d.pop("replaceInstances", UNSET)

        shutdown_all_game_instances_response = cls(
            place_id=place_id,
            replace_instances=replace_instances,
        )

        return shutdown_all_game_instances_response
