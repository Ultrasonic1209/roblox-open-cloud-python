from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v1_groups_create_body import PostV1GroupsCreateBody
from ...models.roblox_web_responses_groups_group_response_v2 import RobloxWebResponsesGroupsGroupResponseV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1GroupsCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v1/groups/create",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebResponsesGroupsGroupResponseV2 | None:
    if response.status_code == 200:
        response_200 = RobloxWebResponsesGroupsGroupResponseV2.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebResponsesGroupsGroupResponseV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1GroupsCreateBody | Unset = UNSET,
) -> Response[Any | RobloxWebResponsesGroupsGroupResponseV2]:
    r"""Creates a new group.

     This endpoint will charge Robux for the group purchase.
    Accepts \"icon\" and \"coverPhoto\" in Files object. Defaults to first file if \"icon\" is not
    present.
    Http status code 413 is thrown when the group icon file size is too large.

    Args:
        body (PostV1GroupsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebResponsesGroupsGroupResponseV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostV1GroupsCreateBody | Unset = UNSET,
) -> Any | RobloxWebResponsesGroupsGroupResponseV2 | None:
    r"""Creates a new group.

     This endpoint will charge Robux for the group purchase.
    Accepts \"icon\" and \"coverPhoto\" in Files object. Defaults to first file if \"icon\" is not
    present.
    Http status code 413 is thrown when the group icon file size is too large.

    Args:
        body (PostV1GroupsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebResponsesGroupsGroupResponseV2
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1GroupsCreateBody | Unset = UNSET,
) -> Response[Any | RobloxWebResponsesGroupsGroupResponseV2]:
    r"""Creates a new group.

     This endpoint will charge Robux for the group purchase.
    Accepts \"icon\" and \"coverPhoto\" in Files object. Defaults to first file if \"icon\" is not
    present.
    Http status code 413 is thrown when the group icon file size is too large.

    Args:
        body (PostV1GroupsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebResponsesGroupsGroupResponseV2]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1GroupsCreateBody | Unset = UNSET,
) -> Any | RobloxWebResponsesGroupsGroupResponseV2 | None:
    r"""Creates a new group.

     This endpoint will charge Robux for the group purchase.
    Accepts \"icon\" and \"coverPhoto\" in Files object. Defaults to first file if \"icon\" is not
    present.
    Http status code 413 is thrown when the group icon file size is too large.

    Args:
        body (PostV1GroupsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebResponsesGroupsGroupResponseV2
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
