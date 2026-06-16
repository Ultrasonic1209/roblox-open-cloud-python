from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_games_universe_id_thumbnails_format import GetV1GamesUniverseIdThumbnailsFormat
from ...models.get_v1_games_universe_id_thumbnails_size import GetV1GamesUniverseIdThumbnailsSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    thumbnail_ids: list[int],
    size: GetV1GamesUniverseIdThumbnailsSize | Unset = GetV1GamesUniverseIdThumbnailsSize.VALUE_0,
    format_: GetV1GamesUniverseIdThumbnailsFormat | Unset = GetV1GamesUniverseIdThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_thumbnail_ids = thumbnail_ids

    params["thumbnailIds"] = json_thumbnail_ids

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
        "url": "/v1/games/{universe_id}/thumbnails".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    thumbnail_ids: list[int],
    size: GetV1GamesUniverseIdThumbnailsSize | Unset = GetV1GamesUniverseIdThumbnailsSize.VALUE_0,
    format_: GetV1GamesUniverseIdThumbnailsFormat | Unset = GetV1GamesUniverseIdThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Fetches game thumbnail URLs for a list of universes' thumbnail ids. Ids that do not correspond to a
    valid thumbnail will be filtered out.

    Args:
        universe_id (int):
        thumbnail_ids (list[int]):
        size (GetV1GamesUniverseIdThumbnailsSize | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsSize.VALUE_0.
        format_ (GetV1GamesUniverseIdThumbnailsFormat | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        thumbnail_ids=thumbnail_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    thumbnail_ids: list[int],
    size: GetV1GamesUniverseIdThumbnailsSize | Unset = GetV1GamesUniverseIdThumbnailsSize.VALUE_0,
    format_: GetV1GamesUniverseIdThumbnailsFormat | Unset = GetV1GamesUniverseIdThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Fetches game thumbnail URLs for a list of universes' thumbnail ids. Ids that do not correspond to a
    valid thumbnail will be filtered out.

    Args:
        universe_id (int):
        thumbnail_ids (list[int]):
        size (GetV1GamesUniverseIdThumbnailsSize | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsSize.VALUE_0.
        format_ (GetV1GamesUniverseIdThumbnailsFormat | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        thumbnail_ids=thumbnail_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    thumbnail_ids: list[int],
    size: GetV1GamesUniverseIdThumbnailsSize | Unset = GetV1GamesUniverseIdThumbnailsSize.VALUE_0,
    format_: GetV1GamesUniverseIdThumbnailsFormat | Unset = GetV1GamesUniverseIdThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Fetches game thumbnail URLs for a list of universes' thumbnail ids. Ids that do not correspond to a
    valid thumbnail will be filtered out.

    Args:
        universe_id (int):
        thumbnail_ids (list[int]):
        size (GetV1GamesUniverseIdThumbnailsSize | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsSize.VALUE_0.
        format_ (GetV1GamesUniverseIdThumbnailsFormat | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        thumbnail_ids=thumbnail_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    thumbnail_ids: list[int],
    size: GetV1GamesUniverseIdThumbnailsSize | Unset = GetV1GamesUniverseIdThumbnailsSize.VALUE_0,
    format_: GetV1GamesUniverseIdThumbnailsFormat | Unset = GetV1GamesUniverseIdThumbnailsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Fetches game thumbnail URLs for a list of universes' thumbnail ids. Ids that do not correspond to a
    valid thumbnail will be filtered out.

    Args:
        universe_id (int):
        thumbnail_ids (list[int]):
        size (GetV1GamesUniverseIdThumbnailsSize | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsSize.VALUE_0.
        format_ (GetV1GamesUniverseIdThumbnailsFormat | Unset):  Default:
            GetV1GamesUniverseIdThumbnailsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            thumbnail_ids=thumbnail_ids,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
