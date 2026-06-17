from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_join_group_request import RobloxGroupsApiJoinGroupRequest
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: RobloxGroupsApiJoinGroupRequest | RobloxGroupsApiJoinGroupRequest | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    roblox_game_id: str | Unset = UNSET,
    roblox_session_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    if not isinstance(roblox_game_id, Unset):
        headers["Roblox-Game-Id"] = roblox_game_id

    if not isinstance(roblox_session_id, Unset):
        headers["Roblox-Session-Id"] = roblox_session_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/users".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_groups_groupId_users",
    }

    if isinstance(body, RobloxGroupsApiJoinGroupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiJoinGroupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiJoinGroupRequest | RobloxGroupsApiJoinGroupRequest | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    roblox_game_id: str | Unset = UNSET,
    roblox_session_id: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Joins a group

    Args:
        group_id (int):
        roblox_place_id (int | Unset):
        roblox_game_id (str | Unset):
        roblox_session_id (str | Unset):
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
        roblox_session_id=roblox_session_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiJoinGroupRequest | RobloxGroupsApiJoinGroupRequest | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    roblox_game_id: str | Unset = UNSET,
    roblox_session_id: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Joins a group

    Args:
        group_id (int):
        roblox_place_id (int | Unset):
        roblox_game_id (str | Unset):
        roblox_session_id (str | Unset):
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
        roblox_session_id=roblox_session_id,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiJoinGroupRequest | RobloxGroupsApiJoinGroupRequest | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    roblox_game_id: str | Unset = UNSET,
    roblox_session_id: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Joins a group

    Args:
        group_id (int):
        roblox_place_id (int | Unset):
        roblox_game_id (str | Unset):
        roblox_session_id (str | Unset):
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
        roblox_session_id=roblox_session_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiJoinGroupRequest | RobloxGroupsApiJoinGroupRequest | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    roblox_game_id: str | Unset = UNSET,
    roblox_session_id: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Joins a group

    Args:
        group_id (int):
        roblox_place_id (int | Unset):
        roblox_game_id (str | Unset):
        roblox_session_id (str | Unset):
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.
        body (RobloxGroupsApiJoinGroupRequest): A request model for joining group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
            roblox_game_id=roblox_game_id,
            roblox_session_id=roblox_session_id,
        )
    ).parsed
