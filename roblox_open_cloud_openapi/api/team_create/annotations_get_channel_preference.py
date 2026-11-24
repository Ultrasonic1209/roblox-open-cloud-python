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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000}}, 'x-roblox-scopes': [{'name': 'universe.place:read', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.channel_preference_response import ChannelPreferenceResponse
from ...models.operation_error_response import OperationErrorResponse
from ...types import Unset


def _get_kwargs(
    *,
    channel_id: str | Unset = UNSET,
    place_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["channelId"] = channel_id

    params["placeId"] = place_id

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/place-annotations-service/v1/get-channel-preference",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChannelPreferenceResponse | OperationErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChannelPreferenceResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OperationErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OperationErrorResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChannelPreferenceResponse | OperationErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    place_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[ChannelPreferenceResponse | OperationErrorResponse]:
    """
    Args:
        channel_id (str | Unset):
        place_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelPreferenceResponse | OperationErrorResponse]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        place_id=place_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    place_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> ChannelPreferenceResponse | OperationErrorResponse | None:
    """
    Args:
        channel_id (str | Unset):
        place_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelPreferenceResponse | OperationErrorResponse
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        place_id=place_id,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    place_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> Response[ChannelPreferenceResponse | OperationErrorResponse]:
    """
    Args:
        channel_id (str | Unset):
        place_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelPreferenceResponse | OperationErrorResponse]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        place_id=place_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: str | Unset = UNSET,
    place_id: int | Unset = UNSET,
    user_id: int | Unset = UNSET,
) -> ChannelPreferenceResponse | OperationErrorResponse | None:
    """
    Args:
        channel_id (str | Unset):
        place_id (int | Unset):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelPreferenceResponse | OperationErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            place_id=place_id,
            user_id=user_id,
        )
    ).parsed
