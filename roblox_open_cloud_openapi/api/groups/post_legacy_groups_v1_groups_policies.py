from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_group_policies_response import RobloxGroupsApiGroupPoliciesResponse
from ...models.roblox_groups_api_group_policy_request import RobloxGroupsApiGroupPolicyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxGroupsApiGroupPolicyRequest | RobloxGroupsApiGroupPolicyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legacy-groups/v1/groups/policies",
        "openapi-extensions": {
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-scopes": [{"name": "legacy-group:manage"}],
        },
        "openapi-id": "post_legacy-groups_v1_groups_policies",
    }

    if isinstance(body, RobloxGroupsApiGroupPolicyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiGroupPolicyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupPoliciesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupPoliciesResponse.from_dict(response.json())

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
) -> Response[Any | RobloxGroupsApiGroupPoliciesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiGroupPolicyRequest | RobloxGroupsApiGroupPolicyRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupPoliciesResponse]:
    """Gets group policy info used for compliance.

    Args:
        body (RobloxGroupsApiGroupPolicyRequest):
        body (RobloxGroupsApiGroupPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupPoliciesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiGroupPolicyRequest | RobloxGroupsApiGroupPolicyRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupPoliciesResponse | None:
    """Gets group policy info used for compliance.

    Args:
        body (RobloxGroupsApiGroupPolicyRequest):
        body (RobloxGroupsApiGroupPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupPoliciesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiGroupPolicyRequest | RobloxGroupsApiGroupPolicyRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupPoliciesResponse]:
    """Gets group policy info used for compliance.

    Args:
        body (RobloxGroupsApiGroupPolicyRequest):
        body (RobloxGroupsApiGroupPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupPoliciesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiGroupPolicyRequest | RobloxGroupsApiGroupPolicyRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupPoliciesResponse | None:
    """Gets group policy info used for compliance.

    Args:
        body (RobloxGroupsApiGroupPolicyRequest):
        body (RobloxGroupsApiGroupPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupPoliciesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
