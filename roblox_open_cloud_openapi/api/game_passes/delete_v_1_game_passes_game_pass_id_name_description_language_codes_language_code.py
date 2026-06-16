from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import Response


def _get_kwargs(
    game_pass_id: int,
    language_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/game-passes/{game_pass_id}/name-description/language-codes/{language_code}".format(
            game_pass_id=quote(str(game_pass_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_pass_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Delete localized name and description of a game pass

    Args:
        game_pass_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_pass_id=game_pass_id,
        language_code=language_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_pass_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Delete localized name and description of a game pass

    Args:
        game_pass_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_pass_id=game_pass_id,
        language_code=language_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_pass_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Delete localized name and description of a game pass

    Args:
        game_pass_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_pass_id=game_pass_id,
        language_code=language_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_pass_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Delete localized name and description of a game pass

    Args:
        game_pass_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_pass_id=game_pass_id,
            language_code=language_code,
            client=client,
        )
    ).parsed
