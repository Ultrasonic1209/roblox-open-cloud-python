from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_games_multiget_thumbnails_format import GetV1GamesMultigetThumbnailsFormat
from ...models.get_v1_games_multiget_thumbnails_size import GetV1GamesMultigetThumbnailsSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_thumbnails_api_models_universe_thumbnails_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_ids: list[int],
    count_per_universe: int | Unset = 1,
    defaults: bool | Unset = True,
    size: GetV1GamesMultigetThumbnailsSize | Unset = GetV1GamesMultigetThumbnailsSize.VALUE_0,
    format_: GetV1GamesMultigetThumbnailsFormat | Unset = GetV1GamesMultigetThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    params["countPerUniverse"] = count_per_universe

    params["defaults"] = defaults

    json_size: str | Unset = UNSET
    if not isinstance(size, Unset):
        json_size = size.value

    params["size"] = json_size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["isCircular"] = is_circular

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/games/multiget/thumbnails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    count_per_universe: int | Unset = 1,
    defaults: bool | Unset = True,
    size: GetV1GamesMultigetThumbnailsSize | Unset = GetV1GamesMultigetThumbnailsSize.VALUE_0,
    format_: GetV1GamesMultigetThumbnailsFormat | Unset = GetV1GamesMultigetThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse]:
    """Fetch game thumbnail URLs for a list of universe IDs.

    Args:
        universe_ids (list[int]):
        count_per_universe (int | Unset):  Default: 1.
        defaults (bool | Unset):  Default: True.
        size (GetV1GamesMultigetThumbnailsSize | Unset):  Default:
            GetV1GamesMultigetThumbnailsSize.VALUE_0.
        format_ (GetV1GamesMultigetThumbnailsFormat | Unset):  Default:
            GetV1GamesMultigetThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        count_per_universe=count_per_universe,
        defaults=defaults,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    count_per_universe: int | Unset = 1,
    defaults: bool | Unset = True,
    size: GetV1GamesMultigetThumbnailsSize | Unset = GetV1GamesMultigetThumbnailsSize.VALUE_0,
    format_: GetV1GamesMultigetThumbnailsFormat | Unset = GetV1GamesMultigetThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse | None:
    """Fetch game thumbnail URLs for a list of universe IDs.

    Args:
        universe_ids (list[int]):
        count_per_universe (int | Unset):  Default: 1.
        defaults (bool | Unset):  Default: True.
        size (GetV1GamesMultigetThumbnailsSize | Unset):  Default:
            GetV1GamesMultigetThumbnailsSize.VALUE_0.
        format_ (GetV1GamesMultigetThumbnailsFormat | Unset):  Default:
            GetV1GamesMultigetThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
        count_per_universe=count_per_universe,
        defaults=defaults,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    count_per_universe: int | Unset = 1,
    defaults: bool | Unset = True,
    size: GetV1GamesMultigetThumbnailsSize | Unset = GetV1GamesMultigetThumbnailsSize.VALUE_0,
    format_: GetV1GamesMultigetThumbnailsFormat | Unset = GetV1GamesMultigetThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse]:
    """Fetch game thumbnail URLs for a list of universe IDs.

    Args:
        universe_ids (list[int]):
        count_per_universe (int | Unset):  Default: 1.
        defaults (bool | Unset):  Default: True.
        size (GetV1GamesMultigetThumbnailsSize | Unset):  Default:
            GetV1GamesMultigetThumbnailsSize.VALUE_0.
        format_ (GetV1GamesMultigetThumbnailsFormat | Unset):  Default:
            GetV1GamesMultigetThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        count_per_universe=count_per_universe,
        defaults=defaults,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    count_per_universe: int | Unset = 1,
    defaults: bool | Unset = True,
    size: GetV1GamesMultigetThumbnailsSize | Unset = GetV1GamesMultigetThumbnailsSize.VALUE_0,
    format_: GetV1GamesMultigetThumbnailsFormat | Unset = GetV1GamesMultigetThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse | None:
    """Fetch game thumbnail URLs for a list of universe IDs.

    Args:
        universe_ids (list[int]):
        count_per_universe (int | Unset):  Default: 1.
        defaults (bool | Unset):  Default: True.
        size (GetV1GamesMultigetThumbnailsSize | Unset):  Default:
            GetV1GamesMultigetThumbnailsSize.VALUE_0.
        format_ (GetV1GamesMultigetThumbnailsFormat | Unset):  Default:
            GetV1GamesMultigetThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxThumbnailsApiModelsUniverseThumbnailsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
            count_per_universe=count_per_universe,
            defaults=defaults,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
