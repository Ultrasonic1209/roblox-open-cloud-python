from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    place_id: int,
    *,
    version_type: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_version_type: None | str | Unset
    if isinstance(version_type, Unset):
        json_version_type = UNSET
    else:
        json_version_type = version_type
    params["versionType"] = json_version_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/universes/v1/{universe_id}/places/{place_id}/versions".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation-name": "Publish a Place",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "universe-places:write"}],
                "x-roblox-cloud-api-operation": True,
                "x-roblox-code-samples": [
                    {
                        "language": "curl",
                        "script": "curl --location --request POST 'https://apis.roblox.com/universes/v1/{universeId}/places/{placeId}/versions?versionType=Published' \n--header 'x-api-key: abc...' \n--header 'Content-Type: application/xml' \n--data-raw '<roblox></roblox>'\n",
                    }
                ],
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 30}},
                "x-roblox-throttling-limit": {"perApiKey": {"periodInSeconds": "60", "maxInPeriod": 30}},
                "x-roblox-size-limit": 10485760,
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "Places_CreatePlaceVersionApiKey",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | str | None:
    if response.status_code == 200:
        response_200 = response.text
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    version_type: None | str | Unset = UNSET,
) -> Response[Any | str]:
    """Publish a new place or update an existing place with a new version. Provide a RBXL or RBXLX file in
    the data-binary.

    Args:
        universe_id (int):
        place_id (int):
        version_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_type=version_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    version_type: None | str | Unset = UNSET,
) -> Any | str | None:
    """Publish a new place or update an existing place with a new version. Provide a RBXL or RBXLX file in
    the data-binary.

    Args:
        universe_id (int):
        place_id (int):
        version_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        client=client,
        version_type=version_type,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    version_type: None | str | Unset = UNSET,
) -> Response[Any | str]:
    """Publish a new place or update an existing place with a new version. Provide a RBXL or RBXLX file in
    the data-binary.

    Args:
        universe_id (int):
        place_id (int):
        version_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_type=version_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    version_type: None | str | Unset = UNSET,
) -> Any | str | None:
    """Publish a new place or update an existing place with a new version. Provide a RBXL or RBXLX file in
    the data-binary.

    Args:
        universe_id (int):
        place_id (int):
        version_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            client=client,
            version_type=version_type,
        )
    ).parsed
