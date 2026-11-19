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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 1}}, 'x-roblox-scopes': [{'name': 'marketplace.item:write', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_request_update_collectible_item_request import (
    RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest,
)


def _get_kwargs(
    collectible_item_id: str,
    *,
    body: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/{collectible_item_id}".format(
            collectible_item_id=quote(str(collectible_item_id), safe=""),
        ),
    }

    if isinstance(body, RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

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

    if response.status_code == 404:
        return None

    if response.status_code == 409:
        return None

    if response.status_code == 412:
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


def sync_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Update product information about a published Collectible Item.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest): Api request to
            update a collectible item.
        body (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest): Api request to
            update a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Update product information about a published Collectible Item.

    Args:
        collectible_item_id (str):
        body (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest): Api request to
            update a collectible item.
        body (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest): Api request to
            update a collectible item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
