from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_empty_response_model import ApiEmptyResponseModel
from ...models.user_game_vote_request import UserGameVoteRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://games.roblox.com/v1/games/{universe_id}/user-votes".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "Voting_VoteGame",
    }

    if isinstance(body, UserGameVoteRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UserGameVoteRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UserGameVoteRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UserGameVoteRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> ApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = ApiEmptyResponseModel.from_dict(response.text)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiEmptyResponseModel]:
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
    body: UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | Unset = UNSET,
) -> Response[ApiEmptyResponseModel]:
    """
    Args:
        universe_id (int):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEmptyResponseModel]
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
    body: UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | Unset = UNSET,
) -> ApiEmptyResponseModel | None:
    """
    Args:
        universe_id (int):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEmptyResponseModel
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
    body: UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | Unset = UNSET,
) -> Response[ApiEmptyResponseModel]:
    """
    Args:
        universe_id (int):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEmptyResponseModel]
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
    body: UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | UserGameVoteRequest | Unset = UNSET,
) -> ApiEmptyResponseModel | None:
    """
    Args:
        universe_id (int):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):
        body (UserGameVoteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
