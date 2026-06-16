from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_api_develop_models_universe_id_permissions_model import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legacy-develop/v1/universes/multiget/permissions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel]:
    """Returns an array of granted and declined permissions related to the universes with the ids in ids
    for the authenticated user.

     If a universe can not be found for a given ID (such as -1) it will be skipped.

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel | None:
    """Returns an array of granted and declined permissions related to the universes with the ids in ids
    for the authenticated user.

     If a universe can not be found for a given ID (such as -1) it will be skipped.

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel]:
    """Returns an array of granted and declined permissions related to the universes with the ids in ids
    for the authenticated user.

     If a universe can not be found for a given ID (such as -1) it will be skipped.

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel | None:
    """Returns an array of granted and declined permissions related to the universes with the ids in ids
    for the authenticated user.

     If a universe can not be found for a given ID (such as -1) it will be skipped.

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseIdPermissionsModel
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
