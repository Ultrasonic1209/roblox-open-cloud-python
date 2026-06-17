from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_bundle_details_model import RobloxCatalogApiBundleDetailsModel
from ...types import Response


def _get_kwargs(
    bundle_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/bundles/{bundle_id}/details".format(
            bundle_id=quote(str(bundle_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxCatalogApiBundleDetailsModel | None:
    if response.status_code == 200:
        response_200 = RobloxCatalogApiBundleDetailsModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxCatalogApiBundleDetailsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxCatalogApiBundleDetailsModel]:
    """Returns details about the given bundleId.

    Args:
        bundle_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxCatalogApiBundleDetailsModel | None:
    """Returns details about the given bundleId.

    Args:
        bundle_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiBundleDetailsModel
    """

    return sync_detailed(
        bundle_id=bundle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxCatalogApiBundleDetailsModel]:
    """Returns details about the given bundleId.

    Args:
        bundle_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxCatalogApiBundleDetailsModel | None:
    """Returns details about the given bundleId.

    Args:
        bundle_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiBundleDetailsModel
    """

    return (
        await asyncio_detailed(
            bundle_id=bundle_id,
            client=client,
        )
    ).parsed
