from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_thumbnail_personalization_request import CreateThumbnailPersonalizationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/thumbnail-personalization-api/v1/universes/{universe_id}/personalization/create".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 50},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 50},
                },
                "x-roblox-scopes": [{"name": "universe.thumbnail:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "ThumbnailPersonalizationApi.HomepageThumbnail_CreateThumbnailPersonalization",
        },
    }

    if isinstance(body, CreateThumbnailPersonalizationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateThumbnailPersonalizationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateThumbnailPersonalizationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateThumbnailPersonalizationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 401:
        response_401 = cast(str, response.json())
        return response_401

    if response.status_code == 403:
        response_403 = cast(str, response.json())
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | Unset = UNSET,
) -> Response[Any | str]:
    """Creates a new active thumbnail personalization configuration for a universe.
    This deactivates the current active configuration, and the new configuration starts its own
    statistics.

    Args:
        universe_id (int):
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | Unset = UNSET,
) -> Any | str | None:
    """Creates a new active thumbnail personalization configuration for a universe.
    This deactivates the current active configuration, and the new configuration starts its own
    statistics.

    Args:
        universe_id (int):
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | Unset = UNSET,
) -> Response[Any | str]:
    """Creates a new active thumbnail personalization configuration for a universe.
    This deactivates the current active configuration, and the new configuration starts its own
    statistics.

    Args:
        universe_id (int):
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | CreateThumbnailPersonalizationRequest
    | Unset = UNSET,
) -> Any | str | None:
    """Creates a new active thumbnail personalization configuration for a universe.
    This deactivates the current active configuration, and the new configuration starts its own
    statistics.

    Args:
        universe_id (int):
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.
        body (CreateThumbnailPersonalizationRequest): The request to create a thumbnail
            personalization configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
