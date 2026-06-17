from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_friends_api_following_exists_request_model import RobloxFriendsApiFollowingExistsRequestModel
from ...models.roblox_friends_api_models_response_following_exists_response_model import (
    RobloxFriendsApiModelsResponseFollowingExistsResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxFriendsApiFollowingExistsRequestModel | RobloxFriendsApiFollowingExistsRequestModel | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://friends.roblox.com/v1/user/following-exists",
    }

    if isinstance(body, RobloxFriendsApiFollowingExistsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxFriendsApiFollowingExistsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxFriendsApiModelsResponseFollowingExistsResponseModel.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxFriendsApiFollowingExistsRequestModel | RobloxFriendsApiFollowingExistsRequestModel | Unset = UNSET,
) -> Response[Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel]:
    """Returns whether or not the current user is following each userId in a list of userIds

    Args:
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel]
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
    body: RobloxFriendsApiFollowingExistsRequestModel | RobloxFriendsApiFollowingExistsRequestModel | Unset = UNSET,
) -> Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel | None:
    """Returns whether or not the current user is following each userId in a list of userIds

    Args:
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxFriendsApiFollowingExistsRequestModel | RobloxFriendsApiFollowingExistsRequestModel | Unset = UNSET,
) -> Response[Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel]:
    """Returns whether or not the current user is following each userId in a list of userIds

    Args:
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxFriendsApiFollowingExistsRequestModel | RobloxFriendsApiFollowingExistsRequestModel | Unset = UNSET,
) -> Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel | None:
    """Returns whether or not the current user is following each userId in a list of userIds

    Args:
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint
        body (RobloxFriendsApiFollowingExistsRequestModel): Request model for FollowingExists
            endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiModelsResponseFollowingExistsResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
