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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'ownership-transfer:read', 'targetResourceSpecifier': '', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_latest_transfer_request import GetLatestTransferRequest
from ...models.hold import Hold
from ...models.ownership_transfer_api_error_response import OwnershipTransferApiErrorResponse
from ...types import Unset


def _get_kwargs(
    *,
    body: GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ownership-transfer/v1/transfers/resource",
    }

    if isinstance(body, GetLatestTransferRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, GetLatestTransferRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, GetLatestTransferRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, GetLatestTransferRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Hold | OwnershipTransferApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = Hold.from_dict(response.json())

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
) -> Response[Hold | OwnershipTransferApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | Unset = UNSET,
) -> Response[Hold | OwnershipTransferApiErrorResponse]:
    """
    Args:
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Hold | OwnershipTransferApiErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | Unset = UNSET,
) -> Hold | OwnershipTransferApiErrorResponse | None:
    """
    Args:
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Hold | OwnershipTransferApiErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | Unset = UNSET,
) -> Response[Hold | OwnershipTransferApiErrorResponse]:
    """
    Args:
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Hold | OwnershipTransferApiErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | GetLatestTransferRequest
    | Unset = UNSET,
) -> Hold | OwnershipTransferApiErrorResponse | None:
    """
    Args:
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):
        body (GetLatestTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Hold | OwnershipTransferApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
