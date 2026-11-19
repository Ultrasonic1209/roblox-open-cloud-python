from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creative_asset_type import CreativeAssetType
from ..models.creative_moderation_status import CreativeModerationStatus
from ..models.creative_source import CreativeSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="Creative")


@_attrs_define
class Creative:
    """
    Attributes:
        asset_id (str | Unset): The Roblox asset ID identifying this creative, as a decimal string. Use this assetId in
            GET and PATCH /creatives/{id}, not the registration UUID in id.
            groupId selects the group ads account; absent groupId selects the personal ads account.
        asset_name (str | Unset): The display name of the underlying asset.
        asset_type (CreativeAssetType | Unset): The media type of the asset. Only `IMAGE` is supported.
        billing_account_id (str | Unset): The billing account whose library holds this entry.
        create_time (datetime.datetime | Unset): The time the creative was added to the library, as an RFC 3339 UTC
            timestamp.
        height (int | Unset): The height of the asset in pixels. Omitted when unknown.
        id (UUID | Unset): The UUID identifying this creative registration. GET and PATCH paths use assetId, not this
            UUID.
        is_archived (bool | Unset): Whether the creative has been archived (soft-deleted).
        moderation_status (CreativeModerationStatus | Unset): The content-review outcome for the asset. Can be
            `PENDING_REVIEW`, `APPROVED`, or `REJECTED`.
        source (CreativeSource | Unset): How the asset was produced. Can be `UPLOAD` or `IN_HOUSE_GEN_AI`.
        universe_id (str | Unset): The identifier of the experience the creative is associated with, if any, as a
            decimal string. Omitted when not associated with an experience.
        update_time (datetime.datetime | Unset): The time the creative was last updated, as an RFC 3339 UTC timestamp.
        width (int | Unset): The width of the asset in pixels. Omitted when unknown.
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: CreativeAssetType | Unset = UNSET
    billing_account_id: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    height: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    moderation_status: CreativeModerationStatus | Unset = UNSET
    source: CreativeSource | Unset = UNSET
    universe_id: str | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        billing_account_id = self.billing_account_id

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        moderation_status: str | Unset = UNSET
        if not isinstance(self.moderation_status, Unset):
            moderation_status = self.moderation_status.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        universe_id = self.universe_id

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if asset_name is not UNSET:
            field_dict["assetName"] = asset_name
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if billing_account_id is not UNSET:
            field_dict["billingAccountId"] = billing_account_id
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status
        if source is not UNSET:
            field_dict["source"] = source
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId", UNSET)

        asset_name = d.pop("assetName", UNSET)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: CreativeAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = CreativeAssetType(_asset_type)

        billing_account_id = d.pop("billingAccountId", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        height = d.pop("height", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_archived = d.pop("isArchived", UNSET)

        _moderation_status = d.pop("moderationStatus", UNSET)
        moderation_status: CreativeModerationStatus | Unset
        if isinstance(_moderation_status, Unset):
            moderation_status = UNSET
        else:
            moderation_status = CreativeModerationStatus(_moderation_status)

        _source = d.pop("source", UNSET)
        source: CreativeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CreativeSource(_source)

        universe_id = d.pop("universeId", UNSET)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        width = d.pop("width", UNSET)

        creative = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            billing_account_id=billing_account_id,
            create_time=create_time,
            height=height,
            id=id,
            is_archived=is_archived,
            moderation_status=moderation_status,
            source=source,
            universe_id=universe_id,
            update_time=update_time,
            width=width,
        )

        creative.additional_properties = d
        return creative

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
