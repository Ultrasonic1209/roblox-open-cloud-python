from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 1}}, 'x-roblox-scopes': [{'name': 'marketplace.item:publish', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_request_collectibles_restock_collectible_item_request import (
    RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest,
)
from ...models.roblox_item_configuration_api_models_response_collectibles_restock_collectible_item_response import (
    RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse,
)


def _get_kwargs(
    collectible_item_id: str,
    *,
    body: RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/{collectible_item_id}/restock".format(
            collectible_item_id=quote(str(collectible_item_id), safe=""),
        ),
    }

    if isinstance(body, RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse]:
    """Restock a published limited collectible item by adding additional quantity.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse | None:
    """Restock a published limited collectible item by adding additional quantity.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse
    """

    return sync_detailed(
        collectible_item_id=collectible_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse]:
    """Restock a published limited collectible item by adding additional quantity.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest
    | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse | None:
    """Restock a published limited collectible item by adding additional quantity.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.
        body (RobloxItemConfigurationApiModelsRequestCollectiblesRestockCollectibleItemRequest):
            Request model for restocking a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockCollectibleItemResponse
    """

    return (
        await asyncio_detailed(
            collectible_item_id=collectible_item_id,
            client=client,
            body=body,
        )
    ).parsed
