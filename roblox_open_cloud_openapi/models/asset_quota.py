from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_quota_asset_type import AssetQuotaAssetType
from ..models.asset_quota_period import AssetQuotaPeriod
from ..models.asset_quota_quota_type import AssetQuotaQuotaType
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
            path (str | Unset): The resource path of the asset quota.

                Format: `users/{user_id}/asset-quotas/{asset_quota_id}` Example: users/123/asset-quotas/some-asset-quota.
            quota_type (AssetQuotaQuotaType | Unset): Type of quota.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | QUOTA_TYPE_UNSPECIFIED | The default quota type. |
                  | RATE_LIMIT_UPLOAD | Rate limit on how often one can upload an asset. |
                  | RATE_LIMIT_CREATOR_STORE_DISTRIBUTE | Rate limit on how often one can distribute an asset on the Creator
                Store. | Example: QUOTA_TYPE_UNSPECIFIED.
            asset_type (AssetQuotaAssetType | Unset): The asset type the quota is for.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | ASSET_TYPE_UNSPECIFIED | The default asset type. |
                  | IMAGE | Image |
                  | TSHIRT | Tshirt |
                  | AUDIO | Audio |
                  | MESH | Mesh |
                  | LUA | Lua |
                  | HAT | Hat |
                  | PLACE | Place |
                  | MODEL | Model |
                  | SHIRT | Classic Shirt |
                  | PANTS | Classic Pants |
                  | DECAL | Decal |
                  | HEAD | Head |
                  | FACE | Face |
                  | GEAR | Gear |
                  | ANIMATION | Animation |
                  | TORSO | Torso |
                  | RIGHT_ARM | Right Arm |
                  | LEFT_ARM | Left Arm |
                  | LEFT_LEG | Left Leg |
                  | RIGHT_LEG | Right Leg |
                  | YOUTUBE_VIDEO | YouTube Video |
                  | APP | App |
                  | CODE | Code |
                  | PLUGIN | Plugin |
                  | SOLID_MODEL | Solid Model |
                  | MESH_PART | Mesh Part |
                  | HAIR_ACCESSORY | Hair Accessory |
                  | FACE_ACCESSORY | Face Accessory |
                  | NECK_ACCESSORY | Neck Accessory |
                  | SHOULDER_ACCESSORY | Shoulder Accessory |
                  | FRONT_ACCESSORY | Front Accessory |
                  | BACK_ACCESSORY | Back Accessory |
                  | WAIST_ACCESSORY | Waist Accessory |
                  | CLIMB_ANIMATION | Climb Animation |
                  | DEATH_ANIMATION | Death Animation |
                  | FALL_ANIMATION | Fall Animation |
                  | IDLE_ANIMATION | Idle Animation |
                  | JUMP_ANIMATION | Jump Animation |
                  | RUN_ANIMATION | Run Animation |
                  | SWIM_ANIMATION | Swim Animation |
                  | WALK_ANIMATION | Walk Animation |
                  | POSE_ANIMATION | Pose Animation |
                  | LOCALIZATION_TABLE_MANIFEST | Localization Table Manifest |
                  | LOCALIZATION_TABLE_TRANSLATION | Localization Table Translation |
                  | EMOTE_ANIMATION | Emote Animation |
                  | VIDEO | Video |
                  | TEXTURE_PACK | Texture Pack |
                  | TSHIRT_ACCESSORY | Tshirt Accessory |
                  | SHIRT_ACCESSORY | Shirt Accessory |
                  | PANTS_ACCESSORY | Pants Accessory |
                  | JACKET_ACCESSORY | Jacket Accessory |
                  | SWEATER_ACCESSORY | Sweater Accessory |
                  | SHORTS_ACCESSORY | Shorts Accessory |
                  | LEFT_SHOE_ACCESSORY | Left Shoe Accessory |
                  | RIGHT_SHOE_ACCESSORY | Right Shoe Accessory |
                  | DRESS_SKIRT_ACCESSORY | Dress Skirt Accessory |
                  | FONT_FAMILY | Font Family |
                  | FONT_FACE | Font Face |
                  | MESH_HIDDEN_SURFACE_REMOVAL | Mesh Hidden Surface Removal |
                  | EYEBROW_ACCESSORY | Eyebrow Accessory |
                  | EYELASH_ACCESSORY | Eyelash Accessory |
                  | MOOD_ANIMATION | Mood Animation |
                  | DYNAMIC_HEAD | Dynamic Head |
                  | CODE_SNIPPET | Code Snippet |
                  | ADS_VIDEO | Ads Video | Example: ASSET_TYPE_UNSPECIFIED.
            usage (int | Unset): The current usage of the quota.
            capacity (int | Unset): The capacity of the quota.
            period (AssetQuotaPeriod | Unset): The period of time the quota is for.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | PERIOD_UNSPECIFIED | The default period, which is invalid. Specify another value. |
                  | MONTH | Month |
                  | DAY | Day | Example: PERIOD_UNSPECIFIED.
            usage_reset_time (datetime.datetime | Unset): The time the usage will reset for this quota. Example:
                2023-07-05T12:34:56Z.
    """

    path: str | Unset = UNSET
    quota_type: AssetQuotaQuotaType | Unset = UNSET
    asset_type: AssetQuotaAssetType | Unset = UNSET
    usage: int | Unset = UNSET
    capacity: int | Unset = UNSET
    period: AssetQuotaPeriod | Unset = UNSET
    usage_reset_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        usage_reset_time: str | Unset = UNSET
        if not isinstance(self.usage_reset_time, Unset):
            usage_reset_time = self.usage_reset_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        _quota_type = d.pop("quotaType", UNSET)
        quota_type: AssetQuotaQuotaType | Unset
        if isinstance(_quota_type, Unset):
            quota_type = UNSET
        else:
            quota_type = AssetQuotaQuotaType(_quota_type)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: AssetQuotaAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = AssetQuotaAssetType(_asset_type)

        usage = d.pop("usage", UNSET)

        capacity = d.pop("capacity", UNSET)

        _period = d.pop("period", UNSET)
        period: AssetQuotaPeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = AssetQuotaPeriod(_period)

        _usage_reset_time = d.pop("usageResetTime", UNSET)
        usage_reset_time: datetime.datetime | Unset
        if isinstance(_usage_reset_time, Unset):
            usage_reset_time = UNSET
        else:
            usage_reset_time = datetime.datetime.fromisoformat(_usage_reset_time)

        asset_quota = cls(
            path=path,
            quota_type=quota_type,
            asset_type=asset_type,
            usage=usage,
            capacity=capacity,
            period=period,
            usage_reset_time=usage_reset_time,
        )

        asset_quota.additional_properties = d
        return asset_quota

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
