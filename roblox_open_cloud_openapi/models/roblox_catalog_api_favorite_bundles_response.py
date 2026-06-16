from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_bundle_details_model import RobloxCatalogApiBundleDetailsModel


T = TypeVar("T", bound="RobloxCatalogApiFavoriteBundlesResponse")


@_attrs_define
class RobloxCatalogApiFavoriteBundlesResponse:
    """A response containing favorited bundles and whether there are more.

    Attributes:
        favorites (list[RobloxCatalogApiBundleDetailsModel] | Unset): Collection of favorited bundles and associated
            details.
        more_favorites (bool | Unset): True if there exists a next page of favorited bundles.
        next_cursor (str | Unset): Pagination cursor for the next page.
        previous_cursor (str | Unset): Pagination cursor for the previous page.
    """

    favorites: list[RobloxCatalogApiBundleDetailsModel] | Unset = UNSET
    more_favorites: bool | Unset = UNSET
    next_cursor: str | Unset = UNSET
    previous_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        favorites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = []
            for favorites_item_data in self.favorites:
                favorites_item = favorites_item_data.to_dict()
                favorites.append(favorites_item)

        more_favorites = self.more_favorites

        next_cursor = self.next_cursor

        previous_cursor = self.previous_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if more_favorites is not UNSET:
            field_dict["moreFavorites"] = more_favorites
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if previous_cursor is not UNSET:
            field_dict["previousCursor"] = previous_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_bundle_details_model import RobloxCatalogApiBundleDetailsModel

        d = dict(src_dict)
        _favorites = d.pop("favorites", UNSET)
        favorites: list[RobloxCatalogApiBundleDetailsModel] | Unset = UNSET
        if _favorites is not UNSET:
            favorites = []
            for favorites_item_data in _favorites:
                favorites_item = RobloxCatalogApiBundleDetailsModel.from_dict(favorites_item_data)

                favorites.append(favorites_item)

        more_favorites = d.pop("moreFavorites", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        previous_cursor = d.pop("previousCursor", UNSET)

        roblox_catalog_api_favorite_bundles_response = cls(
            favorites=favorites,
            more_favorites=more_favorites,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
        )

        return roblox_catalog_api_favorite_bundles_response
