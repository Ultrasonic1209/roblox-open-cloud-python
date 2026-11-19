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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.billing:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.error_envelope import ErrorEnvelope
from ...models.list_billing_accounts_response import ListBillingAccountsResponse
from ...types import Unset


def _get_kwargs(
    *,
    group_id: str | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/billing-accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ListBillingAccountsResponse | None:
    if response.status_code == 200:
        response_200 = ListBillingAccountsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ListBillingAccountsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListBillingAccountsResponse]:
    """List billing accounts

     Lists the billing accounts owned by the authenticated user, or by the group in groupId. Each account
    includes its type, status, time zone, create/update timestamps, creator, and funding state
    (paymentStatus, supportedPaymentTypes, balances, paymentMethods). Group accounts support only
    ADS_CREDIT. Funding state belongs to the account, not to any experience, so this response alone
    answers whether each account can pay for campaigns; GET /campaign-options with universeId only
    narrows which of these accounts a campaign for that experience can use. Results are paginated with a
    cursor (pageToken).

    Args:
        group_id (str | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListBillingAccountsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListBillingAccountsResponse | None:
    """List billing accounts

     Lists the billing accounts owned by the authenticated user, or by the group in groupId. Each account
    includes its type, status, time zone, create/update timestamps, creator, and funding state
    (paymentStatus, supportedPaymentTypes, balances, paymentMethods). Group accounts support only
    ADS_CREDIT. Funding state belongs to the account, not to any experience, so this response alone
    answers whether each account can pay for campaigns; GET /campaign-options with universeId only
    narrows which of these accounts a campaign for that experience can use. Results are paginated with a
    cursor (pageToken).

    Args:
        group_id (str | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListBillingAccountsResponse
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListBillingAccountsResponse]:
    """List billing accounts

     Lists the billing accounts owned by the authenticated user, or by the group in groupId. Each account
    includes its type, status, time zone, create/update timestamps, creator, and funding state
    (paymentStatus, supportedPaymentTypes, balances, paymentMethods). Group accounts support only
    ADS_CREDIT. Funding state belongs to the account, not to any experience, so this response alone
    answers whether each account can pay for campaigns; GET /campaign-options with universeId only
    narrows which of these accounts a campaign for that experience can use. Results are paginated with a
    cursor (pageToken).

    Args:
        group_id (str | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListBillingAccountsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListBillingAccountsResponse | None:
    """List billing accounts

     Lists the billing accounts owned by the authenticated user, or by the group in groupId. Each account
    includes its type, status, time zone, create/update timestamps, creator, and funding state
    (paymentStatus, supportedPaymentTypes, balances, paymentMethods). Group accounts support only
    ADS_CREDIT. Funding state belongs to the account, not to any experience, so this response alone
    answers whether each account can pay for campaigns; GET /campaign-options with universeId only
    narrows which of these accounts a campaign for that experience can use. Results are paginated with a
    cursor (pageToken).

    Args:
        group_id (str | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListBillingAccountsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
