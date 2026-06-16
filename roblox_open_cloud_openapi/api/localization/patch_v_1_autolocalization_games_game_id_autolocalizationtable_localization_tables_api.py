from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_set_autolocalization_table_for_game_request import (
    RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/autolocalization/games/{game_id}/autolocalizationtable#LocalizationTablesApi".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    if isinstance(body, RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """
    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """
    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """
    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """
    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):
        body (RobloxLocalizationTablesApiSetAutolocalizationTableForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
