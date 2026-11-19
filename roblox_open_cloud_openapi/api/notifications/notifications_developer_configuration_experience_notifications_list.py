from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 200}}, 'x-roblox-scopes': [{'name': 'universe.notification-string:read', 'targetResourceSpecifier': '', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.configure_experience_notifications_list_response import ConfigureExperienceNotificationsListResponse
from ...types import Unset


def _get_kwargs(
    *,
    universe_id: int | Unset = UNSET,
    count: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    previous: bool | Unset = UNSET,
    reverse_order: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["UniverseId"] = universe_id

    params["Count"] = count

    params["Cursor"] = cursor

    params["Previous"] = previous

    params["ReverseOrder"] = reverse_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/notifications/v1/developer-configuration/experience-notifications-list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfigureExperienceNotificationsListResponse | None:
    if response.status_code == 200:
        response_200 = ConfigureExperienceNotificationsListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConfigureExperienceNotificationsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    count: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    previous: bool | Unset = UNSET,
    reverse_order: bool | Unset = UNSET,
) -> Response[ConfigureExperienceNotificationsListResponse]:
    """
    Args:
        universe_id (int | Unset):
        count (int | Unset):
        cursor (str | Unset):
        previous (bool | Unset):
        reverse_order (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigureExperienceNotificationsListResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        count=count,
        cursor=cursor,
        previous=previous,
        reverse_order=reverse_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    count: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    previous: bool | Unset = UNSET,
    reverse_order: bool | Unset = UNSET,
) -> ConfigureExperienceNotificationsListResponse | None:
    """
    Args:
        universe_id (int | Unset):
        count (int | Unset):
        cursor (str | Unset):
        previous (bool | Unset):
        reverse_order (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigureExperienceNotificationsListResponse
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
        count=count,
        cursor=cursor,
        previous=previous,
        reverse_order=reverse_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    count: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    previous: bool | Unset = UNSET,
    reverse_order: bool | Unset = UNSET,
) -> Response[ConfigureExperienceNotificationsListResponse]:
    """
    Args:
        universe_id (int | Unset):
        count (int | Unset):
        cursor (str | Unset):
        previous (bool | Unset):
        reverse_order (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigureExperienceNotificationsListResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        count=count,
        cursor=cursor,
        previous=previous,
        reverse_order=reverse_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    count: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    previous: bool | Unset = UNSET,
    reverse_order: bool | Unset = UNSET,
) -> ConfigureExperienceNotificationsListResponse | None:
    """
    Args:
        universe_id (int | Unset):
        count (int | Unset):
        cursor (str | Unset):
        previous (bool | Unset):
        reverse_order (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigureExperienceNotificationsListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            count=count,
            cursor=cursor,
            previous=previous,
            reverse_order=reverse_order,
        )
    ).parsed
