from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_game_passes_format import GetV1GamePassesFormat
from ...models.get_v1_game_passes_size import GetV1GamePassesSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    game_pass_ids: list[int],
    size: GetV1GamePassesSize | Unset = GetV1GamePassesSize.VALUE_0,
    format_: GetV1GamePassesFormat | Unset = GetV1GamePassesFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_game_pass_ids = game_pass_ids

    params["gamePassIds"] = json_game_pass_ids

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
        "url": "/v1/game-passes",
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
    *,
    client: AuthenticatedClient,
    game_pass_ids: list[int],
    size: GetV1GamePassesSize | Unset = GetV1GamePassesSize.VALUE_0,
    format_: GetV1GamePassesFormat | Unset = GetV1GamePassesFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails game pass icons.

    Args:
        game_pass_ids (list[int]):
        size (GetV1GamePassesSize | Unset):  Default: GetV1GamePassesSize.VALUE_0.
        format_ (GetV1GamePassesFormat | Unset):  Default: GetV1GamePassesFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        game_pass_ids=game_pass_ids,
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
    game_pass_ids: list[int],
    size: GetV1GamePassesSize | Unset = GetV1GamePassesSize.VALUE_0,
    format_: GetV1GamePassesFormat | Unset = GetV1GamePassesFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails game pass icons.

    Args:
        game_pass_ids (list[int]):
        size (GetV1GamePassesSize | Unset):  Default: GetV1GamePassesSize.VALUE_0.
        format_ (GetV1GamePassesFormat | Unset):  Default: GetV1GamePassesFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        game_pass_ids=game_pass_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    game_pass_ids: list[int],
    size: GetV1GamePassesSize | Unset = GetV1GamePassesSize.VALUE_0,
    format_: GetV1GamePassesFormat | Unset = GetV1GamePassesFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails game pass icons.

    Args:
        game_pass_ids (list[int]):
        size (GetV1GamePassesSize | Unset):  Default: GetV1GamePassesSize.VALUE_0.
        format_ (GetV1GamePassesFormat | Unset):  Default: GetV1GamePassesFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        game_pass_ids=game_pass_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    game_pass_ids: list[int],
    size: GetV1GamePassesSize | Unset = GetV1GamePassesSize.VALUE_0,
    format_: GetV1GamePassesFormat | Unset = GetV1GamePassesFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails game pass icons.

    Args:
        game_pass_ids (list[int]):
        size (GetV1GamePassesSize | Unset):  Default: GetV1GamePassesSize.VALUE_0.
        format_ (GetV1GamePassesFormat | Unset):  Default: GetV1GamePassesFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            game_pass_ids=game_pass_ids,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
