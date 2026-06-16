from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creation_context import CreationContext
    from ..models.moderation_result import ModerationResult


T = TypeVar("T", bound="AssetVersion")


@_attrs_define
class AssetVersion:
    """An asset version.

    Attributes:
        creation_context (CreationContext | Unset): The context of creation that is not part of the asset content, such
            as metadata and creator information. Required for [Create Asset](#POST-v1-assets).
        path (str | Unset): The returned resource path of the asset version. Format:
            `assets/{assetId}/versions/{version}`. Example: `assets/2205400862/versions/1`.
        moderation_result (ModerationResult | Unset): The moderation result of the asset.
        published (bool | Unset): Only applies to place asset types. Indicates if the place has been published or not.
    """

    creation_context: CreationContext | Unset = UNSET
    path: str | Unset = UNSET
    moderation_result: ModerationResult | Unset = UNSET
    published: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creation_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creation_context, Unset):
            creation_context = self.creation_context.to_dict()

        path = self.path

        moderation_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moderation_result, Unset):
            moderation_result = self.moderation_result.to_dict()

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_context is not UNSET:
            field_dict["creationContext"] = creation_context
        if path is not UNSET:
            field_dict["path"] = path
        if moderation_result is not UNSET:
            field_dict["moderationResult"] = moderation_result
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creation_context import CreationContext
        from ..models.moderation_result import ModerationResult

        d = dict(src_dict)
        _creation_context = d.pop("creationContext", UNSET)
        creation_context: CreationContext | Unset
        if isinstance(_creation_context, Unset):
            creation_context = UNSET
        else:
            creation_context = CreationContext.from_dict(_creation_context)

        path = d.pop("path", UNSET)

        _moderation_result = d.pop("moderationResult", UNSET)
        moderation_result: ModerationResult | Unset
        if isinstance(_moderation_result, Unset):
            moderation_result = UNSET
        else:
            moderation_result = ModerationResult.from_dict(_moderation_result)

        published = d.pop("published", UNSET)

        asset_version = cls(
            creation_context=creation_context,
            path=path,
            moderation_result=moderation_result,
            published=published,
        )

        asset_version.additional_properties = d
        return asset_version

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
