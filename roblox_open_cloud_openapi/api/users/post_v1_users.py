from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_users_api_multi_get_by_user_id_request import RobloxUsersApiMultiGetByUserIdRequest
from ...models.roblox_web_web_api_models_api_array_response_roblox_users_api_multi_get_user_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxUsersApiMultiGetByUserIdRequest | RobloxUsersApiMultiGetByUserIdRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://users.roblox.com/v1/users",
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_users",
        },
    }

    if isinstance(body, RobloxUsersApiMultiGetByUserIdRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxUsersApiMultiGetByUserIdRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxUsersApiMultiGetByUserIdRequest | RobloxUsersApiMultiGetByUserIdRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse]:
    """Get users by ids.

     Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to
    avoid URI limits.

    Args:
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse]
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
    body: RobloxUsersApiMultiGetByUserIdRequest | RobloxUsersApiMultiGetByUserIdRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse | None:
    """Get users by ids.

     Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to
    avoid URI limits.

    Args:
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxUsersApiMultiGetByUserIdRequest | RobloxUsersApiMultiGetByUserIdRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse]:
    """Get users by ids.

     Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to
    avoid URI limits.

    Args:
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxUsersApiMultiGetByUserIdRequest | RobloxUsersApiMultiGetByUserIdRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse | None:
    """Get users by ids.

     Does not require X-CSRF-Token protection because this is essentially a get request but as a POST to
    avoid URI limits.

    Args:
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.
        body (RobloxUsersApiMultiGetByUserIdRequest): Request model for getting users by ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxUsersApiMultiGetUserResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
