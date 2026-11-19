from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_economy_api_models_get_group_snapshot_robux_response import (
    RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse,
)


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v1/groups/{group_id}/snapshot-robux".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse | None:
    if response.status_code == 200:
        response_200 = RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse]:
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
) -> Response[Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse]:
    """Gets the robux amount at old dev-ex rate for the specified group.
    The response field RobuxAt35 is the amount of robux a group has at the dev ex rate of $3.50 per 1000
    robux.

     Snapshot robux can only be retrieved for groups the authenticated user has permission to view group
    funds for.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse | None:
    """Gets the robux amount at old dev-ex rate for the specified group.
    The response field RobuxAt35 is the amount of robux a group has at the dev ex rate of $3.50 per 1000
    robux.

     Snapshot robux can only be retrieved for groups the authenticated user has permission to view group
    funds for.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse]:
    """Gets the robux amount at old dev-ex rate for the specified group.
    The response field RobuxAt35 is the amount of robux a group has at the dev ex rate of $3.50 per 1000
    robux.

     Snapshot robux can only be retrieved for groups the authenticated user has permission to view group
    funds for.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse | None:
    """Gets the robux amount at old dev-ex rate for the specified group.
    The response field RobuxAt35 is the amount of robux a group has at the dev ex rate of $3.50 per 1000
    robux.

     Snapshot robux can only be retrieved for groups the authenticated user has permission to view group
    funds for.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsGetGroupSnapshotRobuxResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
