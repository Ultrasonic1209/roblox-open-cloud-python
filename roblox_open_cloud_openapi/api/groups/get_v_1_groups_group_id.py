import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_groups_api_group_detail_response import RobloxGroupsApiGroupDetailResponse


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/cloud/v2/groups/{group_id}",
                    "httpMethod": "GET",
                    "description": "For core group information.",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#Cloud_GetGroup",
                },
                {
                    "url": "https://apis.roblox.com/cloud/v2/groups/{group_id}/shout",
                    "httpMethod": "GET",
                    "description": "For the group shout information",
                },
            ],
        },
        "openapi-id": "get_v1_groups_groupId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiGroupDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId_"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupDetailResponse]:
    """Gets group information

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupDetailResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId_"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupDetailResponse | None:
    """Gets group information

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupDetailResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId_"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupDetailResponse]:
    """Gets group information

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupDetailResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId_"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupDetailResponse | None:
    """Gets group information

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupDetailResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
