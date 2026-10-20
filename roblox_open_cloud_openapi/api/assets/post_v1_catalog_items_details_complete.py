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
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_catalog_api_batch_item_details_complete_response import (
    RobloxCatalogApiBatchItemDetailsCompleteResponse,
)
from ...models.roblox_catalog_api_multiget_item_details_request_model import (
    RobloxCatalogApiMultigetItemDetailsRequestModel,
)


def _get_kwargs(
    *,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
    roblox_place_id: int,
    roblox_game_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Roblox-Place-Id"] = str(roblox_place_id)

    headers["Roblox-Game-Id"] = roblox_game_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://catalog.roblox.com/v1/catalog/items/details/complete",
    }

    if isinstance(body, RobloxCatalogApiMultigetItemDetailsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxCatalogApiMultigetItemDetailsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxCatalogApiBatchItemDetailsCompleteResponse | None:
    if response.status_code == 200:
        response_200 = RobloxCatalogApiBatchItemDetailsCompleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxCatalogApiBatchItemDetailsCompleteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Response[Any | RobloxCatalogApiBatchItemDetailsCompleteResponse]:
    """Returns list of item details complete with user ownership and economy information.
    Batch version of GetItemDetailsComplete. Items with critical errors are returned in ItemErrors
    with their corresponding HTTP status code (404 for not-found, 500 for other errors).

    Args:
        roblox_place_id (int):
        roblox_game_id (str):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiBatchItemDetailsCompleteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Any | RobloxCatalogApiBatchItemDetailsCompleteResponse | None:
    """Returns list of item details complete with user ownership and economy information.
    Batch version of GetItemDetailsComplete. Items with critical errors are returned in ItemErrors
    with their corresponding HTTP status code (404 for not-found, 500 for other errors).

    Args:
        roblox_place_id (int):
        roblox_game_id (str):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiBatchItemDetailsCompleteResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Response[Any | RobloxCatalogApiBatchItemDetailsCompleteResponse]:
    """Returns list of item details complete with user ownership and economy information.
    Batch version of GetItemDetailsComplete. Items with critical errors are returned in ItemErrors
    with their corresponding HTTP status code (404 for not-found, 500 for other errors).

    Args:
        roblox_place_id (int):
        roblox_game_id (str):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxCatalogApiBatchItemDetailsCompleteResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxCatalogApiMultigetItemDetailsRequestModel
    | RobloxCatalogApiMultigetItemDetailsRequestModel
    | Unset = UNSET,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Any | RobloxCatalogApiBatchItemDetailsCompleteResponse | None:
    """Returns list of item details complete with user ownership and economy information.
    Batch version of GetItemDetailsComplete. Items with critical errors are returned in ItemErrors
    with their corresponding HTTP status code (404 for not-found, 500 for other errors).

    Args:
        roblox_place_id (int):
        roblox_game_id (str):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):
        body (RobloxCatalogApiMultigetItemDetailsRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxCatalogApiBatchItemDetailsCompleteResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
            roblox_game_id=roblox_game_id,
        )
    ).parsed
