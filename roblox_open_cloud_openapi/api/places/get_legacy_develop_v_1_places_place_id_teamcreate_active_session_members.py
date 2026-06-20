from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_legacy_develop_v1_places_place_id_teamcreate_active_session_members_limit import (
    GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit,
)
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_users_skinny_user_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    *,
    limit: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit
    | Unset = GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legacy-develop/v1/places/{place_id}/teamcreate/active_session/members".format(
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-team-collaboration:manage"}],
            },
            "openapi-id": "get_legacy-develop_v1_places_placeId_teamcreate_active_session_members",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse.from_dict(
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse]:
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
    limit: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit
    | Unset = GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse]:
    """List of users in the active Team Create session

    Args:
        place_id (int):
        limit (GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit | Unset):
            Default: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit
    | Unset = GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse | None:
    """List of users in the active Team Create session

    Args:
        place_id (int):
        limit (GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit | Unset):
            Default: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit
    | Unset = GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse]:
    """List of users in the active Team Create session

    Args:
        place_id (int):
        limit (GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit | Unset):
            Default: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit
    | Unset = GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse | None:
    """List of users in the active Team Create session

    Args:
        place_id (int):
        limit (GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit | Unset):
            Default: GetLegacyDevelopV1PlacesPlaceIdTeamcreateActiveSessionMembersLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesUsersSkinnyUserResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
