from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creation_context import CreationContext
    from ..models.moderation_result import ModerationResult


T = TypeVar("T", bound="AssetVersion")


@_attrs_define
class AssetVersion:
    """An asset version.

    Attributes:
        path (None | str | Unset): The returned resource path of the asset version. Format:
            `assets/{assetId}/versions/{version}`. Example: assets/123/versions/123.
        create_time (datetime.datetime | None | Unset): The timestamp when the asset version was created.
        creation_context (CreationContext | Unset): The context of creation that is not part of the asset content, such
            as metadata and creator information. Required for [Create Asset](#Assets_CreateAsset).
        moderation_result (ModerationResult | Unset): The moderation result of the asset.
        published (bool | Unset): Indicates whether the asset version is published. If omitted, the version is not
            published.
    """

    path: None | str | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    creation_context: CreationContext | Unset = UNSET
    moderation_result: ModerationResult | Unset = UNSET
    published: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        creation_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creation_context, Unset):
            creation_context = self.creation_context.to_dict()

        moderation_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moderation_result, Unset):
            moderation_result = self.moderation_result.to_dict()

        published = self.published

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if creation_context is not UNSET:
            field_dict["creationContext"] = creation_context
        if moderation_result is not UNSET:
            field_dict["moderationResult"] = moderation_result
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creation_context import CreationContext  # noqa: PLC0415
        from ..models.moderation_result import ModerationResult  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = datetime.datetime.fromisoformat(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("createTime", UNSET))

        _creation_context = d.pop("creationContext", UNSET)
        creation_context: CreationContext | Unset
        if isinstance(_creation_context, Unset):
            creation_context = UNSET
        else:
            creation_context = CreationContext.from_dict(_creation_context)

        _moderation_result = d.pop("moderationResult", UNSET)
        moderation_result: ModerationResult | Unset
        if isinstance(_moderation_result, Unset):
            moderation_result = UNSET
        else:
            moderation_result = ModerationResult.from_dict(_moderation_result)

        published = d.pop("published", UNSET)

        asset_version = cls(
            path=path,
            create_time=create_time,
            creation_context=creation_context,
            moderation_result=moderation_result,
            published=published,
        )

        return asset_version
