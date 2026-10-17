from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPublishApiAssetQuota")


@_attrs_define
class RobloxPublishApiAssetQuota:
    """Model for asset quota.

    Attributes:
        duration (str | Unset): Duration type of the quota.
        usage (int | Unset): Current usage of the quota.
        capacity (int | Unset): Capacity of the quota.
        expiration_time (str | Unset): Expiration time of current usage limit.
    """

    duration: str | Unset = UNSET
    usage: int | Unset = UNSET
    capacity: int | Unset = UNSET
    expiration_time: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        usage = self.usage

        capacity = self.capacity

        expiration_time = self.expiration_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if usage is not UNSET:
            field_dict["usage"] = usage
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        usage = d.pop("usage", UNSET)

        capacity = d.pop("capacity", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        roblox_publish_api_asset_quota = cls(
            duration=duration,
            usage=usage,
            capacity=capacity,
            expiration_time=expiration_time,
        )

        return roblox_publish_api_asset_quota
