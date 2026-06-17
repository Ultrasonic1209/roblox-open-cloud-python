from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_catalog_api_topic_request_model import RobloxCatalogApiTopicRequestModel
from ...models.roblox_catalog_api_topic_response import RobloxCatalogApiTopicResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxCatalogApiTopicRequestModel | RobloxCatalogApiTopicRequestModel | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://catalog.roblox.com/v1/topic/get-topics",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_topic_get-topics",
    }

    if isinstance(body, RobloxCatalogApiTopicRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxCatalogApiTopicRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxCatalogApiTopicResponse | None:
    if response.status_code == 200:
        response_200 = RobloxCatalogApiTopicResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxCatalogApiTopicResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiTopicRequestModel | RobloxCatalogApiTopicRequestModel | Unset = UNSET,
) -> Response[Any | RobloxCatalogApiTopicResponse]:
    """Get topic given TopicRequestModel.

    Args:
        body (RobloxCatalogApiTopicRequestModel):
        body (RobloxCatalogApiTopicRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiTopicResponse]
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
    body: RobloxCatalogApiTopicRequestModel | RobloxCatalogApiTopicRequestModel | Unset = UNSET,
) -> Any | RobloxCatalogApiTopicResponse | None:
    """Get topic given TopicRequestModel.

    Args:
        body (RobloxCatalogApiTopicRequestModel):
        body (RobloxCatalogApiTopicRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiTopicResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiTopicRequestModel | RobloxCatalogApiTopicRequestModel | Unset = UNSET,
) -> Response[Any | RobloxCatalogApiTopicResponse]:
    """Get topic given TopicRequestModel.

    Args:
        body (RobloxCatalogApiTopicRequestModel):
        body (RobloxCatalogApiTopicRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiTopicResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiTopicRequestModel | RobloxCatalogApiTopicRequestModel | Unset = UNSET,
) -> Any | RobloxCatalogApiTopicResponse | None:
    """Get topic given TopicRequestModel.

    Args:
        body (RobloxCatalogApiTopicRequestModel):
        body (RobloxCatalogApiTopicRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiTopicResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
