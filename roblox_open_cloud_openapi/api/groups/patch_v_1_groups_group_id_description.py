import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_groups_api_group_description_response import RobloxGroupsApiGroupDescriptionResponse
from ...models.roblox_groups_api_update_group_description_request import RobloxGroupsApiUpdateGroupDescriptionRequest


def _get_kwargs(
    group_id: int,
    *,
    body: RobloxGroupsApiUpdateGroupDescriptionRequest | RobloxGroupsApiUpdateGroupDescriptionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/description".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-groups/v1/groups/{groupId}/description",
                    "httpMethod": "PATCH",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#patch_legacy_groups_v1_groups__groupId__description",
                }
            ],
        },
        "openapi-id": "patch_v1_groups_groupId_description",
    }

    if isinstance(body, RobloxGroupsApiUpdateGroupDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiUpdateGroupDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupDescriptionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupDescriptionResponse.from_dict(response.json())

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
) -> Response[Any | RobloxGroupsApiGroupDescriptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__description"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupDescriptionRequest | RobloxGroupsApiUpdateGroupDescriptionRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupDescriptionResponse]:
    """Updates the groups description

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupDescriptionResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__description"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupDescriptionRequest | RobloxGroupsApiUpdateGroupDescriptionRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupDescriptionResponse | None:
    """Updates the groups description

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupDescriptionResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__description"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupDescriptionRequest | RobloxGroupsApiUpdateGroupDescriptionRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupDescriptionResponse]:
    """Updates the groups description

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupDescriptionResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__description"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdateGroupDescriptionRequest | RobloxGroupsApiUpdateGroupDescriptionRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupDescriptionResponse | None:
    """Updates the groups description

    Args:
        group_id (int):
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group
        body (RobloxGroupsApiUpdateGroupDescriptionRequest): A request model for setting a
            description for the group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupDescriptionResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
