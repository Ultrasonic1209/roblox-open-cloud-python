from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.period import Period
from ..models.quota_type import QuotaType
from ..models.roblox_open_cloud_cloud_v2_asset_type import RobloxOpenCloudCloudV2AssetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetQuota")


@_attrs_define
class AssetQuota:
    """Represents a quota for an asset-related action.

    For example, a user might be able to upload 100 audio files per month and
    have uploaded 15 already. In this example:
    - `quotaType` is `RATE_LIMIT_UPLOAD`
    - `assetType` is `AUDIO`
    - `usage` is `15`
    - `capacity` is `100`
    - `period` is `MONTH`
    `usageResetTime` indicates when a new period begins and usage resets to 0.
    This value **doesn't** necessarily correlate with the first day of a
    calendar month or midnight on a given day. For more information on the
    upload process, see the
    [usage
    guide](https://create.roblox.com/docs/en-us/cloud/open-cloud/usage-assets).

        Attributes:
            path (None | str | Unset): The resource path of the asset quota.

                Format: `users/{user_id}/asset-quotas/{asset_quota_id}` Example: users/123/asset-quotas/some-asset-quota.
            quota_type (QuotaType | Unset): Quota type.
            asset_type (RobloxOpenCloudCloudV2AssetType | Unset): Type of the Asset.
            usage (str | Unset): The current usage of the quota.
            capacity (str | Unset): The capacity of the quota.
            period (Period | Unset): Period of time the quota is for.
            usage_reset_time (datetime.datetime | None | Unset): The time the usage will reset for this quota. Example:
                2023-07-05T12:34:56Z.
    """

    path: None | str | Unset = UNSET
    quota_type: QuotaType | Unset = UNSET
    asset_type: RobloxOpenCloudCloudV2AssetType | Unset = UNSET
    usage: str | Unset = UNSET
    capacity: str | Unset = UNSET
    period: Period | Unset = UNSET
    usage_reset_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        quota_type: str | Unset = UNSET
        if not isinstance(self.quota_type, Unset):
            quota_type = self.quota_type.value

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        usage = self.usage

        capacity = self.capacity

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        usage_reset_time: None | str | Unset
        if isinstance(self.usage_reset_time, Unset):
            usage_reset_time = UNSET
        elif isinstance(self.usage_reset_time, datetime.datetime):
            usage_reset_time = self.usage_reset_time.isoformat()
        else:
            usage_reset_time = self.usage_reset_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if quota_type is not UNSET:
            field_dict["quotaType"] = quota_type
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if usage is not UNSET:
            field_dict["usage"] = usage
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if period is not UNSET:
            field_dict["period"] = period
        if usage_reset_time is not UNSET:
            field_dict["usageResetTime"] = usage_reset_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        _quota_type = d.pop("quotaType", UNSET)
        quota_type: QuotaType | Unset
        if isinstance(_quota_type, Unset):
            quota_type = UNSET
        else:
            quota_type = QuotaType(_quota_type)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: RobloxOpenCloudCloudV2AssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = RobloxOpenCloudCloudV2AssetType(_asset_type)

        usage = d.pop("usage", UNSET)

        capacity = d.pop("capacity", UNSET)

        _period = d.pop("period", UNSET)
        period: Period | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = Period(_period)

        def _parse_usage_reset_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                usage_reset_time_type_0 = datetime.datetime.fromisoformat(data)

                return usage_reset_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        usage_reset_time = _parse_usage_reset_time(d.pop("usageResetTime", UNSET))

        asset_quota = cls(
            path=path,
            quota_type=quota_type,
            asset_type=asset_type,
            usage=usage,
            capacity=capacity,
            period=period,
            usage_reset_time=usage_reset_time,
        )

        return asset_quota
