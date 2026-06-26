from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_avatar_format import GetV1UsersAvatarFormat
from ...models.get_v1_users_avatar_size import GetV1UsersAvatarSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_ids: list[int],
    include_background: bool | Unset = False,
    size: GetV1UsersAvatarSize | Unset = GetV1UsersAvatarSize.VALUE_0,
    format_: GetV1UsersAvatarFormat | Unset = GetV1UsersAvatarFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params["includeBackground"] = include_background

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
        "url": "https://thumbnails.roblox.com/v1/users/avatar",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_users_avatar",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
    include_background: bool | Unset = False,
    size: GetV1UsersAvatarSize | Unset = GetV1UsersAvatarSize.VALUE_0,
    format_: GetV1UsersAvatarFormat | Unset = GetV1UsersAvatarFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any]:
    """Get Avatar Full body shots for the given CSV of userIds

    Args:
        user_ids (list[int]):
        include_background (bool | Unset):  Default: False.
        size (GetV1UsersAvatarSize | Unset):  Default: GetV1UsersAvatarSize.VALUE_0.
        format_ (GetV1UsersAvatarFormat | Unset):  Default: GetV1UsersAvatarFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_ids=user_ids,
        include_background=include_background,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
    include_background: bool | Unset = False,
    size: GetV1UsersAvatarSize | Unset = GetV1UsersAvatarSize.VALUE_0,
    format_: GetV1UsersAvatarFormat | Unset = GetV1UsersAvatarFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any]:
    """Get Avatar Full body shots for the given CSV of userIds

    Args:
        user_ids (list[int]):
        include_background (bool | Unset):  Default: False.
        size (GetV1UsersAvatarSize | Unset):  Default: GetV1UsersAvatarSize.VALUE_0.
        format_ (GetV1UsersAvatarFormat | Unset):  Default: GetV1UsersAvatarFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_ids=user_ids,
        include_background=include_background,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
