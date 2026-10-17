from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiBundleCreatorModel")


@_attrs_define
class RobloxCatalogApiBundleCreatorModel:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        type_ (str | Unset):
        has_verified_badge (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_catalog_api_bundle_creator_model = cls(
            id=id,
            name=name,
            type_=type_,
            has_verified_badge=has_verified_badge,
        )

        return roblox_catalog_api_bundle_creator_model
