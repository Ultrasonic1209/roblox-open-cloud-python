from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_outfits_format import GetV1UsersOutfitsFormat
from ...models.get_v1_users_outfits_size import GetV1UsersOutfitsSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_outfit_ids: list[int],
    size: GetV1UsersOutfitsSize | Unset = GetV1UsersOutfitsSize.VALUE_0,
    format_: GetV1UsersOutfitsFormat | Unset = GetV1UsersOutfitsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_outfit_ids = user_outfit_ids

    params["userOutfitIds"] = json_user_outfit_ids

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
        "url": "https://thumbnails.roblox.com/v1/users/outfits",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_users_outfits",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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
    user_outfit_ids: list[int],
    size: GetV1UsersOutfitsSize | Unset = GetV1UsersOutfitsSize.VALUE_0,
    format_: GetV1UsersOutfitsFormat | Unset = GetV1UsersOutfitsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Get outfits for the given CSV of userOutfitIds

    Args:
        user_outfit_ids (list[int]):
        size (GetV1UsersOutfitsSize | Unset):  Default: GetV1UsersOutfitsSize.VALUE_0.
        format_ (GetV1UsersOutfitsFormat | Unset):  Default: GetV1UsersOutfitsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        user_outfit_ids=user_outfit_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_outfit_ids: list[int],
    size: GetV1UsersOutfitsSize | Unset = GetV1UsersOutfitsSize.VALUE_0,
    format_: GetV1UsersOutfitsFormat | Unset = GetV1UsersOutfitsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Get outfits for the given CSV of userOutfitIds

    Args:
        user_outfit_ids (list[int]):
        size (GetV1UsersOutfitsSize | Unset):  Default: GetV1UsersOutfitsSize.VALUE_0.
        format_ (GetV1UsersOutfitsFormat | Unset):  Default: GetV1UsersOutfitsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        user_outfit_ids=user_outfit_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_outfit_ids: list[int],
    size: GetV1UsersOutfitsSize | Unset = GetV1UsersOutfitsSize.VALUE_0,
    format_: GetV1UsersOutfitsFormat | Unset = GetV1UsersOutfitsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Get outfits for the given CSV of userOutfitIds

    Args:
        user_outfit_ids (list[int]):
        size (GetV1UsersOutfitsSize | Unset):  Default: GetV1UsersOutfitsSize.VALUE_0.
        format_ (GetV1UsersOutfitsFormat | Unset):  Default: GetV1UsersOutfitsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        user_outfit_ids=user_outfit_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_outfit_ids: list[int],
    size: GetV1UsersOutfitsSize | Unset = GetV1UsersOutfitsSize.VALUE_0,
    format_: GetV1UsersOutfitsFormat | Unset = GetV1UsersOutfitsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Get outfits for the given CSV of userOutfitIds

    Args:
        user_outfit_ids (list[int]):
        size (GetV1UsersOutfitsSize | Unset):  Default: GetV1UsersOutfitsSize.VALUE_0.
        format_ (GetV1UsersOutfitsFormat | Unset):  Default: GetV1UsersOutfitsFormat.PNG.
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
            user_outfit_ids=user_outfit_ids,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
