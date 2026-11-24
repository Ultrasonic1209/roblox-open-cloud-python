from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-rate-limits': {'description': 'Messaging Service requests are subject to additional throttling limits described in the [Open Cloud guide for Messaging Service](https://create.roblox.com/docs/cloud/guides/usage-messaging#limits).', 'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 5000}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 5000}}, 'x-roblox-stability': 'STABLE', 'x-roblox-scopes': [{'name': 'universe-messaging-service:publish', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.google_protobuf_well_known_types_empty import GoogleProtobufWellKnownTypesEmpty
from ...models.roblox_open_cloud_cloud_v2_publish_universe_message_request import (
    RobloxOpenCloudCloudV2PublishUniverseMessageRequest,
)


def _get_kwargs(
    universe_id: str,
    *,
    body: RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}:publishMessage".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, RobloxOpenCloudCloudV2PublishUniverseMessageRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxOpenCloudCloudV2PublishUniverseMessageRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GoogleProtobufWellKnownTypesEmpty | None:
    if response.status_code == 200:
        response_200 = GoogleProtobufWellKnownTypesEmpty.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GoogleProtobufWellKnownTypesEmpty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | Unset = UNSET,
) -> Response[GoogleProtobufWellKnownTypesEmpty]:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleProtobufWellKnownTypesEmpty]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | Unset = UNSET,
) -> GoogleProtobufWellKnownTypesEmpty | None:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleProtobufWellKnownTypesEmpty
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | Unset = UNSET,
) -> Response[GoogleProtobufWellKnownTypesEmpty]:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleProtobufWellKnownTypesEmpty]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | RobloxOpenCloudCloudV2PublishUniverseMessageRequest
    | Unset = UNSET,
) -> GoogleProtobufWellKnownTypesEmpty | None:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.
        body (RobloxOpenCloudCloudV2PublishUniverseMessageRequest): Publish a message on the
            specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleProtobufWellKnownTypesEmpty
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
