from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_creative_asset_type import InternalPublicV1CreativeAssetType
from ..models.internal_public_v1_creative_moderation_status import InternalPublicV1CreativeModerationStatus
from ..models.internal_public_v1_creative_source import InternalPublicV1CreativeSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1Creative")


@_attrs_define
class InternalPublicV1Creative:
    """
    Attributes:
        asset_id (str | Unset): The Open Cloud image asset ID backing this creative, as a decimal string.
        asset_name (str | Unset): The display name of the underlying asset.
        asset_type (InternalPublicV1CreativeAssetType | Unset): The media type of the asset. Only `IMAGE` is supported
            in v1.
        create_time (str | Unset): The time the creative was added to the library, as an RFC 3339 UTC timestamp.
        height (int | Unset): The height of the asset in pixels. Omitted when unknown.
        id (str | Unset): The identifier of the creative library entry. This is distinct from assetId.
        is_archived (bool | Unset): Whether the creative has been archived (soft-deleted).
        moderation_status (InternalPublicV1CreativeModerationStatus | Unset): The content-review outcome for the asset.
            Can be `PENDING_REVIEW`, `APPROVED`, or `REJECTED`.
        source (InternalPublicV1CreativeSource | Unset): How the asset was produced. Can be `UPLOAD` or
            `IN_HOUSE_GEN_AI`.
        universe_id (str | Unset): The identifier of the experience the creative is associated with, if any, as a
            decimal string. Omitted when not associated with an experience.
        update_time (str | Unset): The time the creative was last updated, as an RFC 3339 UTC timestamp.
        width (int | Unset): The width of the asset in pixels. Omitted when unknown.
    """

    asset_id: str | Unset = UNSET
    asset_name: str | Unset = UNSET
    asset_type: InternalPublicV1CreativeAssetType | Unset = UNSET
    create_time: str | Unset = UNSET
    height: int | Unset = UNSET
    id: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    moderation_status: InternalPublicV1CreativeModerationStatus | Unset = UNSET
    source: InternalPublicV1CreativeSource | Unset = UNSET
    universe_id: str | Unset = UNSET
    update_time: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        create_time = self.create_time

        height = self.height

        id = self.id

        is_archived = self.is_archived

        moderation_status: str | Unset = UNSET
        if not isinstance(self.moderation_status, Unset):
            moderation_status = self.moderation_status.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        universe_id = self.universe_id

        update_time = self.update_time

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        asset_name = d.pop("assetName", UNSET)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: InternalPublicV1CreativeAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = InternalPublicV1CreativeAssetType(_asset_type)

        create_time = d.pop("createTime", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        _moderation_status = d.pop("moderationStatus", UNSET)
        moderation_status: InternalPublicV1CreativeModerationStatus | Unset
        if isinstance(_moderation_status, Unset):
            moderation_status = UNSET
        else:
            moderation_status = InternalPublicV1CreativeModerationStatus(_moderation_status)

        _source = d.pop("source", UNSET)
        source: InternalPublicV1CreativeSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = InternalPublicV1CreativeSource(_source)

        universe_id = d.pop("universeId", UNSET)

        update_time = d.pop("updateTime", UNSET)

        width = d.pop("width", UNSET)

        internal_public_v1_creative = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
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

        internal_public_v1_creative.additional_properties = d
        return internal_public_v1_creative

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
