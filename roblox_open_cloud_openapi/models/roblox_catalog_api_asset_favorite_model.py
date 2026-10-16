from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiAssetFavoriteModel")


@_attrs_define
class RobloxCatalogApiAssetFavoriteModel:
    """A model to represent asset favorites.

    Attributes:
        asset_id (int | Unset): The Id of the asset being favorited.
        user_id (int | Unset): The Id of the user favoriting the asset.
        created (datetime.datetime | Unset): The time at which the user favorited the asset.
    """

    asset_id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        user_id = self.user_id

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        user_id = d.pop("userId", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_catalog_api_asset_favorite_model = cls(
            asset_id=asset_id,
            user_id=user_id,
            created=created,
        )

        return roblox_catalog_api_asset_favorite_model
