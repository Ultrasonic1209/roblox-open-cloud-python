from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_groups_group_basic_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    group_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupName"] = group_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/search/lookup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse.from_dict(
            response.json()
        )

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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_name: str,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse]:
    """Looks up groups by a name. Prioritizes an exact match as the first result.

     Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for
    search pages.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_name: str,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse | None:
    """Looks up groups by a name. Prioritizes an exact match as the first result.

     Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for
    search pages.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse
    """

    return sync_detailed(
        client=client,
        group_name=group_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_name: str,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse]:
    """Looks up groups by a name. Prioritizes an exact match as the first result.

     Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for
    search pages.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_name: str,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse | None:
    """Looks up groups by a name. Prioritizes an exact match as the first result.

     Should only be used for direct lookups where a user is inputting a group name, shouldn't be used for
    search pages.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesGroupsGroupBasicResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_name=group_name,
        )
    ).parsed
