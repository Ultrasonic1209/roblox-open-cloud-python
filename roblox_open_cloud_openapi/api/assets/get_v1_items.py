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


from ...models.get_v1_items_item_type import GetV1ItemsItemType
from ...models.roblox_item_configuration_api_get_item_response import RobloxItemConfigurationApiGetItemResponse


def _get_kwargs(
    *,
    item_type: GetV1ItemsItemType,
    item_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_item_type = item_type.value
    params["itemType"] = json_item_type

    params["itemId"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiGetItemResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiGetItemResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | RobloxItemConfigurationApiGetItemResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    item_type: GetV1ItemsItemType,
    item_id: str,
) -> Response[Any | RobloxItemConfigurationApiGetItemResponse]:
    """Get an item by its id.

    Args:
        item_type (GetV1ItemsItemType):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetItemResponse]
    """

    kwargs = _get_kwargs(
        item_type=item_type,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_type: GetV1ItemsItemType,
    item_id: str,
) -> Any | RobloxItemConfigurationApiGetItemResponse | None:
    """Get an item by its id.

    Args:
        item_type (GetV1ItemsItemType):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetItemResponse
    """

    return sync_detailed(
        client=client,
        item_type=item_type,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_type: GetV1ItemsItemType,
    item_id: str,
) -> Response[Any | RobloxItemConfigurationApiGetItemResponse]:
    """Get an item by its id.

    Args:
        item_type (GetV1ItemsItemType):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetItemResponse]
    """

    kwargs = _get_kwargs(
        item_type=item_type,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_type: GetV1ItemsItemType,
    item_id: str,
) -> Any | RobloxItemConfigurationApiGetItemResponse | None:
    """Get an item by its id.

    Args:
        item_type (GetV1ItemsItemType):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetItemResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            item_type=item_type,
            item_id=item_id,
        )
    ).parsed
