from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_develop_models_universe_model import RobloxApiDevelopModelsUniverseModel
from ...types import Response


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://develop.roblox.com/v1/universes/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiDevelopModelsUniverseModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiDevelopModelsUniverseModel.from_dict(response.json())

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
) -> Response[Any | RobloxApiDevelopModelsUniverseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxApiDevelopModelsUniverseModel]:
    """Gets a Roblox.Api.Develop.Models.UniverseModel.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsUniverseModel]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxApiDevelopModelsUniverseModel | None:
    """Gets a Roblox.Api.Develop.Models.UniverseModel.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsUniverseModel
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxApiDevelopModelsUniverseModel]:
    """Gets a Roblox.Api.Develop.Models.UniverseModel.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsUniverseModel]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxApiDevelopModelsUniverseModel | None:
    """Gets a Roblox.Api.Develop.Models.UniverseModel.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsUniverseModel
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
