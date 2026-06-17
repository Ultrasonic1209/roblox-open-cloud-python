import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_inventory_api_models_can_view_inventory_response import (
    RobloxInventoryApiModelsCanViewInventoryResponse,
)


def _get_kwargs(
    user_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://inventory.roblox.com/v1/users/{user_id}/can-view-inventory".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxInventoryApiModelsCanViewInventoryResponse | None:
    if response.status_code == 200:
        response_200 = RobloxInventoryApiModelsCanViewInventoryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxInventoryApiModelsCanViewInventoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#inventory_get_v1_users__userId__can_view_inventory"
)
def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxInventoryApiModelsCanViewInventoryResponse]:
    """Gets whether the specified user's inventory can be viewed.

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxInventoryApiModelsCanViewInventoryResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#inventory_get_v1_users__userId__can_view_inventory"
)
def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxInventoryApiModelsCanViewInventoryResponse | None:
    """Gets whether the specified user's inventory can be viewed.

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxInventoryApiModelsCanViewInventoryResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#inventory_get_v1_users__userId__can_view_inventory"
)
async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxInventoryApiModelsCanViewInventoryResponse]:
    """Gets whether the specified user's inventory can be viewed.

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxInventoryApiModelsCanViewInventoryResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#inventory_get_v1_users__userId__can_view_inventory"
)
async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxInventoryApiModelsCanViewInventoryResponse | None:
    """Gets whether the specified user's inventory can be viewed.

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxInventoryApiModelsCanViewInventoryResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
