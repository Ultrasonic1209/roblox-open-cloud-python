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
{'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/cloud/v2/universes/{universeId}:publishMessage', 'httpMethod': 'POST', 'documentationUrl': 'https://create.roblox.com/docs/cloud/reference/features/universes#Cloud_PublishUniverseMessage'}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 5000}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 5000}}, 'x-roblox-scopes': [{'name': 'universe-messaging-service:publish', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.cross_server_messaging_models_requests_publish_request import (
    CrossServerMessagingModelsRequestsPublishRequest,
)
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    topic: str,
    *,
    body: CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messaging-service/v1/universes/{universe_id}/topics/{topic}".format(
            universe_id=quote(str(universe_id), safe=""),
            topic=quote(str(topic), safe=""),
        ),
    }

    if isinstance(body, CrossServerMessagingModelsRequestsPublishRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CrossServerMessagingModelsRequestsPublishRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CrossServerMessagingModelsRequestsPublishRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 500:
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/universes#CrossServerMessaging_Publish"
)
def sync_detailed(
    universe_id: int,
    topic: str,
    *,
    client: AuthenticatedClient,
    body: CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Publish a cross-server message to a universe

     Publish a message to a pre-defined topic of an experience, with the size of the message up to 1,024
    characters (1 KB). Requires the **Publish** permission for API keys and the **universe-messaging-
    service:publish** scope for OAuth 2.0 apps. See [Cross-server messaging](/cloud-services/cross-
    server-messaging.md#subscribe-users-to-receive-messages) for defining and subscribing users to a
    topic.

    Args:
        universe_id (int):
        topic (str):
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        topic=topic,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/universes#CrossServerMessaging_Publish"
)
async def asyncio_detailed(
    universe_id: int,
    topic: str,
    *,
    client: AuthenticatedClient,
    body: CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | CrossServerMessagingModelsRequestsPublishRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Publish a cross-server message to a universe

     Publish a message to a pre-defined topic of an experience, with the size of the message up to 1,024
    characters (1 KB). Requires the **Publish** permission for API keys and the **universe-messaging-
    service:publish** scope for OAuth 2.0 apps. See [Cross-server messaging](/cloud-services/cross-
    server-messaging.md#subscribe-users-to-receive-messages) for defining and subscribing users to a
    topic.

    Args:
        universe_id (int):
        topic (str):
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.
        body (CrossServerMessagingModelsRequestsPublishRequest | Unset): The request body object
            with the message string that you want to publish to the live server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        topic=topic,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
