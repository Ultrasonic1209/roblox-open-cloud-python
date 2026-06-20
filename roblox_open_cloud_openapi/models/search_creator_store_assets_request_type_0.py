from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_category_type import SearchCategoryType
from ..models.search_view import SearchView
from ..models.sort_category import SortCategory
from ..models.sort_direction import SortDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_search_filters_type_0 import AudioSearchFiltersType0
    from ..models.model_search_filters_type_0 import ModelSearchFiltersType0


T = TypeVar("T", bound="SearchCreatorStoreAssetsRequestType0")


@_attrs_define
class SearchCreatorStoreAssetsRequestType0:
    """Request model for searching Creator Store assets.

    Attributes:
        search_category_type (None | SearchCategoryType | Unset): The asset type to search within. Optional when
            Toolbox.Service.SearchCreatorStoreAssetsRequest.CategoryPath
            resolves to an asset type; otherwise required.
        query (None | str | Unset): The search terms used to filter the results. Only one of 'query' and 'image' can be
            present in a query.
        image (None | str | Unset): The image file to search by. The image must be base64 encoded to be used in the
            search. Only one of 'query' and 'image' can be present in a query.
        user_id (int | None | Unset): The User ID of the creator. Only one of 'userId' and 'groupId' can be present in a
            query.
        group_id (int | None | Unset): The Group ID of the creator. Only one of 'userId' and 'groupId' can be present in
            a query.
        page_token (None | str | Unset): The identifier for the desired search results page. Only one of 'pageNumber'
            and 'pageToken' can be present in a query.
        page_number (int | None | Unset): The page number to retrieve, starting from 0. Only one of 'pageNumber' and
            'pageToken' can be present in a query.
        max_page_size (int | Unset): The number of assets to be returned. Cannot be larger than 100.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the results
        sort_category (SortCategory | Unset): The category to sort the search results by.
        include_only_verified_creators (bool | Unset): Whether the results should only include assets created by
            verified creators.
        min_price_cents (int | None | Unset): The minimum price of the asset in cents. If included, must be greater than
            or equal to 0.
        max_price_cents (int | None | Unset): The maximum price of the asset in cents. If included, must be greater than
            or equal to 0.
        facets (list[str] | None | Unset): Additional keywords to query by.
        tags (list[str] | None | Unset): The tags to filter by.
        category_path (None | str | Unset): The category path to filter by.
        swimlane (None | str | Unset): Optional swimlane identifier (e.g. "trending", "essential", "priced").
            Resolves through Toolbox.Service.Interfaces.Swimlanes.ISwimlaneRegistry to a provider whose
            default sort intent and search-builder configuration are applied to the
            query. Unknown, disabled, or category-ineligible values yield 400.
        search_view (SearchView | Unset): This view controls which fields are populated in the search response. A
            lighter
            view will result in faster response times and higher reliability.
        audio_search_filters (AudioSearchFiltersType0 | None | Unset): Audio-specific search filters.
        model_search_filters (ModelSearchFiltersType0 | None | Unset): Model-specific search filters.
    """

    search_category_type: None | SearchCategoryType | Unset = UNSET
    query: None | str | Unset = UNSET
    image: None | str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    group_id: int | None | Unset = UNSET
    page_token: None | str | Unset = UNSET
    page_number: int | None | Unset = UNSET
    max_page_size: int | Unset = UNSET
    sort_direction: SortDirection | Unset = UNSET
    sort_category: SortCategory | Unset = UNSET
    include_only_verified_creators: bool | Unset = UNSET
    min_price_cents: int | None | Unset = UNSET
    max_price_cents: int | None | Unset = UNSET
    facets: list[str] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    category_path: None | str | Unset = UNSET
    swimlane: None | str | Unset = UNSET
    search_view: SearchView | Unset = UNSET
    audio_search_filters: AudioSearchFiltersType0 | None | Unset = UNSET
    model_search_filters: ModelSearchFiltersType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.audio_search_filters_type_0 import AudioSearchFiltersType0
        from ..models.model_search_filters_type_0 import ModelSearchFiltersType0

        search_category_type: None | str | Unset
        if isinstance(self.search_category_type, Unset):
            search_category_type = UNSET
        elif isinstance(self.search_category_type, SearchCategoryType):
            search_category_type = self.search_category_type.value
        else:
            search_category_type = self.search_category_type

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        group_id: int | None | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        page_token: None | str | Unset
        if isinstance(self.page_token, Unset):
            page_token = UNSET
        else:
            page_token = self.page_token

        page_number: int | None | Unset
        if isinstance(self.page_number, Unset):
            page_number = UNSET
        else:
            page_number = self.page_number

        max_page_size = self.max_page_size

        sort_direction: str | Unset = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = self.sort_direction.value

        sort_category: str | Unset = UNSET
        if not isinstance(self.sort_category, Unset):
            sort_category = self.sort_category.value

        include_only_verified_creators = self.include_only_verified_creators

        min_price_cents: int | None | Unset
        if isinstance(self.min_price_cents, Unset):
            min_price_cents = UNSET
        else:
            min_price_cents = self.min_price_cents

        max_price_cents: int | None | Unset
        if isinstance(self.max_price_cents, Unset):
            max_price_cents = UNSET
        else:
            max_price_cents = self.max_price_cents

        facets: list[str] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, list):
            facets = self.facets

        else:
            facets = self.facets

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        category_path: None | str | Unset
        if isinstance(self.category_path, Unset):
            category_path = UNSET
        else:
            category_path = self.category_path

        swimlane: None | str | Unset
        if isinstance(self.swimlane, Unset):
            swimlane = UNSET
        else:
            swimlane = self.swimlane

        search_view: str | Unset = UNSET
        if not isinstance(self.search_view, Unset):
            search_view = self.search_view.value

        audio_search_filters: dict[str, Any] | None | Unset
        if isinstance(self.audio_search_filters, Unset):
            audio_search_filters = UNSET
        elif isinstance(self.audio_search_filters, AudioSearchFiltersType0):
            audio_search_filters = self.audio_search_filters.to_dict()
        else:
            audio_search_filters = self.audio_search_filters

        model_search_filters: dict[str, Any] | None | Unset
        if isinstance(self.model_search_filters, Unset):
            model_search_filters = UNSET
        elif isinstance(self.model_search_filters, ModelSearchFiltersType0):
            model_search_filters = self.model_search_filters.to_dict()
        else:
            model_search_filters = self.model_search_filters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if search_category_type is not UNSET:
            field_dict["searchCategoryType"] = search_category_type
        if query is not UNSET:
            field_dict["query"] = query
        if image is not UNSET:
            field_dict["image"] = image
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if max_page_size is not UNSET:
            field_dict["maxPageSize"] = max_page_size
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction
        if sort_category is not UNSET:
            field_dict["sortCategory"] = sort_category
        if include_only_verified_creators is not UNSET:
            field_dict["includeOnlyVerifiedCreators"] = include_only_verified_creators
        if min_price_cents is not UNSET:
            field_dict["minPriceCents"] = min_price_cents
        if max_price_cents is not UNSET:
            field_dict["maxPriceCents"] = max_price_cents
        if facets is not UNSET:
            field_dict["facets"] = facets
        if tags is not UNSET:
            field_dict["tags"] = tags
        if category_path is not UNSET:
            field_dict["categoryPath"] = category_path
        if swimlane is not UNSET:
            field_dict["swimlane"] = swimlane
        if search_view is not UNSET:
            field_dict["searchView"] = search_view
        if audio_search_filters is not UNSET:
            field_dict["audioSearchFilters"] = audio_search_filters
        if model_search_filters is not UNSET:
            field_dict["modelSearchFilters"] = model_search_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_search_filters_type_0 import AudioSearchFiltersType0
        from ..models.model_search_filters_type_0 import ModelSearchFiltersType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_search_category_type(data: object) -> None | SearchCategoryType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                search_category_type_type_1 = SearchCategoryType(data)

                return search_category_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchCategoryType | Unset, data)

        search_category_type = _parse_search_category_type(d.pop("searchCategoryType", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        def _parse_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_token = _parse_page_token(d.pop("pageToken", UNSET))

        def _parse_page_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_number = _parse_page_number(d.pop("pageNumber", UNSET))

        max_page_size = d.pop("maxPageSize", UNSET)

        _sort_direction = d.pop("sortDirection", UNSET)
        sort_direction: SortDirection | Unset
        if isinstance(_sort_direction, Unset):
            sort_direction = UNSET
        else:
            sort_direction = SortDirection(_sort_direction)

        _sort_category = d.pop("sortCategory", UNSET)
        sort_category: SortCategory | Unset
        if isinstance(_sort_category, Unset):
            sort_category = UNSET
        else:
            sort_category = SortCategory(_sort_category)

        include_only_verified_creators = d.pop("includeOnlyVerifiedCreators", UNSET)

        def _parse_min_price_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_price_cents = _parse_min_price_cents(d.pop("minPriceCents", UNSET))

        def _parse_max_price_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_price_cents = _parse_max_price_cents(d.pop("maxPriceCents", UNSET))

        def _parse_facets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facets_type_0 = cast(list[str], data)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_category_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_path = _parse_category_path(d.pop("categoryPath", UNSET))

        def _parse_swimlane(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        swimlane = _parse_swimlane(d.pop("swimlane", UNSET))

        _search_view = d.pop("searchView", UNSET)
        search_view: SearchView | Unset
        if isinstance(_search_view, Unset):
            search_view = UNSET
        else:
            search_view = SearchView(_search_view)

        def _parse_audio_search_filters(data: object) -> AudioSearchFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audio_search_filters_type_0 = AudioSearchFiltersType0.from_dict(data)

                return componentsschemas_audio_search_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudioSearchFiltersType0 | None | Unset, data)

        audio_search_filters = _parse_audio_search_filters(d.pop("audioSearchFilters", UNSET))

        def _parse_model_search_filters(data: object) -> ModelSearchFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_model_search_filters_type_0 = ModelSearchFiltersType0.from_dict(data)

                return componentsschemas_model_search_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelSearchFiltersType0 | None | Unset, data)

        model_search_filters = _parse_model_search_filters(d.pop("modelSearchFilters", UNSET))

        search_creator_store_assets_request_type_0 = cls(
            search_category_type=search_category_type,
            query=query,
            image=image,
            user_id=user_id,
            group_id=group_id,
            page_token=page_token,
            page_number=page_number,
            max_page_size=max_page_size,
            sort_direction=sort_direction,
            sort_category=sort_category,
            include_only_verified_creators=include_only_verified_creators,
            min_price_cents=min_price_cents,
            max_price_cents=max_price_cents,
            facets=facets,
            tags=tags,
            category_path=category_path,
            swimlane=swimlane,
            search_view=search_view,
            audio_search_filters=audio_search_filters,
            model_search_filters=model_search_filters,
        )

        return search_creator_store_assets_request_type_0
