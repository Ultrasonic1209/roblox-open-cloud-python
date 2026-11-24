from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxOpencloudScopeconfigurationV2TargetType")


@_attrs_define
class RobloxOpencloudScopeconfigurationV2TargetType:
    """The configuration of a target type. Referenced by Scopes' target_type.

    Attributes:
        name (str | Unset):
        required_parts (list[str] | Unset):
        optional_parts (list[str] | Unset):
        translation_key (str | Unset):
    """

    name: str | Unset = UNSET
    required_parts: list[str] | Unset = UNSET
    optional_parts: list[str] | Unset = UNSET
    translation_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        required_parts: list[str] | Unset = UNSET
        if not isinstance(self.required_parts, Unset):
            required_parts = self.required_parts

        optional_parts: list[str] | Unset = UNSET
        if not isinstance(self.optional_parts, Unset):
            optional_parts = self.optional_parts

        translation_key = self.translation_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if required_parts is not UNSET:
            field_dict["requiredParts"] = required_parts
        if optional_parts is not UNSET:
            field_dict["optionalParts"] = optional_parts
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        required_parts = cast(list[str], d.pop("requiredParts", UNSET))

        optional_parts = cast(list[str], d.pop("optionalParts", UNSET))

        translation_key = d.pop("translationKey", UNSET)

        roblox_opencloud_scopeconfiguration_v2_target_type = cls(
            name=name,
            required_parts=required_parts,
            optional_parts=optional_parts,
            translation_key=translation_key,
        )

        return roblox_opencloud_scopeconfiguration_v2_target_type
