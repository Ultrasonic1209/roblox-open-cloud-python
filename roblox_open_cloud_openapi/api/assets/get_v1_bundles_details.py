from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_bundle_details_model import RobloxCatalogApiBundleDetailsModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    bundle_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_bundle_ids = bundle_ids

    params["bundleIds"] = json_bundle_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/bundles/details",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RobloxCatalogApiBundleDetailsModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxCatalogApiBundleDetailsModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[RobloxCatalogApiBundleDetailsModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bundle_ids: list[int],
) -> Response[Any | list[RobloxCatalogApiBundleDetailsModel]]:
    """Returns details about the given bundleIds.

    Args:
        bundle_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxCatalogApiBundleDetailsModel]]
    """

    kwargs = _get_kwargs(
        bundle_ids=bundle_ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bundle_ids: list[int],
) -> Any | list[RobloxCatalogApiBundleDetailsModel] | None:
    """Returns details about the given bundleIds.

    Args:
        bundle_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxCatalogApiBundleDetailsModel]
    """

    return sync_detailed(
        client=client,
        bundle_ids=bundle_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bundle_ids: list[int],
) -> Response[Any | list[RobloxCatalogApiBundleDetailsModel]]:
    """Returns details about the given bundleIds.

    Args:
        bundle_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxCatalogApiBundleDetailsModel]]
    """

    kwargs = _get_kwargs(
        bundle_ids=bundle_ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bundle_ids: list[int],
) -> Any | list[RobloxCatalogApiBundleDetailsModel] | None:
    """Returns details about the given bundleIds.

    Args:
        bundle_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxCatalogApiBundleDetailsModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            bundle_ids=bundle_ids,
        )
    ).parsed
