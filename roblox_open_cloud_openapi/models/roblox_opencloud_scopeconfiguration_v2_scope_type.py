from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxOpencloudScopeconfigurationV2ScopeType")


@_attrs_define
class RobloxOpencloudScopeconfigurationV2ScopeType:
    """The configuration of a scope type. In v2 this carries only display + grouping data.

    Attributes:
        name (str | Unset):
        translation_key (str | Unset):
        product (str | Unset):
    """

    name: str | Unset = UNSET
    translation_key: str | Unset = UNSET
    product: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        translation_key = self.translation_key

        product = self.product

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        product = d.pop("product", UNSET)

        roblox_opencloud_scopeconfiguration_v2_scope_type = cls(
            name=name,
            translation_key=translation_key,
            product=product,
        )

        return roblox_opencloud_scopeconfiguration_v2_scope_type
