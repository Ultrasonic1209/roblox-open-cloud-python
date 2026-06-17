from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_develop_models_team_create_membership_request import (
    RobloxApiDevelopModelsTeamCreateMembershipRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: RobloxApiDevelopModelsTeamCreateMembershipRequest
    | RobloxApiDevelopModelsTeamCreateMembershipRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/legacy-develop/v1/universes/{universe_id}/teamcreate/memberships".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, RobloxApiDevelopModelsTeamCreateMembershipRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiDevelopModelsTeamCreateMembershipRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
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
    body: RobloxApiDevelopModelsTeamCreateMembershipRequest
    | RobloxApiDevelopModelsTeamCreateMembershipRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Removes a user from a TeamCreate permissions list.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
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
    body: RobloxApiDevelopModelsTeamCreateMembershipRequest
    | RobloxApiDevelopModelsTeamCreateMembershipRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Removes a user from a TeamCreate permissions list.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
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
    body: RobloxApiDevelopModelsTeamCreateMembershipRequest
    | RobloxApiDevelopModelsTeamCreateMembershipRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Removes a user from a TeamCreate permissions list.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
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
    body: RobloxApiDevelopModelsTeamCreateMembershipRequest
    | RobloxApiDevelopModelsTeamCreateMembershipRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Removes a user from a TeamCreate permissions list.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership
        body (RobloxApiDevelopModelsTeamCreateMembershipRequest): Request model for a TeamCreate
            membership

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
