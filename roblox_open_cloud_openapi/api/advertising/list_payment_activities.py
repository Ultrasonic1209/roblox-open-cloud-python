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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.billing:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


import datetime

from ...models.error_envelope import ErrorEnvelope
from ...models.list_payment_activities_ledger import ListPaymentActivitiesLedger
from ...models.list_payment_activities_response import ListPaymentActivitiesResponse
from ...models.list_payment_activities_type import ListPaymentActivitiesType
from ...types import Unset


def _get_kwargs(
    id: str,
    *,
    ledger: ListPaymentActivitiesLedger,
    type_: ListPaymentActivitiesType | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ledger = ledger.value
    params["ledger"] = json_ledger

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/billing-accounts/{id}/payment-activities".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ListPaymentActivitiesResponse | None:
    if response.status_code == 200:
        response_200 = ListPaymentActivitiesResponse.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ListPaymentActivitiesResponse]:
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
    ledger: ListPaymentActivitiesLedger,
    type_: ListPaymentActivitiesType | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListPaymentActivitiesResponse]:
    """List scoped payment activity

     Lists one ledger, newest first. AD_CREDIT includes the source transaction type and initiator when
    available. CARD charge rows include the latest associated card settlement time when available. CARD
    requires type=CHARGE or type=REFUND. CHARGE and AD_CREDIT use cursor pagination; filtered pages can
    be short or empty and still have a nextPageToken. REFUND requires startTime (inclusive) and endTime
    (exclusive), returns complete results without pagination, and rejects ranges containing more than
    100 refund requests, including non-card requests. Requests without payment details are retained;
    known non-card payments are excluded.

    Args:
        id (str):
        ledger (ListPaymentActivitiesLedger):
        type_ (ListPaymentActivitiesType | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListPaymentActivitiesResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        ledger=ledger,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    ledger: ListPaymentActivitiesLedger,
    type_: ListPaymentActivitiesType | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListPaymentActivitiesResponse | None:
    """List scoped payment activity

     Lists one ledger, newest first. AD_CREDIT includes the source transaction type and initiator when
    available. CARD charge rows include the latest associated card settlement time when available. CARD
    requires type=CHARGE or type=REFUND. CHARGE and AD_CREDIT use cursor pagination; filtered pages can
    be short or empty and still have a nextPageToken. REFUND requires startTime (inclusive) and endTime
    (exclusive), returns complete results without pagination, and rejects ranges containing more than
    100 refund requests, including non-card requests. Requests without payment details are retained;
    known non-card payments are excluded.

    Args:
        id (str):
        ledger (ListPaymentActivitiesLedger):
        type_ (ListPaymentActivitiesType | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListPaymentActivitiesResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        ledger=ledger,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    ledger: ListPaymentActivitiesLedger,
    type_: ListPaymentActivitiesType | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListPaymentActivitiesResponse]:
    """List scoped payment activity

     Lists one ledger, newest first. AD_CREDIT includes the source transaction type and initiator when
    available. CARD charge rows include the latest associated card settlement time when available. CARD
    requires type=CHARGE or type=REFUND. CHARGE and AD_CREDIT use cursor pagination; filtered pages can
    be short or empty and still have a nextPageToken. REFUND requires startTime (inclusive) and endTime
    (exclusive), returns complete results without pagination, and rejects ranges containing more than
    100 refund requests, including non-card requests. Requests without payment details are retained;
    known non-card payments are excluded.

    Args:
        id (str):
        ledger (ListPaymentActivitiesLedger):
        type_ (ListPaymentActivitiesType | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListPaymentActivitiesResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        ledger=ledger,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    ledger: ListPaymentActivitiesLedger,
    type_: ListPaymentActivitiesType | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListPaymentActivitiesResponse | None:
    """List scoped payment activity

     Lists one ledger, newest first. AD_CREDIT includes the source transaction type and initiator when
    available. CARD charge rows include the latest associated card settlement time when available. CARD
    requires type=CHARGE or type=REFUND. CHARGE and AD_CREDIT use cursor pagination; filtered pages can
    be short or empty and still have a nextPageToken. REFUND requires startTime (inclusive) and endTime
    (exclusive), returns complete results without pagination, and rejects ranges containing more than
    100 refund requests, including non-card requests. Requests without payment details are retained;
    known non-card payments are excluded.

    Args:
        id (str):
        ledger (ListPaymentActivitiesLedger):
        type_ (ListPaymentActivitiesType | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListPaymentActivitiesResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            ledger=ledger,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
