from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_playtester_eligibility import RobloxApiDevelopModelsPlaytesterEligibility


T = TypeVar("T", bound="RobloxApiDevelopModelsPlaytesterEligibilityResponse")


@_attrs_define
class RobloxApiDevelopModelsPlaytesterEligibilityResponse:
    """Per-user add eligibility for private playtester candidates.

    Attributes:
        playtesters (list[RobloxApiDevelopModelsPlaytesterEligibility] | Unset): The per-user eligibility results.
    """

    playtesters: list[RobloxApiDevelopModelsPlaytesterEligibility] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playtesters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.playtesters, Unset):
            playtesters = []
            for playtesters_item_data in self.playtesters:
                playtesters_item = playtesters_item_data.to_dict()
                playtesters.append(playtesters_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playtesters is not UNSET:
            field_dict["playtesters"] = playtesters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_playtester_eligibility import (
            RobloxApiDevelopModelsPlaytesterEligibility,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _playtesters = d.pop("playtesters", UNSET)
        playtesters: list[RobloxApiDevelopModelsPlaytesterEligibility] | Unset = UNSET
        if _playtesters is not UNSET:
            playtesters = []
            for playtesters_item_data in _playtesters:
                playtesters_item = RobloxApiDevelopModelsPlaytesterEligibility.from_dict(playtesters_item_data)

                playtesters.append(playtesters_item)

        roblox_api_develop_models_playtester_eligibility_response = cls(
            playtesters=playtesters,
        )

        return roblox_api_develop_models_playtester_eligibility_response
