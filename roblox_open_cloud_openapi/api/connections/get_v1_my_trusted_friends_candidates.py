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


from ...models.roblox_paging_cursored_paged_result_roblox_friends_api_models_response_trusted_friend_candidate_response import (
    RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/my/trusted-friends/candidates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse]:
    """Get a page of friends that the authenticated user can add as trusted friends. Friends with a pending
    trusted
    friend request from the user come after the other friends. A page can be short or empty and still
    have a
    cursor, so request pages until nextPageCursor is null.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse | None:
    """Get a page of friends that the authenticated user can add as trusted friends. Friends with a pending
    trusted
    friend request from the user come after the other friends. A page can be short or empty and still
    have a
    cursor, so request pages until nextPageCursor is null.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse]:
    """Get a page of friends that the authenticated user can add as trusted friends. Friends with a pending
    trusted
    friend request from the user come after the other friends. A page can be short or empty and still
    have a
    cursor, so request pages until nextPageCursor is null.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse | None:
    """Get a page of friends that the authenticated user can add as trusted friends. Friends with a pending
    trusted
    friend request from the user come after the other friends. A page can be short or empty and still
    have a
    cursor, so request pages until nextPageCursor is null.

    Args:
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseTrustedFriendCandidateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
