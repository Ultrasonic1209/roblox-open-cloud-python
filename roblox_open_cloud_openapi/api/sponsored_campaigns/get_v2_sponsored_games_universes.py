from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_ad_configuration_api_models_get_recent_ads_ranked_universes_response import (
    RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://adconfiguration.roblox.com/v2/sponsored-games/universes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int | Unset = UNSET,
) -> Response[Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse]:
    """Gets a list of universes for the authenticated user, or the given group, ordered by most recently
    created sponsored game ads.

    Args:
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: int | Unset = UNSET,
) -> Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse | None:
    """Gets a list of universes for the authenticated user, or the given group, ordered by most recently
    created sponsored game ads.

    Args:
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int | Unset = UNSET,
) -> Response[Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse]:
    """Gets a list of universes for the authenticated user, or the given group, ordered by most recently
    created sponsored game ads.

    Args:
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: int | Unset = UNSET,
) -> Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse | None:
    """Gets a list of universes for the authenticated user, or the given group, ordered by most recently
    created sponsored game ads.

    Args:
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdConfigurationApiModelsGetRecentAdsRankedUniversesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
        )
    ).parsed
