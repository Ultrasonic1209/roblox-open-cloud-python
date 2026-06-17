import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.model_instance_type import ModelInstanceType
from ...models.model_sub_type import ModelSubType
from ...models.music_chart_type import MusicChartType
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...models.search_audio_type_model import SearchAudioTypeModel
from ...models.search_category_type import SearchCategoryType
from ...models.search_creator_store_assets_response_type_0 import SearchCreatorStoreAssetsResponseType0
from ...models.search_view import SearchView
from ...models.sort_category import SortCategory
from ...models.sort_direction import SortDirection


def _get_kwargs(
    *,
    search_category_type: SearchCategoryType,
    query: str | Unset = UNSET,
    model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    excluded_model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    creator: str | Unset = UNSET,
    user_id: int | None | Unset = UNSET,
    group_id: int | None | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_number: int | None | Unset = UNSET,
    max_page_size: int | Unset = 25,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    sort_category: SortCategory | Unset = SortCategory.RELEVANCE,
    audio_min_duration_seconds: int | Unset = 0,
    audio_max_duration_seconds: int | None | Unset = UNSET,
    audio_artist: str | Unset = UNSET,
    audio_album: str | Unset = UNSET,
    include_top_charts: bool | None | Unset = False,
    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET,
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET,
    include_only_verified_creators: bool | Unset = True,
    min_price_cents: int | None | Unset = UNSET,
    max_price_cents: int | None | Unset = UNSET,
    facets: list[str] | None | Unset = UNSET,
    category_path: str | Unset = UNSET,
    search_view: SearchView | Unset = SearchView.CORE,
    music_chart_type: MusicChartType | Unset = MusicChartType.NONE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search_category_type = search_category_type.value
    params["searchCategoryType"] = json_search_category_type

    params["query"] = query

    json_model_sub_types: list[str] | None | Unset
    if isinstance(model_sub_types, Unset):
        json_model_sub_types = UNSET
    elif isinstance(model_sub_types, list):
        json_model_sub_types = []
        for model_sub_types_type_0_item_data in model_sub_types:
            model_sub_types_type_0_item = model_sub_types_type_0_item_data.value
            json_model_sub_types.append(model_sub_types_type_0_item)

    else:
        json_model_sub_types = model_sub_types
    params["modelSubTypes"] = json_model_sub_types

    json_excluded_model_sub_types: list[str] | None | Unset
    if isinstance(excluded_model_sub_types, Unset):
        json_excluded_model_sub_types = UNSET
    elif isinstance(excluded_model_sub_types, list):
        json_excluded_model_sub_types = []
        for excluded_model_sub_types_type_0_item_data in excluded_model_sub_types:
            excluded_model_sub_types_type_0_item = excluded_model_sub_types_type_0_item_data.value
            json_excluded_model_sub_types.append(excluded_model_sub_types_type_0_item)

    else:
        json_excluded_model_sub_types = excluded_model_sub_types
    params["excludedModelSubTypes"] = json_excluded_model_sub_types

    params["creator"] = creator

    json_user_id: int | None | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["userId"] = json_user_id

    json_group_id: int | None | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    else:
        json_group_id = group_id
    params["groupId"] = json_group_id

    params["pageToken"] = page_token

    json_page_number: int | None | Unset
    if isinstance(page_number, Unset):
        json_page_number = UNSET
    else:
        json_page_number = page_number
    params["pageNumber"] = json_page_number

    params["maxPageSize"] = max_page_size

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_sort_category: str | Unset = UNSET
    if not isinstance(sort_category, Unset):
        json_sort_category = sort_category.value

    params["sortCategory"] = json_sort_category

    params["audioMinDurationSeconds"] = audio_min_duration_seconds

    json_audio_max_duration_seconds: int | None | Unset
    if isinstance(audio_max_duration_seconds, Unset):
        json_audio_max_duration_seconds = UNSET
    else:
        json_audio_max_duration_seconds = audio_max_duration_seconds
    params["audioMaxDurationSeconds"] = json_audio_max_duration_seconds

    params["audioArtist"] = audio_artist

    params["audioAlbum"] = audio_album

    json_include_top_charts: bool | None | Unset
    if isinstance(include_top_charts, Unset):
        json_include_top_charts = UNSET
    else:
        json_include_top_charts = include_top_charts
    params["includeTopCharts"] = json_include_top_charts

    json_audio_types: list[str] | None | Unset
    if isinstance(audio_types, Unset):
        json_audio_types = UNSET
    elif isinstance(audio_types, list):
        json_audio_types = []
        for audio_types_type_0_item_data in audio_types:
            audio_types_type_0_item = audio_types_type_0_item_data.value
            json_audio_types.append(audio_types_type_0_item)

    else:
        json_audio_types = audio_types
    params["audioTypes"] = json_audio_types

    json_included_instance_types: list[str] | None | Unset
    if isinstance(included_instance_types, Unset):
        json_included_instance_types = UNSET
    elif isinstance(included_instance_types, list):
        json_included_instance_types = []
        for included_instance_types_type_0_item_data in included_instance_types:
            included_instance_types_type_0_item = included_instance_types_type_0_item_data.value
            json_included_instance_types.append(included_instance_types_type_0_item)

    else:
        json_included_instance_types = included_instance_types
    params["includedInstanceTypes"] = json_included_instance_types

    params["includeOnlyVerifiedCreators"] = include_only_verified_creators

    json_min_price_cents: int | None | Unset
    if isinstance(min_price_cents, Unset):
        json_min_price_cents = UNSET
    else:
        json_min_price_cents = min_price_cents
    params["minPriceCents"] = json_min_price_cents

    json_max_price_cents: int | None | Unset
    if isinstance(max_price_cents, Unset):
        json_max_price_cents = UNSET
    else:
        json_max_price_cents = max_price_cents
    params["maxPriceCents"] = json_max_price_cents

    json_facets: list[str] | None | Unset
    if isinstance(facets, Unset):
        json_facets = UNSET
    elif isinstance(facets, list):
        json_facets = facets

    else:
        json_facets = facets
    params["facets"] = json_facets

    params["categoryPath"] = category_path

    json_search_view: str | Unset = UNSET
    if not isinstance(search_view, Unset):
        json_search_view = search_view.value

    params["searchView"] = json_search_view

    json_music_chart_type: str | Unset = UNSET
    if not isinstance(music_chart_type, Unset):
        json_music_chart_type = music_chart_type.value

    params["musicChartType"] = json_music_chart_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/toolbox-service/v2/assets:search",
        "params": params,
        "openapi-extensions": {
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/toolbox/v2/assets:search",
                    "httpMethod": "POST",
                    "description": "This endpoint is being deprecated in favor of using POST which has the same functionality but with better structured data & support for image-based search.",
                }
            ],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 1000},
            },
            "x-roblox-scopes": [{"name": "creator-store-product:read"}],
        },
        "openapi-id": "Toolbox_SearchCreatorStoreAssetsDeprecated",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | SearchCreatorStoreAssetsResponseType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_search_creator_store_assets_response_type_0 = (
                    SearchCreatorStoreAssetsResponseType0.from_dict(data)
                )

                return componentsschemas_search_creator_store_assets_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchCreatorStoreAssetsResponseType0, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 429:

        def _parse_response_429(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_429 = _parse_response_429(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#Toolbox_SearchCreatorStoreAssetsDeprecated"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    search_category_type: SearchCategoryType,
    query: str | Unset = UNSET,
    model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    excluded_model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    creator: str | Unset = UNSET,
    user_id: int | None | Unset = UNSET,
    group_id: int | None | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_number: int | None | Unset = UNSET,
    max_page_size: int | Unset = 25,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    sort_category: SortCategory | Unset = SortCategory.RELEVANCE,
    audio_min_duration_seconds: int | Unset = 0,
    audio_max_duration_seconds: int | None | Unset = UNSET,
    audio_artist: str | Unset = UNSET,
    audio_album: str | Unset = UNSET,
    include_top_charts: bool | None | Unset = False,
    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET,
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET,
    include_only_verified_creators: bool | Unset = True,
    min_price_cents: int | None | Unset = UNSET,
    max_price_cents: int | None | Unset = UNSET,
    facets: list[str] | None | Unset = UNSET,
    category_path: str | Unset = UNSET,
    search_view: SearchView | Unset = SearchView.CORE,
    music_chart_type: MusicChartType | Unset = MusicChartType.NONE,
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        search_category_type (SearchCategoryType): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        query (str | Unset):
        model_sub_types (list[ModelSubType] | None | Unset):
        excluded_model_sub_types (list[ModelSubType] | None | Unset):
        creator (str | Unset):
        user_id (int | None | Unset):
        group_id (int | None | Unset):
        page_token (str | Unset):
        page_number (int | None | Unset):
        max_page_size (int | Unset):  Default: 25.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        sort_category (SortCategory | Unset): The category to sort the search results by. Default:
            SortCategory.RELEVANCE.
        audio_min_duration_seconds (int | Unset):  Default: 0.
        audio_max_duration_seconds (int | None | Unset):
        audio_artist (str | Unset):
        audio_album (str | Unset):
        include_top_charts (bool | None | Unset):  Default: False.
        audio_types (list[SearchAudioTypeModel] | None | Unset):
        included_instance_types (list[ModelInstanceType] | None | Unset):
        include_only_verified_creators (bool | Unset):  Default: True.
        min_price_cents (int | None | Unset):
        max_price_cents (int | None | Unset):
        facets (list[str] | None | Unset):
        category_path (str | Unset):
        search_view (SearchView | Unset): This view controls which fields are populated in the
            search response. A lighter
            view will result in faster response times and higher reliability. Default:
            SearchView.CORE.
        music_chart_type (MusicChartType | Unset): Represents which music chart to pull entries
            from, if any Default: MusicChartType.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]
    """

    kwargs = _get_kwargs(
        search_category_type=search_category_type,
        query=query,
        model_sub_types=model_sub_types,
        excluded_model_sub_types=excluded_model_sub_types,
        creator=creator,
        user_id=user_id,
        group_id=group_id,
        page_token=page_token,
        page_number=page_number,
        max_page_size=max_page_size,
        sort_direction=sort_direction,
        sort_category=sort_category,
        audio_min_duration_seconds=audio_min_duration_seconds,
        audio_max_duration_seconds=audio_max_duration_seconds,
        audio_artist=audio_artist,
        audio_album=audio_album,
        include_top_charts=include_top_charts,
        audio_types=audio_types,
        included_instance_types=included_instance_types,
        include_only_verified_creators=include_only_verified_creators,
        min_price_cents=min_price_cents,
        max_price_cents=max_price_cents,
        facets=facets,
        category_path=category_path,
        search_view=search_view,
        music_chart_type=music_chart_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#Toolbox_SearchCreatorStoreAssetsDeprecated"
)
def sync(
    *,
    client: AuthenticatedClient,
    search_category_type: SearchCategoryType,
    query: str | Unset = UNSET,
    model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    excluded_model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    creator: str | Unset = UNSET,
    user_id: int | None | Unset = UNSET,
    group_id: int | None | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_number: int | None | Unset = UNSET,
    max_page_size: int | Unset = 25,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    sort_category: SortCategory | Unset = SortCategory.RELEVANCE,
    audio_min_duration_seconds: int | Unset = 0,
    audio_max_duration_seconds: int | None | Unset = UNSET,
    audio_artist: str | Unset = UNSET,
    audio_album: str | Unset = UNSET,
    include_top_charts: bool | None | Unset = False,
    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET,
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET,
    include_only_verified_creators: bool | Unset = True,
    min_price_cents: int | None | Unset = UNSET,
    max_price_cents: int | None | Unset = UNSET,
    facets: list[str] | None | Unset = UNSET,
    category_path: str | Unset = UNSET,
    search_view: SearchView | Unset = SearchView.CORE,
    music_chart_type: MusicChartType | Unset = MusicChartType.NONE,
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        search_category_type (SearchCategoryType): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        query (str | Unset):
        model_sub_types (list[ModelSubType] | None | Unset):
        excluded_model_sub_types (list[ModelSubType] | None | Unset):
        creator (str | Unset):
        user_id (int | None | Unset):
        group_id (int | None | Unset):
        page_token (str | Unset):
        page_number (int | None | Unset):
        max_page_size (int | Unset):  Default: 25.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        sort_category (SortCategory | Unset): The category to sort the search results by. Default:
            SortCategory.RELEVANCE.
        audio_min_duration_seconds (int | Unset):  Default: 0.
        audio_max_duration_seconds (int | None | Unset):
        audio_artist (str | Unset):
        audio_album (str | Unset):
        include_top_charts (bool | None | Unset):  Default: False.
        audio_types (list[SearchAudioTypeModel] | None | Unset):
        included_instance_types (list[ModelInstanceType] | None | Unset):
        include_only_verified_creators (bool | Unset):  Default: True.
        min_price_cents (int | None | Unset):
        max_price_cents (int | None | Unset):
        facets (list[str] | None | Unset):
        category_path (str | Unset):
        search_view (SearchView | Unset): This view controls which fields are populated in the
            search response. A lighter
            view will result in faster response times and higher reliability. Default:
            SearchView.CORE.
        music_chart_type (MusicChartType | Unset): Represents which music chart to pull entries
            from, if any Default: MusicChartType.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0
    """

    return sync_detailed(
        client=client,
        search_category_type=search_category_type,
        query=query,
        model_sub_types=model_sub_types,
        excluded_model_sub_types=excluded_model_sub_types,
        creator=creator,
        user_id=user_id,
        group_id=group_id,
        page_token=page_token,
        page_number=page_number,
        max_page_size=max_page_size,
        sort_direction=sort_direction,
        sort_category=sort_category,
        audio_min_duration_seconds=audio_min_duration_seconds,
        audio_max_duration_seconds=audio_max_duration_seconds,
        audio_artist=audio_artist,
        audio_album=audio_album,
        include_top_charts=include_top_charts,
        audio_types=audio_types,
        included_instance_types=included_instance_types,
        include_only_verified_creators=include_only_verified_creators,
        min_price_cents=min_price_cents,
        max_price_cents=max_price_cents,
        facets=facets,
        category_path=category_path,
        search_view=search_view,
        music_chart_type=music_chart_type,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#Toolbox_SearchCreatorStoreAssetsDeprecated"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_category_type: SearchCategoryType,
    query: str | Unset = UNSET,
    model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    excluded_model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    creator: str | Unset = UNSET,
    user_id: int | None | Unset = UNSET,
    group_id: int | None | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_number: int | None | Unset = UNSET,
    max_page_size: int | Unset = 25,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    sort_category: SortCategory | Unset = SortCategory.RELEVANCE,
    audio_min_duration_seconds: int | Unset = 0,
    audio_max_duration_seconds: int | None | Unset = UNSET,
    audio_artist: str | Unset = UNSET,
    audio_album: str | Unset = UNSET,
    include_top_charts: bool | None | Unset = False,
    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET,
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET,
    include_only_verified_creators: bool | Unset = True,
    min_price_cents: int | None | Unset = UNSET,
    max_price_cents: int | None | Unset = UNSET,
    facets: list[str] | None | Unset = UNSET,
    category_path: str | Unset = UNSET,
    search_view: SearchView | Unset = SearchView.CORE,
    music_chart_type: MusicChartType | Unset = MusicChartType.NONE,
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        search_category_type (SearchCategoryType): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        query (str | Unset):
        model_sub_types (list[ModelSubType] | None | Unset):
        excluded_model_sub_types (list[ModelSubType] | None | Unset):
        creator (str | Unset):
        user_id (int | None | Unset):
        group_id (int | None | Unset):
        page_token (str | Unset):
        page_number (int | None | Unset):
        max_page_size (int | Unset):  Default: 25.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        sort_category (SortCategory | Unset): The category to sort the search results by. Default:
            SortCategory.RELEVANCE.
        audio_min_duration_seconds (int | Unset):  Default: 0.
        audio_max_duration_seconds (int | None | Unset):
        audio_artist (str | Unset):
        audio_album (str | Unset):
        include_top_charts (bool | None | Unset):  Default: False.
        audio_types (list[SearchAudioTypeModel] | None | Unset):
        included_instance_types (list[ModelInstanceType] | None | Unset):
        include_only_verified_creators (bool | Unset):  Default: True.
        min_price_cents (int | None | Unset):
        max_price_cents (int | None | Unset):
        facets (list[str] | None | Unset):
        category_path (str | Unset):
        search_view (SearchView | Unset): This view controls which fields are populated in the
            search response. A lighter
            view will result in faster response times and higher reliability. Default:
            SearchView.CORE.
        music_chart_type (MusicChartType | Unset): Represents which music chart to pull entries
            from, if any Default: MusicChartType.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]
    """

    kwargs = _get_kwargs(
        search_category_type=search_category_type,
        query=query,
        model_sub_types=model_sub_types,
        excluded_model_sub_types=excluded_model_sub_types,
        creator=creator,
        user_id=user_id,
        group_id=group_id,
        page_token=page_token,
        page_number=page_number,
        max_page_size=max_page_size,
        sort_direction=sort_direction,
        sort_category=sort_category,
        audio_min_duration_seconds=audio_min_duration_seconds,
        audio_max_duration_seconds=audio_max_duration_seconds,
        audio_artist=audio_artist,
        audio_album=audio_album,
        include_top_charts=include_top_charts,
        audio_types=audio_types,
        included_instance_types=included_instance_types,
        include_only_verified_creators=include_only_verified_creators,
        min_price_cents=min_price_cents,
        max_price_cents=max_price_cents,
        facets=facets,
        category_path=category_path,
        search_view=search_view,
        music_chart_type=music_chart_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#Toolbox_SearchCreatorStoreAssetsDeprecated"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    search_category_type: SearchCategoryType,
    query: str | Unset = UNSET,
    model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    excluded_model_sub_types: list[ModelSubType] | None | Unset = UNSET,
    creator: str | Unset = UNSET,
    user_id: int | None | Unset = UNSET,
    group_id: int | None | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_number: int | None | Unset = UNSET,
    max_page_size: int | Unset = 25,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    sort_category: SortCategory | Unset = SortCategory.RELEVANCE,
    audio_min_duration_seconds: int | Unset = 0,
    audio_max_duration_seconds: int | None | Unset = UNSET,
    audio_artist: str | Unset = UNSET,
    audio_album: str | Unset = UNSET,
    include_top_charts: bool | None | Unset = False,
    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET,
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET,
    include_only_verified_creators: bool | Unset = True,
    min_price_cents: int | None | Unset = UNSET,
    max_price_cents: int | None | Unset = UNSET,
    facets: list[str] | None | Unset = UNSET,
    category_path: str | Unset = UNSET,
    search_view: SearchView | Unset = SearchView.CORE,
    music_chart_type: MusicChartType | Unset = MusicChartType.NONE,
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        search_category_type (SearchCategoryType): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        query (str | Unset):
        model_sub_types (list[ModelSubType] | None | Unset):
        excluded_model_sub_types (list[ModelSubType] | None | Unset):
        creator (str | Unset):
        user_id (int | None | Unset):
        group_id (int | None | Unset):
        page_token (str | Unset):
        page_number (int | None | Unset):
        max_page_size (int | Unset):  Default: 25.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        sort_category (SortCategory | Unset): The category to sort the search results by. Default:
            SortCategory.RELEVANCE.
        audio_min_duration_seconds (int | Unset):  Default: 0.
        audio_max_duration_seconds (int | None | Unset):
        audio_artist (str | Unset):
        audio_album (str | Unset):
        include_top_charts (bool | None | Unset):  Default: False.
        audio_types (list[SearchAudioTypeModel] | None | Unset):
        included_instance_types (list[ModelInstanceType] | None | Unset):
        include_only_verified_creators (bool | Unset):  Default: True.
        min_price_cents (int | None | Unset):
        max_price_cents (int | None | Unset):
        facets (list[str] | None | Unset):
        category_path (str | Unset):
        search_view (SearchView | Unset): This view controls which fields are populated in the
            search response. A lighter
            view will result in faster response times and higher reliability. Default:
            SearchView.CORE.
        music_chart_type (MusicChartType | Unset): Represents which music chart to pull entries
            from, if any Default: MusicChartType.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0
    """

    return (
        await asyncio_detailed(
            client=client,
            search_category_type=search_category_type,
            query=query,
            model_sub_types=model_sub_types,
            excluded_model_sub_types=excluded_model_sub_types,
            creator=creator,
            user_id=user_id,
            group_id=group_id,
            page_token=page_token,
            page_number=page_number,
            max_page_size=max_page_size,
            sort_direction=sort_direction,
            sort_category=sort_category,
            audio_min_duration_seconds=audio_min_duration_seconds,
            audio_max_duration_seconds=audio_max_duration_seconds,
            audio_artist=audio_artist,
            audio_album=audio_album,
            include_top_charts=include_top_charts,
            audio_types=audio_types,
            included_instance_types=included_instance_types,
            include_only_verified_creators=include_only_verified_creators,
            min_price_cents=min_price_cents,
            max_price_cents=max_price_cents,
            facets=facets,
            category_path=category_path,
            search_view=search_view,
            music_chart_type=music_chart_type,
        )
    ).parsed
