from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translation_roles_api_roblox_web_web_api_models_api_array_response_system_string import (
    TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString,
)
from ...types import Response


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://translationroles.roblox.com/v1/game-localization-roles/games/{game_id}/current-user/roles".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString | None:
    if response.status_code == 200:
        response_200 = TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString]:
    """Retrieves the list of roles granted to current logged-in user

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString | None:
    """Retrieves the list of roles granted to current logged-in user

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString]:
    """Retrieves the list of roles granted to current logged-in user

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString | None:
    """Retrieves the list of roles granted to current logged-in user

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
