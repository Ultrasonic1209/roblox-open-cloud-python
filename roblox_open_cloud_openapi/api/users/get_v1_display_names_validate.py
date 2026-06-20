import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    display_name: str,
    birthdate: datetime.datetime,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["displayName"] = display_name

    json_birthdate = birthdate.isoformat()
    params["birthdate"] = json_birthdate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://users.roblox.com/v1/display-names/validate",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_display-names_validate",
        },
    }

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

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
    display_name: str,
    birthdate: datetime.datetime,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Validate a display name for a new user.

    Args:
        display_name (str):
        birthdate (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        display_name=display_name,
        birthdate=birthdate,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birthdate: datetime.datetime,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Validate a display name for a new user.

    Args:
        display_name (str):
        birthdate (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        client=client,
        display_name=display_name,
        birthdate=birthdate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birthdate: datetime.datetime,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Validate a display name for a new user.

    Args:
        display_name (str):
        birthdate (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        display_name=display_name,
        birthdate=birthdate,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birthdate: datetime.datetime,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Validate a display name for a new user.

    Args:
        display_name (str):
        birthdate (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            display_name=display_name,
            birthdate=birthdate,
        )
    ).parsed
