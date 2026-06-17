from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_favorite_bundles_response import RobloxCatalogApiFavoriteBundlesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    subtype_id: int,
    *,
    items_per_page: int | Unset = 24,
    cursor: str | Unset = UNSET,
    is_previous: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["itemsPerPage"] = items_per_page

    params["cursor"] = cursor

    params["isPrevious"] = is_previous

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/favorites/users/{user_id}/favorites/{subtype_id}/bundles".format(
            user_id=quote(str(user_id), safe=""),
            subtype_id=quote(str(subtype_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxCatalogApiFavoriteBundlesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxCatalogApiFavoriteBundlesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxCatalogApiFavoriteBundlesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    subtype_id: int,
    *,
    client: AuthenticatedClient,
    items_per_page: int | Unset = 24,
    cursor: str | Unset = UNSET,
    is_previous: bool | Unset = False,
) -> Response[Any | RobloxCatalogApiFavoriteBundlesResponse]:
    """Lists the bundles favorited by a given user with the given bundle subtypeId.Switched to EAAS style
    pagination cursors since July 2024.

    Args:
        user_id (int):
        subtype_id (int):
        items_per_page (int | Unset):  Default: 24.
        cursor (str | Unset):
        is_previous (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiFavoriteBundlesResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        subtype_id=subtype_id,
        items_per_page=items_per_page,
        cursor=cursor,
        is_previous=is_previous,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    subtype_id: int,
    *,
    client: AuthenticatedClient,
    items_per_page: int | Unset = 24,
    cursor: str | Unset = UNSET,
    is_previous: bool | Unset = False,
) -> Any | RobloxCatalogApiFavoriteBundlesResponse | None:
    """Lists the bundles favorited by a given user with the given bundle subtypeId.Switched to EAAS style
    pagination cursors since July 2024.

    Args:
        user_id (int):
        subtype_id (int):
        items_per_page (int | Unset):  Default: 24.
        cursor (str | Unset):
        is_previous (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiFavoriteBundlesResponse
    """

    return sync_detailed(
        user_id=user_id,
        subtype_id=subtype_id,
        client=client,
        items_per_page=items_per_page,
        cursor=cursor,
        is_previous=is_previous,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    subtype_id: int,
    *,
    client: AuthenticatedClient,
    items_per_page: int | Unset = 24,
    cursor: str | Unset = UNSET,
    is_previous: bool | Unset = False,
) -> Response[Any | RobloxCatalogApiFavoriteBundlesResponse]:
    """Lists the bundles favorited by a given user with the given bundle subtypeId.Switched to EAAS style
    pagination cursors since July 2024.

    Args:
        user_id (int):
        subtype_id (int):
        items_per_page (int | Unset):  Default: 24.
        cursor (str | Unset):
        is_previous (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiFavoriteBundlesResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        subtype_id=subtype_id,
        items_per_page=items_per_page,
        cursor=cursor,
        is_previous=is_previous,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    subtype_id: int,
    *,
    client: AuthenticatedClient,
    items_per_page: int | Unset = 24,
    cursor: str | Unset = UNSET,
    is_previous: bool | Unset = False,
) -> Any | RobloxCatalogApiFavoriteBundlesResponse | None:
    """Lists the bundles favorited by a given user with the given bundle subtypeId.Switched to EAAS style
    pagination cursors since July 2024.

    Args:
        user_id (int):
        subtype_id (int):
        items_per_page (int | Unset):  Default: 24.
        cursor (str | Unset):
        is_previous (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiFavoriteBundlesResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            subtype_id=subtype_id,
            client=client,
            items_per_page=items_per_page,
            cursor=cursor,
            is_previous=is_previous,
        )
    ).parsed
