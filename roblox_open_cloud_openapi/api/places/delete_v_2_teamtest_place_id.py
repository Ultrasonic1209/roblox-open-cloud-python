import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from uuid import UUID

from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    place_id: int,
    *,
    game_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_game_id = str(game_id)
    params["gameId"] = json_game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/teamtest/{place_id}".format(
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_delete_v2_teamtest__placeId_"
)
def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    game_id: UUID,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Close a game instance that is being used for team testing

    Args:
        place_id (int):
        game_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_delete_v2_teamtest__placeId_"
)
def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    game_id: UUID,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Close a game instance that is being used for team testing

    Args:
        place_id (int):
        game_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        game_id=game_id,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_delete_v2_teamtest__placeId_"
)
async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    game_id: UUID,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Close a game instance that is being used for team testing

    Args:
        place_id (int):
        game_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_delete_v2_teamtest__placeId_"
)
async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    game_id: UUID,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Close a game instance that is being used for team testing

    Args:
        place_id (int):
        game_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            game_id=game_id,
        )
    ).parsed
