from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organizations_service_api_error_response import OrganizationsServiceApiErrorResponse
from ...models.public_all_one_time_payouts_response_model import PublicAllOneTimePayoutsResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    user_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids: list[str] | Unset = UNSET
    if not isinstance(user_ids, Unset):
        json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/payouts/latest".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_groups_groupId_payouts_latest",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel | None:
    if response.status_code == 200:
        response_200 = PublicAllOneTimePayoutsResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[str] | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel]:
    """Gets the latest one-time payout for each requested user.

    Args:
        group_id (int):
        user_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_ids=user_ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[str] | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel | None:
    """Gets the latest one-time payout for each requested user.

    Args:
        group_id (int):
        user_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        user_ids=user_ids,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[str] | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel]:
    """Gets the latest one-time payout for each requested user.

    Args:
        group_id (int):
        user_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_ids=user_ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[str] | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel | None:
    """Gets the latest one-time payout for each requested user.

    Args:
        group_id (int):
        user_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | PublicAllOneTimePayoutsResponseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            user_ids=user_ids,
        )
    ).parsed
