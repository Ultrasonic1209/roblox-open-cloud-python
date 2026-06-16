from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0
    from ..models.query_correction_type_0 import QueryCorrectionType0
    from ..models.query_facets_type_0 import QueryFacetsType0


T = TypeVar("T", bound="SearchCreatorStoreAssetsResponseType0")


@_attrs_define
class SearchCreatorStoreAssetsResponseType0:
    """The response for the SearchCreatorStoreAssets endpoint.

    Attributes:
        next_page_token (None | str | Unset): The page token to view the next page of results.
        query_facets (None | QueryFacetsType0 | Unset): The applied and available facets of a query.
        creator_store_assets (list[CreatorStoreAssetType0 | None] | None | Unset): The list of creator store assets
            returned by the search query.
        total_results (int | Unset): The total number of results for the given search query.
        query_correction (None | QueryCorrectionType0 | Unset): Query correction information, if a correction was
            available for the search query.
        filtered_keyword (None | str | Unset): The filtered keyword that was used to search for assets, if applicable.
    """

    next_page_token: None | str | Unset = UNSET
    query_facets: None | QueryFacetsType0 | Unset = UNSET
    creator_store_assets: list[CreatorStoreAssetType0 | None] | None | Unset = UNSET
    total_results: int | Unset = UNSET
    query_correction: None | QueryCorrectionType0 | Unset = UNSET
    filtered_keyword: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0
        from ..models.query_correction_type_0 import QueryCorrectionType0
        from ..models.query_facets_type_0 import QueryFacetsType0

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        query_facets: dict[str, Any] | None | Unset
        if isinstance(self.query_facets, Unset):
            query_facets = UNSET
        elif isinstance(self.query_facets, QueryFacetsType0):
            query_facets = self.query_facets.to_dict()
        else:
            query_facets = self.query_facets

        creator_store_assets: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.creator_store_assets, Unset):
            creator_store_assets = UNSET
        elif isinstance(self.creator_store_assets, list):
            creator_store_assets = []
            for creator_store_assets_type_0_item_data in self.creator_store_assets:
                creator_store_assets_type_0_item: dict[str, Any] | None
                if isinstance(creator_store_assets_type_0_item_data, CreatorStoreAssetType0):
                    creator_store_assets_type_0_item = creator_store_assets_type_0_item_data.to_dict()
                else:
                    creator_store_assets_type_0_item = creator_store_assets_type_0_item_data
                creator_store_assets.append(creator_store_assets_type_0_item)

        else:
            creator_store_assets = self.creator_store_assets

        total_results = self.total_results

        query_correction: dict[str, Any] | None | Unset
        if isinstance(self.query_correction, Unset):
            query_correction = UNSET
        elif isinstance(self.query_correction, QueryCorrectionType0):
            query_correction = self.query_correction.to_dict()
        else:
            query_correction = self.query_correction

        filtered_keyword: None | str | Unset
        if isinstance(self.filtered_keyword, Unset):
            filtered_keyword = UNSET
        else:
            filtered_keyword = self.filtered_keyword

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if query_facets is not UNSET:
            field_dict["queryFacets"] = query_facets
        if creator_store_assets is not UNSET:
            field_dict["creatorStoreAssets"] = creator_store_assets
        if total_results is not UNSET:
            field_dict["totalResults"] = total_results
        if query_correction is not UNSET:
            field_dict["queryCorrection"] = query_correction
        if filtered_keyword is not UNSET:
            field_dict["filteredKeyword"] = filtered_keyword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0
        from ..models.query_correction_type_0 import QueryCorrectionType0
        from ..models.query_facets_type_0 import QueryFacetsType0

        d = dict(src_dict)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_query_facets(data: object) -> None | QueryFacetsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_query_facets_type_0 = QueryFacetsType0.from_dict(data)

                return componentsschemas_query_facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QueryFacetsType0 | Unset, data)

        query_facets = _parse_query_facets(d.pop("queryFacets", UNSET))

        def _parse_creator_store_assets(data: object) -> list[CreatorStoreAssetType0 | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                creator_store_assets_type_0 = []
                _creator_store_assets_type_0 = data
                for creator_store_assets_type_0_item_data in _creator_store_assets_type_0:

                    def _parse_creator_store_assets_type_0_item(data: object) -> CreatorStoreAssetType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_creator_store_asset_type_0 = CreatorStoreAssetType0.from_dict(data)

                            return componentsschemas_creator_store_asset_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(CreatorStoreAssetType0 | None, data)

                    creator_store_assets_type_0_item = _parse_creator_store_assets_type_0_item(
                        creator_store_assets_type_0_item_data
                    )

                    creator_store_assets_type_0.append(creator_store_assets_type_0_item)

                return creator_store_assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreatorStoreAssetType0 | None] | None | Unset, data)

        creator_store_assets = _parse_creator_store_assets(d.pop("creatorStoreAssets", UNSET))

        total_results = d.pop("totalResults", UNSET)

        def _parse_query_correction(data: object) -> None | QueryCorrectionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_query_correction_type_0 = QueryCorrectionType0.from_dict(data)

                return componentsschemas_query_correction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QueryCorrectionType0 | Unset, data)

        query_correction = _parse_query_correction(d.pop("queryCorrection", UNSET))

        def _parse_filtered_keyword(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filtered_keyword = _parse_filtered_keyword(d.pop("filteredKeyword", UNSET))

        search_creator_store_assets_response_type_0 = cls(
            next_page_token=next_page_token,
            query_facets=query_facets,
            creator_store_assets=creator_store_assets,
            total_results=total_results,
            query_correction=query_correction,
            filtered_keyword=filtered_keyword,
        )

        return search_creator_store_assets_response_type_0
