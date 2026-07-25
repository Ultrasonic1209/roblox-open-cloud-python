from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaytestersRequest")


@_attrs_define
class RobloxApiDevelopModelsPlaytestersRequest:
    """Request model for adding or removing playtesters.

    Attributes:
        playtesters (list[int] | Unset): The user ids to add or remove as playtesters for this universe.
    """

    playtesters: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playtesters: list[int] | Unset = UNSET
        if not isinstance(self.playtesters, Unset):
            playtesters = self.playtesters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playtesters is not UNSET:
            field_dict["playtesters"] = playtesters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        playtesters = cast(list[int], d.pop("playtesters", UNSET))

        roblox_api_develop_models_playtesters_request = cls(
            playtesters=playtesters,
        )

        return roblox_api_develop_models_playtesters_request
