from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_relationships_request import RobloxGroupsApiRelationshipsRequest
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    group_relationship_type: str,
    *,
    body: RobloxGroupsApiRelationshipsRequest | RobloxGroupsApiRelationshipsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/relationships/{group_relationship_type}/requests".format(
            group_id=quote(str(group_id), safe=""),
            group_relationship_type=quote(str(group_relationship_type), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_groups_groupId_relationships_groupRelationshipType_requests",
    }

    if isinstance(body, RobloxGroupsApiRelationshipsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiRelationshipsRequest):
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
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiRelationshipsRequest | RobloxGroupsApiRelationshipsRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Batch accepts group affiliate requests

    Args:
        group_id (int):
        group_relationship_type (str):
        body (RobloxGroupsApiRelationshipsRequest):
        body (RobloxGroupsApiRelationshipsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiRelationshipsRequest | RobloxGroupsApiRelationshipsRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Batch accepts group affiliate requests

    Args:
        group_id (int):
        group_relationship_type (str):
        body (RobloxGroupsApiRelationshipsRequest):
        body (RobloxGroupsApiRelationshipsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiRelationshipsRequest | RobloxGroupsApiRelationshipsRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Batch accepts group affiliate requests

    Args:
        group_id (int):
        group_relationship_type (str):
        body (RobloxGroupsApiRelationshipsRequest):
        body (RobloxGroupsApiRelationshipsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiRelationshipsRequest | RobloxGroupsApiRelationshipsRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Batch accepts group affiliate requests

    Args:
        group_id (int):
        group_relationship_type (str):
        body (RobloxGroupsApiRelationshipsRequest):
        body (RobloxGroupsApiRelationshipsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            group_relationship_type=group_relationship_type,
            client=client,
            body=body,
        )
    ).parsed
