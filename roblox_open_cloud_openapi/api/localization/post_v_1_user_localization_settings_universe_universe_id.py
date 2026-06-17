from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_models_request_set_user_localization_settings_request import (
    RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest,
)
from ...models.roblox_game_internationalization_api_models_response_set_user_localization_settings_response import (
    RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://gameinternationalization.roblox.com/v1/user-localization-settings/universe/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse.from_dict(
            response.json()
        )

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse]:
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
    body: RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse]:
    """Set user localization settings for universe.

    Args:
        universe_id (int):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse | None:
    """Set user localization settings for universe.

    Args:
        universe_id (int):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse]:
    """Set user localization settings for universe.

    Args:
        universe_id (int):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse | None:
    """Set user localization settings for universe.

    Args:
        universe_id (int):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):
        body (RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiModelsResponseSetUserLocalizationSettingsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
