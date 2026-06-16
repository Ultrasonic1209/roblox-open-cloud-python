from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_search_items_details_category_filter import GetV2SearchItemsDetailsCategoryFilter
from ...models.get_v2_search_items_details_creator_type import GetV2SearchItemsDetailsCreatorType
from ...models.get_v2_search_items_details_limit import GetV2SearchItemsDetailsLimit
from ...models.get_v2_search_items_details_sales_type_filter import GetV2SearchItemsDetailsSalesTypeFilter
from ...models.get_v2_search_items_details_sort_aggregation import GetV2SearchItemsDetailsSortAggregation
from ...models.get_v2_search_items_details_sort_order import GetV2SearchItemsDetailsSortOrder
from ...models.get_v2_search_items_details_sort_type import GetV2SearchItemsDetailsSortType
from ...models.roblox_catalog_api_catalog_search_page_response_roblox_catalog_api_catalog_search_detailed_response_item_v2 import (
    RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    taxonomy: str | Unset = UNSET,
    asset_type_ids: list[int] | Unset = UNSET,
    bundle_type_ids: list[int] | Unset = UNSET,
    category_filter: GetV2SearchItemsDetailsCategoryFilter | Unset = UNSET,
    sort_aggregation: GetV2SearchItemsDetailsSortAggregation | Unset = UNSET,
    sort_type: GetV2SearchItemsDetailsSortType | Unset = UNSET,
    creator_type: GetV2SearchItemsDetailsCreatorType | Unset = UNSET,
    creator_target_id: int | Unset = UNSET,
    creator_name: str | Unset = UNSET,
    max_price: int | Unset = UNSET,
    min_price: int | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_not_for_sale: bool | Unset = UNSET,
    triggered_by_topic_discovery: bool | Unset = UNSET,
    sales_type_filter: GetV2SearchItemsDetailsSalesTypeFilter | Unset = UNSET,
    topics: str | Unset = UNSET,
    limit: GetV2SearchItemsDetailsLimit | Unset = GetV2SearchItemsDetailsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2SearchItemsDetailsSortOrder | Unset = GetV2SearchItemsDetailsSortOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Taxonomy"] = taxonomy

    json_asset_type_ids: list[int] | Unset = UNSET
    if not isinstance(asset_type_ids, Unset):
        json_asset_type_ids = asset_type_ids

    params["AssetTypeIds"] = json_asset_type_ids

    json_bundle_type_ids: list[int] | Unset = UNSET
    if not isinstance(bundle_type_ids, Unset):
        json_bundle_type_ids = bundle_type_ids

    params["BundleTypeIds"] = json_bundle_type_ids

    json_category_filter: int | Unset = UNSET
    if not isinstance(category_filter, Unset):
        json_category_filter = category_filter.value

    params["CategoryFilter"] = json_category_filter

    json_sort_aggregation: int | Unset = UNSET
    if not isinstance(sort_aggregation, Unset):
        json_sort_aggregation = sort_aggregation.value

    params["SortAggregation"] = json_sort_aggregation

    json_sort_type: int | Unset = UNSET
    if not isinstance(sort_type, Unset):
        json_sort_type = sort_type.value

    params["SortType"] = json_sort_type

    json_creator_type: int | Unset = UNSET
    if not isinstance(creator_type, Unset):
        json_creator_type = creator_type.value

    params["CreatorType"] = json_creator_type

    params["CreatorTargetId"] = creator_target_id

    params["CreatorName"] = creator_name

    params["MaxPrice"] = max_price

    params["MinPrice"] = min_price

    params["Keyword"] = keyword

    params["IncludeNotForSale"] = include_not_for_sale

    params["TriggeredByTopicDiscovery"] = triggered_by_topic_discovery

    json_sales_type_filter: int | Unset = UNSET
    if not isinstance(sales_type_filter, Unset):
        json_sales_type_filter = sales_type_filter.value

    params["SalesTypeFilter"] = json_sales_type_filter

    params["Topics"] = topics

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/search/items/details",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    if response.status_code == 200:
        response_200 = (
            RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    taxonomy: str | Unset = UNSET,
    asset_type_ids: list[int] | Unset = UNSET,
    bundle_type_ids: list[int] | Unset = UNSET,
    category_filter: GetV2SearchItemsDetailsCategoryFilter | Unset = UNSET,
    sort_aggregation: GetV2SearchItemsDetailsSortAggregation | Unset = UNSET,
    sort_type: GetV2SearchItemsDetailsSortType | Unset = UNSET,
    creator_type: GetV2SearchItemsDetailsCreatorType | Unset = UNSET,
    creator_target_id: int | Unset = UNSET,
    creator_name: str | Unset = UNSET,
    max_price: int | Unset = UNSET,
    min_price: int | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_not_for_sale: bool | Unset = UNSET,
    triggered_by_topic_discovery: bool | Unset = UNSET,
    sales_type_filter: GetV2SearchItemsDetailsSalesTypeFilter | Unset = UNSET,
    topics: str | Unset = UNSET,
    limit: GetV2SearchItemsDetailsLimit | Unset = GetV2SearchItemsDetailsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2SearchItemsDetailsSortOrder | Unset = GetV2SearchItemsDetailsSortOrder.DESC,
) -> Response[Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    """Search for catalog items.

     This endpoint is for search by item type ids.

    Args:
        taxonomy (str | Unset):
        asset_type_ids (list[int] | Unset):
        bundle_type_ids (list[int] | Unset):
        category_filter (GetV2SearchItemsDetailsCategoryFilter | Unset):
        sort_aggregation (GetV2SearchItemsDetailsSortAggregation | Unset):
        sort_type (GetV2SearchItemsDetailsSortType | Unset):
        creator_type (GetV2SearchItemsDetailsCreatorType | Unset):
        creator_target_id (int | Unset):
        creator_name (str | Unset):
        max_price (int | Unset):
        min_price (int | Unset):
        keyword (str | Unset):
        include_not_for_sale (bool | Unset):
        triggered_by_topic_discovery (bool | Unset):
        sales_type_filter (GetV2SearchItemsDetailsSalesTypeFilter | Unset):
        topics (str | Unset):
        limit (GetV2SearchItemsDetailsLimit | Unset):  Default:
            GetV2SearchItemsDetailsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2SearchItemsDetailsSortOrder | Unset):  Default:
            GetV2SearchItemsDetailsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]
    """

    kwargs = _get_kwargs(
        taxonomy=taxonomy,
        asset_type_ids=asset_type_ids,
        bundle_type_ids=bundle_type_ids,
        category_filter=category_filter,
        sort_aggregation=sort_aggregation,
        sort_type=sort_type,
        creator_type=creator_type,
        creator_target_id=creator_target_id,
        creator_name=creator_name,
        max_price=max_price,
        min_price=min_price,
        keyword=keyword,
        include_not_for_sale=include_not_for_sale,
        triggered_by_topic_discovery=triggered_by_topic_discovery,
        sales_type_filter=sales_type_filter,
        topics=topics,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    taxonomy: str | Unset = UNSET,
    asset_type_ids: list[int] | Unset = UNSET,
    bundle_type_ids: list[int] | Unset = UNSET,
    category_filter: GetV2SearchItemsDetailsCategoryFilter | Unset = UNSET,
    sort_aggregation: GetV2SearchItemsDetailsSortAggregation | Unset = UNSET,
    sort_type: GetV2SearchItemsDetailsSortType | Unset = UNSET,
    creator_type: GetV2SearchItemsDetailsCreatorType | Unset = UNSET,
    creator_target_id: int | Unset = UNSET,
    creator_name: str | Unset = UNSET,
    max_price: int | Unset = UNSET,
    min_price: int | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_not_for_sale: bool | Unset = UNSET,
    triggered_by_topic_discovery: bool | Unset = UNSET,
    sales_type_filter: GetV2SearchItemsDetailsSalesTypeFilter | Unset = UNSET,
    topics: str | Unset = UNSET,
    limit: GetV2SearchItemsDetailsLimit | Unset = GetV2SearchItemsDetailsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2SearchItemsDetailsSortOrder | Unset = GetV2SearchItemsDetailsSortOrder.DESC,
) -> Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    """Search for catalog items.

     This endpoint is for search by item type ids.

    Args:
        taxonomy (str | Unset):
        asset_type_ids (list[int] | Unset):
        bundle_type_ids (list[int] | Unset):
        category_filter (GetV2SearchItemsDetailsCategoryFilter | Unset):
        sort_aggregation (GetV2SearchItemsDetailsSortAggregation | Unset):
        sort_type (GetV2SearchItemsDetailsSortType | Unset):
        creator_type (GetV2SearchItemsDetailsCreatorType | Unset):
        creator_target_id (int | Unset):
        creator_name (str | Unset):
        max_price (int | Unset):
        min_price (int | Unset):
        keyword (str | Unset):
        include_not_for_sale (bool | Unset):
        triggered_by_topic_discovery (bool | Unset):
        sales_type_filter (GetV2SearchItemsDetailsSalesTypeFilter | Unset):
        topics (str | Unset):
        limit (GetV2SearchItemsDetailsLimit | Unset):  Default:
            GetV2SearchItemsDetailsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2SearchItemsDetailsSortOrder | Unset):  Default:
            GetV2SearchItemsDetailsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2
    """

    return sync_detailed(
        client=client,
        taxonomy=taxonomy,
        asset_type_ids=asset_type_ids,
        bundle_type_ids=bundle_type_ids,
        category_filter=category_filter,
        sort_aggregation=sort_aggregation,
        sort_type=sort_type,
        creator_type=creator_type,
        creator_target_id=creator_target_id,
        creator_name=creator_name,
        max_price=max_price,
        min_price=min_price,
        keyword=keyword,
        include_not_for_sale=include_not_for_sale,
        triggered_by_topic_discovery=triggered_by_topic_discovery,
        sales_type_filter=sales_type_filter,
        topics=topics,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    taxonomy: str | Unset = UNSET,
    asset_type_ids: list[int] | Unset = UNSET,
    bundle_type_ids: list[int] | Unset = UNSET,
    category_filter: GetV2SearchItemsDetailsCategoryFilter | Unset = UNSET,
    sort_aggregation: GetV2SearchItemsDetailsSortAggregation | Unset = UNSET,
    sort_type: GetV2SearchItemsDetailsSortType | Unset = UNSET,
    creator_type: GetV2SearchItemsDetailsCreatorType | Unset = UNSET,
    creator_target_id: int | Unset = UNSET,
    creator_name: str | Unset = UNSET,
    max_price: int | Unset = UNSET,
    min_price: int | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_not_for_sale: bool | Unset = UNSET,
    triggered_by_topic_discovery: bool | Unset = UNSET,
    sales_type_filter: GetV2SearchItemsDetailsSalesTypeFilter | Unset = UNSET,
    topics: str | Unset = UNSET,
    limit: GetV2SearchItemsDetailsLimit | Unset = GetV2SearchItemsDetailsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2SearchItemsDetailsSortOrder | Unset = GetV2SearchItemsDetailsSortOrder.DESC,
) -> Response[Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    """Search for catalog items.

     This endpoint is for search by item type ids.

    Args:
        taxonomy (str | Unset):
        asset_type_ids (list[int] | Unset):
        bundle_type_ids (list[int] | Unset):
        category_filter (GetV2SearchItemsDetailsCategoryFilter | Unset):
        sort_aggregation (GetV2SearchItemsDetailsSortAggregation | Unset):
        sort_type (GetV2SearchItemsDetailsSortType | Unset):
        creator_type (GetV2SearchItemsDetailsCreatorType | Unset):
        creator_target_id (int | Unset):
        creator_name (str | Unset):
        max_price (int | Unset):
        min_price (int | Unset):
        keyword (str | Unset):
        include_not_for_sale (bool | Unset):
        triggered_by_topic_discovery (bool | Unset):
        sales_type_filter (GetV2SearchItemsDetailsSalesTypeFilter | Unset):
        topics (str | Unset):
        limit (GetV2SearchItemsDetailsLimit | Unset):  Default:
            GetV2SearchItemsDetailsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2SearchItemsDetailsSortOrder | Unset):  Default:
            GetV2SearchItemsDetailsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]
    """

    kwargs = _get_kwargs(
        taxonomy=taxonomy,
        asset_type_ids=asset_type_ids,
        bundle_type_ids=bundle_type_ids,
        category_filter=category_filter,
        sort_aggregation=sort_aggregation,
        sort_type=sort_type,
        creator_type=creator_type,
        creator_target_id=creator_target_id,
        creator_name=creator_name,
        max_price=max_price,
        min_price=min_price,
        keyword=keyword,
        include_not_for_sale=include_not_for_sale,
        triggered_by_topic_discovery=triggered_by_topic_discovery,
        sales_type_filter=sales_type_filter,
        topics=topics,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    taxonomy: str | Unset = UNSET,
    asset_type_ids: list[int] | Unset = UNSET,
    bundle_type_ids: list[int] | Unset = UNSET,
    category_filter: GetV2SearchItemsDetailsCategoryFilter | Unset = UNSET,
    sort_aggregation: GetV2SearchItemsDetailsSortAggregation | Unset = UNSET,
    sort_type: GetV2SearchItemsDetailsSortType | Unset = UNSET,
    creator_type: GetV2SearchItemsDetailsCreatorType | Unset = UNSET,
    creator_target_id: int | Unset = UNSET,
    creator_name: str | Unset = UNSET,
    max_price: int | Unset = UNSET,
    min_price: int | Unset = UNSET,
    keyword: str | Unset = UNSET,
    include_not_for_sale: bool | Unset = UNSET,
    triggered_by_topic_discovery: bool | Unset = UNSET,
    sales_type_filter: GetV2SearchItemsDetailsSalesTypeFilter | Unset = UNSET,
    topics: str | Unset = UNSET,
    limit: GetV2SearchItemsDetailsLimit | Unset = GetV2SearchItemsDetailsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2SearchItemsDetailsSortOrder | Unset = GetV2SearchItemsDetailsSortOrder.DESC,
) -> Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    """Search for catalog items.

     This endpoint is for search by item type ids.

    Args:
        taxonomy (str | Unset):
        asset_type_ids (list[int] | Unset):
        bundle_type_ids (list[int] | Unset):
        category_filter (GetV2SearchItemsDetailsCategoryFilter | Unset):
        sort_aggregation (GetV2SearchItemsDetailsSortAggregation | Unset):
        sort_type (GetV2SearchItemsDetailsSortType | Unset):
        creator_type (GetV2SearchItemsDetailsCreatorType | Unset):
        creator_target_id (int | Unset):
        creator_name (str | Unset):
        max_price (int | Unset):
        min_price (int | Unset):
        keyword (str | Unset):
        include_not_for_sale (bool | Unset):
        triggered_by_topic_discovery (bool | Unset):
        sales_type_filter (GetV2SearchItemsDetailsSalesTypeFilter | Unset):
        topics (str | Unset):
        limit (GetV2SearchItemsDetailsLimit | Unset):  Default:
            GetV2SearchItemsDetailsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2SearchItemsDetailsSortOrder | Unset):  Default:
            GetV2SearchItemsDetailsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2
    """

    return (
        await asyncio_detailed(
            client=client,
            taxonomy=taxonomy,
            asset_type_ids=asset_type_ids,
            bundle_type_ids=bundle_type_ids,
            category_filter=category_filter,
            sort_aggregation=sort_aggregation,
            sort_type=sort_type,
            creator_type=creator_type,
            creator_target_id=creator_target_id,
            creator_name=creator_name,
            max_price=max_price,
            min_price=min_price,
            keyword=keyword,
            include_not_for_sale=include_not_for_sale,
            triggered_by_topic_discovery=triggered_by_topic_discovery,
            sales_type_filter=sales_type_filter,
            topics=topics,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
