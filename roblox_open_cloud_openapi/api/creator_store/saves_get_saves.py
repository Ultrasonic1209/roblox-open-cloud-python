from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_saves_response_type_0 import GetSavesResponseType0
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...models.saves_sort_category import SavesSortCategory
from ...models.search_category_type import SearchCategoryType
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    target_type: None | SearchCategoryType | Unset = UNSET,
    target_id: int | None | Unset = UNSET,
    collection_name: str | Unset = UNSET,
    sort_by: SavesSortCategory | Unset = SavesSortCategory.DATE_SAVED,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    limit: int | Unset = 100,
    page: int | Unset = 1,
    keyword: str | Unset = UNSET,
    hide_owned_assets: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type: None | str | Unset
    if isinstance(target_type, Unset):
        json_target_type = UNSET
    elif isinstance(target_type, SearchCategoryType):
        json_target_type = target_type.value
    else:
        json_target_type = target_type
    params["targetType"] = json_target_type

    json_target_id: int | None | Unset
    if isinstance(target_id, Unset):
        json_target_id = UNSET
    else:
        json_target_id = target_id
    params["targetId"] = json_target_id

    params["collectionName"] = collection_name

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params["limit"] = limit

    params["page"] = page

    params["keyword"] = keyword

    params["hideOwnedAssets"] = hide_owned_assets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/toolbox-service/v1/saves",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 200},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 200},
                },
                "x-roblox-scopes": [{"name": "creator-store-save:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "Saves_GetSaves",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetSavesResponseType0 | None | None | ProblemDetailsType0 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> GetSavesResponseType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_get_saves_response_type_0 = GetSavesResponseType0.from_dict(data)

                return componentsschemas_get_saves_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSavesResponseType0 | None, data)

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetSavesResponseType0 | None | None | ProblemDetailsType0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: None | SearchCategoryType | Unset = UNSET,
    target_id: int | None | Unset = UNSET,
    collection_name: str | Unset = UNSET,
    sort_by: SavesSortCategory | Unset = SavesSortCategory.DATE_SAVED,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    limit: int | Unset = 100,
    page: int | Unset = 1,
    keyword: str | Unset = UNSET,
    hide_owned_assets: bool | Unset = False,
) -> Response[GetSavesResponseType0 | None | None | ProblemDetailsType0]:
    """Gets saves from a collection.

    Args:
        target_type (None | SearchCategoryType | Unset):
        target_id (int | None | Unset):
        collection_name (str | Unset):
        sort_by (SavesSortCategory | Unset): The category to sort the saves by. Default:
            SavesSortCategory.DATE_SAVED.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        keyword (str | Unset):
        hide_owned_assets (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavesResponseType0 | None | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        page=page,
        keyword=keyword,
        hide_owned_assets=hide_owned_assets,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: None | SearchCategoryType | Unset = UNSET,
    target_id: int | None | Unset = UNSET,
    collection_name: str | Unset = UNSET,
    sort_by: SavesSortCategory | Unset = SavesSortCategory.DATE_SAVED,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    limit: int | Unset = 100,
    page: int | Unset = 1,
    keyword: str | Unset = UNSET,
    hide_owned_assets: bool | Unset = False,
) -> GetSavesResponseType0 | None | None | ProblemDetailsType0 | None:
    """Gets saves from a collection.

    Args:
        target_type (None | SearchCategoryType | Unset):
        target_id (int | None | Unset):
        collection_name (str | Unset):
        sort_by (SavesSortCategory | Unset): The category to sort the saves by. Default:
            SavesSortCategory.DATE_SAVED.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        keyword (str | Unset):
        hide_owned_assets (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavesResponseType0 | None | None | ProblemDetailsType0
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        page=page,
        keyword=keyword,
        hide_owned_assets=hide_owned_assets,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: None | SearchCategoryType | Unset = UNSET,
    target_id: int | None | Unset = UNSET,
    collection_name: str | Unset = UNSET,
    sort_by: SavesSortCategory | Unset = SavesSortCategory.DATE_SAVED,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    limit: int | Unset = 100,
    page: int | Unset = 1,
    keyword: str | Unset = UNSET,
    hide_owned_assets: bool | Unset = False,
) -> Response[GetSavesResponseType0 | None | None | ProblemDetailsType0]:
    """Gets saves from a collection.

    Args:
        target_type (None | SearchCategoryType | Unset):
        target_id (int | None | Unset):
        collection_name (str | Unset):
        sort_by (SavesSortCategory | Unset): The category to sort the saves by. Default:
            SavesSortCategory.DATE_SAVED.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        keyword (str | Unset):
        hide_owned_assets (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavesResponseType0 | None | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
        sort_by=sort_by,
        sort_direction=sort_direction,
        limit=limit,
        page=page,
        keyword=keyword,
        hide_owned_assets=hide_owned_assets,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: None | SearchCategoryType | Unset = UNSET,
    target_id: int | None | Unset = UNSET,
    collection_name: str | Unset = UNSET,
    sort_by: SavesSortCategory | Unset = SavesSortCategory.DATE_SAVED,
    sort_direction: SortDirection | Unset = SortDirection.NONE,
    limit: int | Unset = 100,
    page: int | Unset = 1,
    keyword: str | Unset = UNSET,
    hide_owned_assets: bool | Unset = False,
) -> GetSavesResponseType0 | None | None | ProblemDetailsType0 | None:
    """Gets saves from a collection.

    Args:
        target_type (None | SearchCategoryType | Unset):
        target_id (int | None | Unset):
        collection_name (str | Unset):
        sort_by (SavesSortCategory | Unset): The category to sort the saves by. Default:
            SavesSortCategory.DATE_SAVED.
        sort_direction (SortDirection | Unset): Represents the direction in which to sort the
            results Default: SortDirection.NONE.
        limit (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
        keyword (str | Unset):
        hide_owned_assets (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavesResponseType0 | None | None | ProblemDetailsType0
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            target_id=target_id,
            collection_name=collection_name,
            sort_by=sort_by,
            sort_direction=sort_direction,
            limit=limit,
            page=page,
            keyword=keyword,
            hide_owned_assets=hide_owned_assets,
        )
    ).parsed
