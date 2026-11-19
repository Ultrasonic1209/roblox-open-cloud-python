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
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_response_collectibles_restock_eligibility_response import (
    RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse,
)


def _get_kwargs(
    collectible_item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/{collectible_item_id}/restock-eligibility".format(
            collectible_item_id=quote(str(collectible_item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse.from_dict(
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
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse]:
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
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse]:
    """Returns structured restock eligibility information for a given collectible item.
    This is the single source of truth the frontend should use to determine whether
    restocking is available, instead of re-deriving from individual flags.

    Args:
        collectible_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse | None:
    """Returns structured restock eligibility information for a given collectible item.
    This is the single source of truth the frontend should use to determine whether
    restocking is available, instead of re-deriving from individual flags.

    Args:
        collectible_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse
    """

    return sync_detailed(
        collectible_item_id=collectible_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse]:
    """Returns structured restock eligibility information for a given collectible item.
    This is the single source of truth the frontend should use to determine whether
    restocking is available, instead of re-deriving from individual flags.

    Args:
        collectible_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse | None:
    """Returns structured restock eligibility information for a given collectible item.
    This is the single source of truth the frontend should use to determine whether
    restocking is available, instead of re-deriving from individual flags.

    Args:
        collectible_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse
    """

    return (
        await asyncio_detailed(
            collectible_item_id=collectible_item_id,
            client=client,
        )
    ).parsed
