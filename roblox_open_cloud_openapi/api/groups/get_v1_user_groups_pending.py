import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_web_api_models_api_array_response_roblox_groups_api_group_detail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse,
)


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/user/groups/pending",
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-groups/v1/user/groups/pending",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#get_legacy_groups_v1_user_groups_pending",
                }
            ],
        },
        "openapi-id": "get_v1_user_groups_pending",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_user_groups_pending"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse]:
    """Gets groups that the authenticated user has requested to join

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_user_groups_pending"
)
def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse | None:
    """Gets groups that the authenticated user has requested to join

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_user_groups_pending"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse]:
    """Gets groups that the authenticated user has requested to join

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_user_groups_pending"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse | None:
    """Gets groups that the authenticated user has requested to join

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
