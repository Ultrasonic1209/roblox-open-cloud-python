import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_groups_api_update_permissions_request import RobloxGroupsApiUpdatePermissionsRequest
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    group_id: int,
    role_set_id: int,
    *,
    body: RobloxGroupsApiUpdatePermissionsRequest | RobloxGroupsApiUpdatePermissionsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/groups/{group_id}/roles/{role_set_id}/permissions".format(
            group_id=quote(str(group_id), safe=""),
            role_set_id=quote(str(role_set_id), safe=""),
        ),
    }

    if isinstance(body, RobloxGroupsApiUpdatePermissionsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiUpdatePermissionsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__roles__roleSetId__permissions"
)
def sync_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdatePermissionsRequest | RobloxGroupsApiUpdatePermissionsRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Updates the permissions for a group's roleset. The authorized user must be the group owner.

    Args:
        group_id (int):
        role_set_id (int):
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__roles__roleSetId__permissions"
)
def sync(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdatePermissionsRequest | RobloxGroupsApiUpdatePermissionsRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Updates the permissions for a group's roleset. The authorized user must be the group owner.

    Args:
        group_id (int):
        role_set_id (int):
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        group_id=group_id,
        role_set_id=role_set_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__roles__roleSetId__permissions"
)
async def asyncio_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdatePermissionsRequest | RobloxGroupsApiUpdatePermissionsRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Updates the permissions for a group's roleset. The authorized user must be the group owner.

    Args:
        group_id (int):
        role_set_id (int):
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_patch_v1_groups__groupId__roles__roleSetId__permissions"
)
async def asyncio(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiUpdatePermissionsRequest | RobloxGroupsApiUpdatePermissionsRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Updates the permissions for a group's roleset. The authorized user must be the group owner.

    Args:
        group_id (int):
        role_set_id (int):
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.
        body (RobloxGroupsApiUpdatePermissionsRequest): A request model for updating a group's
            roleset's permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_set_id=role_set_id,
            client=client,
            body=body,
        )
    ).parsed
