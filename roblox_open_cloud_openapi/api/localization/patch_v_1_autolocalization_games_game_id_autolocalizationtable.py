import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_game_internationalization_api_set_autolocalization_table_for_game_request import (
    RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/autolocalization/games/{game_id}/autolocalizationtable".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    if isinstance(body, RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationTableForGameRequest):

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
