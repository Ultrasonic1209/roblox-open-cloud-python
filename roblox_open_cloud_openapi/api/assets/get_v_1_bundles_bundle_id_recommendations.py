from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_catalog_api_bundle_details_model import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bundle_id: int,
    *,
    num_items: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["numItems"] = num_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/bundles/{bundle_id}/recommendations".format(
            bundle_id=quote(str(bundle_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_bundles_bundleId_recommendations",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel.from_dict(
            response.json()
        )

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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel]:
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
    num_items: int | Unset = 20,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel]:
    """Gets recommendations for a given bundle, bundleId of 0 returns randomized bundles
    - Accepts both public and authenticated users.

    Args:
        bundle_id (int):
        num_items (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        num_items=num_items,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
    num_items: int | Unset = 20,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel | None:
    """Gets recommendations for a given bundle, bundleId of 0 returns randomized bundles
    - Accepts both public and authenticated users.

    Args:
        bundle_id (int):
        num_items (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel
    """

    return sync_detailed(
        bundle_id=bundle_id,
        client=client,
        num_items=num_items,
    ).parsed


async def asyncio_detailed(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
    num_items: int | Unset = 20,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel]:
    """Gets recommendations for a given bundle, bundleId of 0 returns randomized bundles
    - Accepts both public and authenticated users.

    Args:
        bundle_id (int):
        num_items (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        num_items=num_items,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_id: int,
    *,
    client: AuthenticatedClient,
    num_items: int | Unset = 20,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel | None:
    """Gets recommendations for a given bundle, bundleId of 0 returns randomized bundles
    - Accepts both public and authenticated users.

    Args:
        bundle_id (int):
        num_items (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiBundleDetailsModel
    """

    return (
        await asyncio_detailed(
            bundle_id=bundle_id,
            client=client,
            num_items=num_items,
        )
    ).parsed
