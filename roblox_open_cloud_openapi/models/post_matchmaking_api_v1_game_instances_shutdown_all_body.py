from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMatchmakingApiV1GameInstancesShutdownAllBody")


@_attrs_define
class PostMatchmakingApiV1GameInstancesShutdownAllBody:
    """
    Attributes:
        place_id (int | Unset): The place ID to shut down.
        replace_instances (bool | Unset): Whether to replace instances or not.
    """

    place_id: int | Unset = UNSET
    replace_instances: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        replace_instances = self.replace_instances

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place_id is not UNSET:
            field_dict["PlaceId"] = place_id
        if replace_instances is not UNSET:
            field_dict["ReplaceInstances"] = replace_instances

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.place_id, Unset):
            files.append(("PlaceId", (None, str(self.place_id).encode(), "text/plain")))

        if not isinstance(self.replace_instances, Unset):
            files.append(("ReplaceInstances", (None, str(self.replace_instances).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        place_id = d.pop("PlaceId", UNSET)

        replace_instances = d.pop("ReplaceInstances", UNSET)

        post_matchmaking_api_v1_game_instances_shutdown_all_body = cls(
            place_id=place_id,
            replace_instances=replace_instances,
        )

        post_matchmaking_api_v1_game_instances_shutdown_all_body.additional_properties = d
        return post_matchmaking_api_v1_game_instances_shutdown_all_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
