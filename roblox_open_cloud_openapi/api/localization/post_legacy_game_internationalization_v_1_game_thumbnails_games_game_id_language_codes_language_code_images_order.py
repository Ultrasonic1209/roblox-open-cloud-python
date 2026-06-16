from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_sort_image_ids_request import (
    RobloxGameInternationalizationApiSortImageIdsRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    game_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legacy-game-internationalization/v1/game-thumbnails/games/{game_id}/language-codes/{language_code}/images/order".format(
            game_id=quote(str(game_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
    }

    if isinstance(body, RobloxGameInternationalizationApiSortImageIdsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiSortImageIdsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

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


def sync_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
