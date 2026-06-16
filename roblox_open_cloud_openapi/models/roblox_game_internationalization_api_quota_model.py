from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiQuotaModel")


@_attrs_define
class RobloxGameInternationalizationApiQuotaModel:
    """
    Attributes:
        remaining (int | Unset):
        capacity (int | Unset):
    """

    remaining: int | Unset = UNSET
    capacity: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        remaining = self.remaining

        capacity = self.capacity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remaining = d.pop("remaining", UNSET)

        capacity = d.pop("capacity", UNSET)

        roblox_game_internationalization_api_quota_model = cls(
            remaining=remaining,
            capacity=capacity,
        )

        return roblox_game_internationalization_api_quota_model
