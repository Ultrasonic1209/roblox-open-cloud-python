from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_opencloud_scopeconfiguration_v2_target_part_types_value_type import (
    RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxOpencloudScopeconfigurationV2TargetPart")


@_attrs_define
class RobloxOpencloudScopeconfigurationV2TargetPart:
    """The configuration of a target part. Referenced by TargetTypes.

    Attributes:
        name (str | Unset):
        type_ (RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType | Unset): Data type of a target part value.
        constraints (list[str] | Unset):
        translation_key (str | Unset):
    """

    name: str | Unset = UNSET
    type_: RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType | Unset = UNSET
    constraints: list[str] | Unset = UNSET
    translation_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        constraints: list[str] | Unset = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = self.constraints

        translation_key = self.translation_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType(_type_)

        constraints = cast(list[str], d.pop("constraints", UNSET))

        translation_key = d.pop("translationKey", UNSET)

        roblox_opencloud_scopeconfiguration_v2_target_part = cls(
            name=name,
            type_=type_,
            constraints=constraints,
            translation_key=translation_key,
        )

        return roblox_opencloud_scopeconfiguration_v2_target_part
