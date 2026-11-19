from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

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


from ...models.roblox_item_configuration_api_models_response_get_items_by_token_response import (
    RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    token_id: str,
    limit: int,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["tokenId"] = token_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/items/by-token",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token_id: str,
    limit: int,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse]:
    """Gets the marketplace items for a token (i.e. an IEC avatar creation token).

    Args:
        token_id (str):
        limit (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    token_id: str,
    limit: int,
    cursor: str | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse | None:
    """Gets the marketplace items for a token (i.e. an IEC avatar creation token).

    Args:
        token_id (str):
        limit (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse
    """

    return sync_detailed(
        client=client,
        token_id=token_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token_id: str,
    limit: int,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse]:
    """Gets the marketplace items for a token (i.e. an IEC avatar creation token).

    Args:
        token_id (str):
        limit (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    token_id: str,
    limit: int,
    cursor: str | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse | None:
    """Gets the marketplace items for a token (i.e. an IEC avatar creation token).

    Args:
        token_id (str):
        limit (int):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseGetItemsByTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            token_id=token_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
