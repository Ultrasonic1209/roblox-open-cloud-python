from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accept_group_join_request_request import AcceptGroupJoinRequestRequest
from ...types import Response


def _get_kwargs(
    group_id: str,
    join_request_id: str,
    *,
    body: AcceptGroupJoinRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/groups/{group_id}/join-requests/{join_request_id}:accept".format(
            group_id=quote(str(group_id), safe=""),
            join_request_id=quote(str(join_request_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-scopes": [{"name": "group:write"}],
                "x-roblox-docs": {
                    "category": "Users and groups",
                    "methodProperties": {"scopes": ["group:write"]},
                    "resource": {"$ref": "#/components/schemas/GroupJoinRequest", "name": "GroupJoinRequest"},
                },
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 90},
                },
            },
            "openapi-id": "Cloud_AcceptGroupJoinRequest",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    join_request_id: str,
    *,
    client: AuthenticatedClient,
    body: AcceptGroupJoinRequestRequest,
) -> Response[Any]:
    """Accept Group Join Request

     Accepts a join request.

    Args:
        group_id (str):
        join_request_id (str):
        body (AcceptGroupJoinRequestRequest): A join request ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        join_request_id=join_request_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    join_request_id: str,
    *,
    client: AuthenticatedClient,
    body: AcceptGroupJoinRequestRequest,
) -> Response[Any]:
    """Accept Group Join Request

     Accepts a join request.

    Args:
        group_id (str):
        join_request_id (str):
        body (AcceptGroupJoinRequestRequest): A join request ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        join_request_id=join_request_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
