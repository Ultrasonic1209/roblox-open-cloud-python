import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_restriction import UserRestriction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    place_id: str,
    user_restriction_id: str,
    *,
    body: UserRestriction,
    update_mask: str | Unset = UNSET,
    idempotency_key_key: str | Unset = UNSET,
    idempotency_key_first_sent: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params["idempotencyKey.key"] = idempotency_key_key

    json_idempotency_key_first_sent: str | Unset = UNSET
    if not isinstance(idempotency_key_first_sent, Unset):
        json_idempotency_key_first_sent = idempotency_key_first_sent.isoformat()
    params["idempotencyKey.firstSent"] = json_idempotency_key_first_sent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            user_restriction_id=quote(str(user_restriction_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "User Restrictions are subject to the additional rate limits, applied per universe\n\n* Get User Restriction: 50 req/s\n* List User Restrictions: 50 req/s\n* Update User Restrictions: 10 req/s\n* List User Restriction Logs: 50 req/s\n\nAdditionally, we impose the following rate limit for the same user within a universe:\n\n* Update User Restriction: 2 req/min\n\nFor example, Update User Restriction may not be called for user 123 more than twice every minute.",
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 150},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 30},
                },
                "x-roblox-scopes": [{"name": "universe.user-restriction:write"}],
                "x-roblox-docs": {
                    "category": "Users and groups",
                    "methodProperties": {"scopes": ["universe.user-restriction:write"]},
                    "resource": {"$ref": "#/components/schemas/UserRestriction", "name": "UserRestriction"},
                },
                "x-roblox-stability": "BETA",
            },
            "openapi-id": "Cloud_UpdateUserRestriction__Using_Universes_Places",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> UserRestriction | None:
    if response.status_code == 200:
        response_200 = UserRestriction.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[UserRestriction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    place_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
    body: UserRestriction,
    update_mask: str | Unset = UNSET,
    idempotency_key_key: str | Unset = UNSET,
    idempotency_key_first_sent: datetime.datetime | Unset = UNSET,
) -> Response[UserRestriction]:
    """Update User Restriction

     Update the user restriction.

    Args:
        universe_id (str):
        place_id (str):
        user_restriction_id (str):
        update_mask (str | Unset):
        idempotency_key_key (str | Unset):
        idempotency_key_first_sent (datetime.datetime | Unset):  Example: 2023-07-05T12:34:56Z.
        body (UserRestriction): Represents a restriction on a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserRestriction]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        user_restriction_id=user_restriction_id,
        body=body,
        update_mask=update_mask,
        idempotency_key_key=idempotency_key_key,
        idempotency_key_first_sent=idempotency_key_first_sent,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
    body: UserRestriction,
    update_mask: str | Unset = UNSET,
    idempotency_key_key: str | Unset = UNSET,
    idempotency_key_first_sent: datetime.datetime | Unset = UNSET,
) -> UserRestriction | None:
    """Update User Restriction

     Update the user restriction.

    Args:
        universe_id (str):
        place_id (str):
        user_restriction_id (str):
        update_mask (str | Unset):
        idempotency_key_key (str | Unset):
        idempotency_key_first_sent (datetime.datetime | Unset):  Example: 2023-07-05T12:34:56Z.
        body (UserRestriction): Represents a restriction on a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserRestriction
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        user_restriction_id=user_restriction_id,
        client=client,
        body=body,
        update_mask=update_mask,
        idempotency_key_key=idempotency_key_key,
        idempotency_key_first_sent=idempotency_key_first_sent,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
    body: UserRestriction,
    update_mask: str | Unset = UNSET,
    idempotency_key_key: str | Unset = UNSET,
    idempotency_key_first_sent: datetime.datetime | Unset = UNSET,
) -> Response[UserRestriction]:
    """Update User Restriction

     Update the user restriction.

    Args:
        universe_id (str):
        place_id (str):
        user_restriction_id (str):
        update_mask (str | Unset):
        idempotency_key_key (str | Unset):
        idempotency_key_first_sent (datetime.datetime | Unset):  Example: 2023-07-05T12:34:56Z.
        body (UserRestriction): Represents a restriction on a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserRestriction]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        user_restriction_id=user_restriction_id,
        body=body,
        update_mask=update_mask,
        idempotency_key_key=idempotency_key_key,
        idempotency_key_first_sent=idempotency_key_first_sent,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
    body: UserRestriction,
    update_mask: str | Unset = UNSET,
    idempotency_key_key: str | Unset = UNSET,
    idempotency_key_first_sent: datetime.datetime | Unset = UNSET,
) -> UserRestriction | None:
    """Update User Restriction

     Update the user restriction.

    Args:
        universe_id (str):
        place_id (str):
        user_restriction_id (str):
        update_mask (str | Unset):
        idempotency_key_key (str | Unset):
        idempotency_key_first_sent (datetime.datetime | Unset):  Example: 2023-07-05T12:34:56Z.
        body (UserRestriction): Represents a restriction on a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserRestriction
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            user_restriction_id=user_restriction_id,
            client=client,
            body=body,
            update_mask=update_mask,
            idempotency_key_key=idempotency_key_key,
            idempotency_key_first_sent=idempotency_key_first_sent,
        )
    ).parsed
