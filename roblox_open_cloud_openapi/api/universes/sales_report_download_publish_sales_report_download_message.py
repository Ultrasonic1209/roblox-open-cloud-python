from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_response_message import HttpResponseMessage
from ...models.sales_report_download_request import SalesReportDownloadRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sales/sales-report-download",
    }

    if isinstance(body, SalesReportDownloadRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, SalesReportDownloadRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SalesReportDownloadRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, SalesReportDownloadRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HttpResponseMessage | None:
    if response.status_code == 200:
        response_200 = HttpResponseMessage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HttpResponseMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | Unset = UNSET,
) -> Response[HttpResponseMessage]:
    """
    Args:
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpResponseMessage]
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
    body: SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | Unset = UNSET,
) -> HttpResponseMessage | None:
    """
    Args:
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpResponseMessage
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | Unset = UNSET,
) -> Response[HttpResponseMessage]:
    """
    Args:
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpResponseMessage]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | SalesReportDownloadRequest
    | Unset = UNSET,
) -> HttpResponseMessage | None:
    """
    Args:
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):
        body (SalesReportDownloadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpResponseMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
