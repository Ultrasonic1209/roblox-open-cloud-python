from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}, 'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/games/{gameId}/autolocalizationtable', 'httpMethod': 'POST', 'documentationUrl': 'https://create.roblox.com/docs/cloud/reference/features/localization#post_legacy_localization_tables_v1_autolocalization_games__gameId__autolocalizationtable'}]}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_localization_tables_api_game_autolocalization_information_response import (
    RobloxLocalizationTablesApiGameAutolocalizationInformationResponse,
)


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://localizationtables.roblox.com/v1/autolocalization/games/{game_id}/autolocalizationtable#localizationtables.roblox.com".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGameAutolocalizationInformationResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
