from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_multiget_item_details_request_model import (
    RobloxCatalogApiMultigetItemDetailsRequestModel,
)
from ...models.roblox_web_web_api_models_api_array_response_roblox_catalog_api_catalog_search_detailed_response_item_v2 import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://catalog.roblox.com/v1/catalog/items/details",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_catalog_items_details",
    }

    if isinstance(body, RobloxCatalogApiMultigetItemDetailsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxCatalogApiMultigetItemDetailsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2.from_dict(
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    """Returns details for one or more catalog items.

     There is an item count limit per request. Exceeding this returns 400 Bad Request.

    Args:
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    """Returns details for one or more catalog items.

     There is an item count limit per request. Exceeding this returns 400 Bad Request.

    Args:
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]:
    """Returns details for one or more catalog items.

     There is an item count limit per request. Exceeding this returns 400 Bad Request.

    Args:
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2 | None:
    """Returns details for one or more catalog items.

     There is an item count limit per request. Exceeding this returns 400 Bad Request.

    Args:
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
