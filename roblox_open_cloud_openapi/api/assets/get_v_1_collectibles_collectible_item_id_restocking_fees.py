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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_response_collectibles_restocking_fee_response import (
    RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse,
)


def _get_kwargs(
    collectible_item_id: str,
    *,
    additional_quantity: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["AdditionalQuantity"] = additional_quantity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/{collectible_item_id}/restocking-fees".format(
            collectible_item_id=quote(str(collectible_item_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse]:
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
    additional_quantity: int,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse]:
    """Get the restocking fee for a given collectible item and additional quantity.

    Args:
        collectible_item_id (str):
        additional_quantity (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        additional_quantity=additional_quantity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    additional_quantity: int,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse | None:
    """Get the restocking fee for a given collectible item and additional quantity.

    Args:
        collectible_item_id (str):
        additional_quantity (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse
    """

    return sync_detailed(
        collectible_item_id=collectible_item_id,
        client=client,
        additional_quantity=additional_quantity,
    ).parsed


async def asyncio_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    additional_quantity: int,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse]:
    """Get the restocking fee for a given collectible item and additional quantity.

    Args:
        collectible_item_id (str):
        additional_quantity (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        additional_quantity=additional_quantity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    additional_quantity: int,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse | None:
    """Get the restocking fee for a given collectible item and additional quantity.

    Args:
        collectible_item_id (str):
        additional_quantity (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse
    """

    return (
        await asyncio_detailed(
            collectible_item_id=collectible_item_id,
            client=client,
            additional_quantity=additional_quantity,
        )
    ).parsed
