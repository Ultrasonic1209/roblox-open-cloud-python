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

from ...models.roblox_groups_api_get_social_link_response import RobloxGroupsApiGetSocialLinkResponse


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/social-links".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/cloud/v2/groups/{group_id}",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#Cloud_GetGroup",
                }
            ],
        },
        "openapi-id": "get_v1_groups_groupId_social-links",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGetSocialLinkResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGetSocialLinkResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiGetSocialLinkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__social_links"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGetSocialLinkResponse]:
    """Get social link data associated with a group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGetSocialLinkResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__social_links"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGetSocialLinkResponse | None:
    """Get social link data associated with a group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGetSocialLinkResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__social_links"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGetSocialLinkResponse]:
    """Get social link data associated with a group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGetSocialLinkResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__social_links"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGetSocialLinkResponse | None:
    """Get social link data associated with a group

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGetSocialLinkResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
