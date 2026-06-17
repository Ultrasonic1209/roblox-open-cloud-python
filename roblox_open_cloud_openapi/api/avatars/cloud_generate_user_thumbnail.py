from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_generate_user_thumbnail_format import CloudGenerateUserThumbnailFormat
from ...models.cloud_generate_user_thumbnail_shape import CloudGenerateUserThumbnailShape
from ...models.operation import Operation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    size: int | Unset = UNSET,
    format_: CloudGenerateUserThumbnailFormat | Unset = UNSET,
    shape: CloudGenerateUserThumbnailShape | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["size"] = size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_shape: str | Unset = UNSET
    if not isinstance(shape, Unset):
        json_shape = shape.value

    params["shape"] = json_shape

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}:generateThumbnail".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Operation | None:
    if response.status_code == 200:
        response_200 = Operation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Operation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    size: int | Unset = UNSET,
    format_: CloudGenerateUserThumbnailFormat | Unset = UNSET,
    shape: CloudGenerateUserThumbnailShape | Unset = UNSET,
) -> Response[Operation]:
    """Generate User Thumbnail

     Generates and returns the URL for the user's avatar thumbnail.

    Args:
        user_id (str):
        size (int | Unset):
        format_ (CloudGenerateUserThumbnailFormat | Unset):  Example: FORMAT_UNSPECIFIED.
        shape (CloudGenerateUserThumbnailShape | Unset):  Example: SHAPE_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        size=size,
        format_=format_,
        shape=shape,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    size: int | Unset = UNSET,
    format_: CloudGenerateUserThumbnailFormat | Unset = UNSET,
    shape: CloudGenerateUserThumbnailShape | Unset = UNSET,
) -> Operation | None:
    """Generate User Thumbnail

     Generates and returns the URL for the user's avatar thumbnail.

    Args:
        user_id (str):
        size (int | Unset):
        format_ (CloudGenerateUserThumbnailFormat | Unset):  Example: FORMAT_UNSPECIFIED.
        shape (CloudGenerateUserThumbnailShape | Unset):  Example: SHAPE_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        size=size,
        format_=format_,
        shape=shape,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    size: int | Unset = UNSET,
    format_: CloudGenerateUserThumbnailFormat | Unset = UNSET,
    shape: CloudGenerateUserThumbnailShape | Unset = UNSET,
) -> Response[Operation]:
    """Generate User Thumbnail

     Generates and returns the URL for the user's avatar thumbnail.

    Args:
        user_id (str):
        size (int | Unset):
        format_ (CloudGenerateUserThumbnailFormat | Unset):  Example: FORMAT_UNSPECIFIED.
        shape (CloudGenerateUserThumbnailShape | Unset):  Example: SHAPE_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        size=size,
        format_=format_,
        shape=shape,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    size: int | Unset = UNSET,
    format_: CloudGenerateUserThumbnailFormat | Unset = UNSET,
    shape: CloudGenerateUserThumbnailShape | Unset = UNSET,
) -> Operation | None:
    """Generate User Thumbnail

     Generates and returns the URL for the user's avatar thumbnail.

    Args:
        user_id (str):
        size (int | Unset):
        format_ (CloudGenerateUserThumbnailFormat | Unset):  Example: FORMAT_UNSPECIFIED.
        shape (CloudGenerateUserThumbnailShape | Unset):  Example: SHAPE_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            size=size,
            format_=format_,
            shape=shape,
        )
    ).parsed
