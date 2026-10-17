from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': True}, 'x-roblox-scopes': [{'name': 'group:write', 'targetResourceSpecifier': ''}, {'name': 'group:write'}], 'x-roblox-docs': {'category': 'Users and groups', 'methodProperties': {'scopes': ['group:write']}, 'resource': {'$ref': '#/components/schemas/GroupJoinRequest', 'name': 'GroupJoinRequest'}}, 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 90}}}
"""


from ...models.accept_group_join_request_request import AcceptGroupJoinRequestRequest


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
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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

    response = client.get_httpx_client().request(
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
