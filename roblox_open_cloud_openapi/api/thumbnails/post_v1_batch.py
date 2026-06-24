from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_thumbnails_apis_models_thumbnail_batch_request import (
    RobloxThumbnailsApisModelsThumbnailBatchRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://thumbnails.roblox.com/v1/batch",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "post_v1_batch",
        },
    }

    if isinstance(body, list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any]:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any]:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
