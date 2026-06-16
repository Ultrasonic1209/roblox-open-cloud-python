from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiBundleFavoriteModel")


@_attrs_define
class RobloxCatalogApiBundleFavoriteModel:
    """A model to represent bundle favorites.

    Attributes:
        bundle_id (int | Unset): The Id of the bundle being favorited.
        user_id (int | Unset): The Id of the user favoriting the bundle.
        created (datetime.datetime | Unset): The time at which the user favorited the bundle.
    """

    bundle_id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        user_id = self.user_id

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_id = d.pop("bundleId", UNSET)

        user_id = d.pop("userId", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_catalog_api_bundle_favorite_model = cls(
            bundle_id=bundle_id,
            user_id=user_id,
            created=created,
        )

        return roblox_catalog_api_bundle_favorite_model
