from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_thumbnails_apis_models_thumbnail_batch_request import (
    RobloxThumbnailsApisModelsThumbnailBatchRequest,
)
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_batch_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse,
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
        "url": "/v1/batch",
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse.from_dict(
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse]:
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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse]:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse | None:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse]:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | list[RobloxThumbnailsApisModelsThumbnailBatchRequest]
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse | None:
    """Returns a list of thumbnails with varying types and sizes

    Args:
        roblox_place_id (int | Unset):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):
        body (list[RobloxThumbnailsApisModelsThumbnailBatchRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailBatchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
