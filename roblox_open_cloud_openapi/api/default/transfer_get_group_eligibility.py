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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'ownership-transfer:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.ownership_transfer_api_error_response import OwnershipTransferApiErrorResponse
from ...models.transfer_get_group_eligibility_response_200 import TransferGetGroupEligibilityResponse200


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ownership-transfer/v1/transfers/resource/group/{group_id}/eligibility".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200 | None:
    if response.status_code == 200:
        response_200 = TransferGetGroupEligibilityResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OwnershipTransferApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OwnershipTransferApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OwnershipTransferApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = OwnershipTransferApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200]:
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
) -> Response[OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200]:
    """
    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200]
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
) -> OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200 | None:
    """
    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200]:
    """
    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200]
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
) -> OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200 | None:
    """
    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnershipTransferApiErrorResponse | TransferGetGroupEligibilityResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
