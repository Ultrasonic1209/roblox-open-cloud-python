from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxOpencloudScopeconfigurationV2Operation")


@_attrs_define
class RobloxOpencloudScopeconfigurationV2Operation:
    """The configuration of a global operation. The generic display label only; per-scope description/risk live on Scope.

    Attributes:
        name (str | Unset):
        translation_key (str | Unset):
    """

    name: str | Unset = UNSET
    translation_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        translation_key = self.translation_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        roblox_opencloud_scopeconfiguration_v2_operation = cls(
            name=name,
            translation_key=translation_key,
        )

        return roblox_opencloud_scopeconfiguration_v2_operation
