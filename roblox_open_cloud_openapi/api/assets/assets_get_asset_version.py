from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_version import AssetVersion
from ...types import Response


def _get_kwargs(
    asset_id: str,
    version_number: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/assets/{asset_id}/versions/{version_number}".format(
            asset_id=quote(str(asset_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | AssetVersion | None:
    if response.status_code == 200:
        response_200 = AssetVersion.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | AssetVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    version_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | AssetVersion]:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (str):
        version_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetVersion]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_number: str,
    *,
    client: AuthenticatedClient,
) -> Any | AssetVersion | None:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (str):
        version_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetVersion
    """

    return sync_detailed(
        asset_id=asset_id,
        version_number=version_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | AssetVersion]:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (str):
        version_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetVersion]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_number: str,
    *,
    client: AuthenticatedClient,
) -> Any | AssetVersion | None:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (str):
        version_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetVersion
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_number=version_number,
            client=client,
        )
    ).parsed
