from http import HTTPStatus
from typing import TYPE_CHECKING, Any
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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.error_envelope import ErrorEnvelope


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaigns/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | None:
    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope]:
    """Get a campaign

     Returns a single campaign, including its status (the lifecycle state you control: ACTIVE, PAUSED, or
    CANCELLED) and its deliveryStatus (whether it is currently serving: SERVING, IN_REVIEW, NOT_SERVING,
    or REJECTED). deliveryStatusReasons lists any reasons that affect delivery — for example why a
    campaign is not serving or was rejected, or that a serving campaign is still in its initial learning
    period. Returns 404 if the campaign does not exist or the caller can't manage it. A campaign owned
    by a group is readable by any member with advertising permission on the campaign's experience,
    without groupId.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | None:
    """Get a campaign

     Returns a single campaign, including its status (the lifecycle state you control: ACTIVE, PAUSED, or
    CANCELLED) and its deliveryStatus (whether it is currently serving: SERVING, IN_REVIEW, NOT_SERVING,
    or REJECTED). deliveryStatusReasons lists any reasons that affect delivery — for example why a
    campaign is not serving or was rejected, or that a serving campaign is still in its initial learning
    period. Returns 404 if the campaign does not exist or the caller can't manage it. A campaign owned
    by a group is readable by any member with advertising permission on the campaign's experience,
    without groupId.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope]:
    """Get a campaign

     Returns a single campaign, including its status (the lifecycle state you control: ACTIVE, PAUSED, or
    CANCELLED) and its deliveryStatus (whether it is currently serving: SERVING, IN_REVIEW, NOT_SERVING,
    or REJECTED). deliveryStatusReasons lists any reasons that affect delivery — for example why a
    campaign is not serving or was rejected, or that a serving campaign is still in its initial learning
    period. Returns 404 if the campaign does not exist or the caller can't manage it. A campaign owned
    by a group is readable by any member with advertising permission on the campaign's experience,
    without groupId.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | None:
    """Get a campaign

     Returns a single campaign, including its status (the lifecycle state you control: ACTIVE, PAUSED, or
    CANCELLED) and its deliveryStatus (whether it is currently serving: SERVING, IN_REVIEW, NOT_SERVING,
    or REJECTED). deliveryStatusReasons lists any reasons that affect delivery — for example why a
    campaign is not serving or was rejected, or that a serving campaign is still in its initial learning
    period. Returns 404 if the campaign does not exist or the caller can't manage it. A campaign owned
    by a group is readable by any member with advertising permission on the campaign's experience,
    without groupId.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
