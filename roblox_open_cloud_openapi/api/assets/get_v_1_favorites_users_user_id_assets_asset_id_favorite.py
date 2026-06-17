from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_asset_favorite_model import RobloxCatalogApiAssetFavoriteModel
from ...types import Response


def _get_kwargs(
    user_id: int,
    asset_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/favorites/users/{user_id}/assets/{asset_id}/favorite".format(
            user_id=quote(str(user_id), safe=""),
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxCatalogApiAssetFavoriteModel | None:
    if response.status_code == 200:
        response_200 = RobloxCatalogApiAssetFavoriteModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxCatalogApiAssetFavoriteModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxCatalogApiAssetFavoriteModel]:
    """Gets the favorite model for the asset and user.

    Args:
        user_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiAssetFavoriteModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_id=asset_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxCatalogApiAssetFavoriteModel | None:
    """Gets the favorite model for the asset and user.

    Args:
        user_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiAssetFavoriteModel
    """

    return sync_detailed(
        user_id=user_id,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxCatalogApiAssetFavoriteModel]:
    """Gets the favorite model for the asset and user.

    Args:
        user_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiAssetFavoriteModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxCatalogApiAssetFavoriteModel | None:
    """Gets the favorite model for the asset and user.

    Args:
        user_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiAssetFavoriteModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
