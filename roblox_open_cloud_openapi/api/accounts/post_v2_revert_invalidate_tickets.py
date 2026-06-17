from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v2/revert/invalidate-tickets",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

        return response_200

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Invalidates all account security tickets for the authenticated user.
    This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Invalidates all account security tickets for the authenticated user.
    This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Invalidates all account security tickets for the authenticated user.
    This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Invalidates all account security tickets for the authenticated user.
    This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
