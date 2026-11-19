from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse")


@_attrs_define
class RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse:
    """GetGroupSnapshotRobuxResponse.

    Attributes:
        robux_at_35 (int | Unset): Snapshot robux at the given rate.
    """

    robux_at_35: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        robux_at_35 = self.robux_at_35

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if robux_at_35 is not UNSET:
            field_dict["robuxAt35"] = robux_at_35

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        robux_at_35 = d.pop("robuxAt35", UNSET)

        roblox_economy_api_models_get_group_snapshot_robux_response = cls(
            robux_at_35=robux_at_35,
        )

        return roblox_economy_api_models_get_group_snapshot_robux_response
