from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_update_group_name_request import RobloxGroupsApiUpdateGroupNameRequest
from ...models.roblox_groups_api_update_group_name_response import RobloxGroupsApiUpdateGroupNameResponse
from ...types import UNSET, Response


def _get_kwargs(
    group_id: int,
    *,
    body: RobloxGroupsApiUpdateGroupNameRequest | RobloxGroupsApiUpdateGroupNameRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/groups/{group_id}/name".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    if isinstance(body, RobloxGroupsApiUpdateGroupNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiUpdateGroupNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiUpdateGroupNameResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiUpdateGroupNameResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGroupsApiUpdateGroupNameResponse]:
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
    body: RobloxGroupsApiUpdateGroupNameRequest | RobloxGroupsApiUpdateGroupNameRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiUpdateGroupNameResponse]:
    """Updates the group's name.

     This endpoint will charge Robux for the group rename.

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiUpdateGroupNameResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupNameRequest | RobloxGroupsApiUpdateGroupNameRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiUpdateGroupNameResponse | None:
    """Updates the group's name.

     This endpoint will charge Robux for the group rename.

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiUpdateGroupNameResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupNameRequest | RobloxGroupsApiUpdateGroupNameRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiUpdateGroupNameResponse]:
    """Updates the group's name.

     This endpoint will charge Robux for the group rename.

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiUpdateGroupNameResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupNameRequest | RobloxGroupsApiUpdateGroupNameRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiUpdateGroupNameResponse | None:
    """Updates the group's name.

     This endpoint will charge Robux for the group rename.

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group
        body (RobloxGroupsApiUpdateGroupNameRequest): A request model for setting a name for the
            group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiUpdateGroupNameResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
