from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_develop_models_place_configuration_model_v2 import (
    RobloxApiDevelopModelsPlaceConfigurationModelV2,
)
from ...models.roblox_api_develop_models_place_model_v2 import RobloxApiDevelopModelsPlaceModelV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    *,
    body: RobloxApiDevelopModelsPlaceConfigurationModelV2
    | RobloxApiDevelopModelsPlaceConfigurationModelV2
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://develop.roblox.com/v2/places/{place_id}".format(
            place_id=quote(str(place_id), safe=""),
        ),
    }

    if isinstance(body, RobloxApiDevelopModelsPlaceConfigurationModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiDevelopModelsPlaceConfigurationModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiDevelopModelsPlaceModelV2 | None:
    if response.status_code == 200:
        response_200 = RobloxApiDevelopModelsPlaceModelV2.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiDevelopModelsPlaceModelV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModelV2
    | RobloxApiDevelopModelsPlaceConfigurationModelV2
    | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsPlaceModelV2]:
    """Updates the place configuration for the place with the id placeId

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsPlaceModelV2]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModelV2
    | RobloxApiDevelopModelsPlaceConfigurationModelV2
    | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsPlaceModelV2 | None:
    """Updates the place configuration for the place with the id placeId

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsPlaceModelV2
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModelV2
    | RobloxApiDevelopModelsPlaceConfigurationModelV2
    | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsPlaceModelV2]:
    """Updates the place configuration for the place with the id placeId

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsPlaceModelV2]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModelV2
    | RobloxApiDevelopModelsPlaceConfigurationModelV2
    | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsPlaceModelV2 | None:
    """Updates the place configuration for the place with the id placeId

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModelV2): A model containing information
            about a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsPlaceModelV2
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            body=body,
        )
    ).parsed
