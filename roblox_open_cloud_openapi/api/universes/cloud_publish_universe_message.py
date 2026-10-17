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
from ...types import Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': True}, 'x-roblox-rate-limits': {'description': 'Messaging Service requests are subject to additional throttling limits described in the [Open Cloud guide for Messaging Service](https://create.roblox.com/docs/cloud/guides/usage-messaging#limits).', 'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 5000}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 5000}}, 'x-roblox-scopes': [{'name': 'universe-messaging-service:publish'}], 'x-roblox-docs': {'category': 'Universes and places', 'methodProperties': {'scopes': ['universe-messaging-service:publish']}, 'resource': {'$ref': '#/components/schemas/Universe', 'name': 'Universe'}}, 'x-roblox-stability': 'STABLE'}
"""


from ...models.publish_universe_message_request import PublishUniverseMessageRequest


def _get_kwargs(
    universe_id: str,
    *,
    body: PublishUniverseMessageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}:publishMessage".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: PublishUniverseMessageRequest,
) -> Response[Any]:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (PublishUniverseMessageRequest): Publish a message on the specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: PublishUniverseMessageRequest,
) -> Response[Any]:
    """Publish Universe Message

     Publishes a message to the universe's live servers.

    Servers can consume messages via
    [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

    Args:
        universe_id (str):
        body (PublishUniverseMessageRequest): Publish a message on the specified topic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
