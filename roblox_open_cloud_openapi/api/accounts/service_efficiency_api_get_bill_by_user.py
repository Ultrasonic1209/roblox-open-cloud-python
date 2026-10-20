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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'extended-services:read', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.bill_details_response import BillDetailsResponse
from ...types import Unset


def _get_kwargs(
    user_id: int,
    *,
    bill_id: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    date: int | Unset = UNSET,
    latest: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["billId"] = bill_id

    params["year"] = year

    params["month"] = month

    params["date"] = date

    params["latest"] = latest

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/service-efficiency-api/v1/bills/users/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillDetailsResponse | None:
    if response.status_code == 200:
        response_200 = BillDetailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    bill_id: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    date: int | Unset = UNSET,
    latest: bool | Unset = False,
) -> Response[Any | BillDetailsResponse]:
    """Operation to Get Billing Statement for user owned account.

    Args:
        user_id (int):
        bill_id (str | Unset):
        year (int | Unset):
        month (int | Unset):
        date (int | Unset):
        latest (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillDetailsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bill_id=bill_id,
        year=year,
        month=month,
        date=date,
        latest=latest,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    bill_id: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    date: int | Unset = UNSET,
    latest: bool | Unset = False,
) -> Any | BillDetailsResponse | None:
    """Operation to Get Billing Statement for user owned account.

    Args:
        user_id (int):
        bill_id (str | Unset):
        year (int | Unset):
        month (int | Unset):
        date (int | Unset):
        latest (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillDetailsResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        bill_id=bill_id,
        year=year,
        month=month,
        date=date,
        latest=latest,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    bill_id: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    date: int | Unset = UNSET,
    latest: bool | Unset = False,
) -> Response[Any | BillDetailsResponse]:
    """Operation to Get Billing Statement for user owned account.

    Args:
        user_id (int):
        bill_id (str | Unset):
        year (int | Unset):
        month (int | Unset):
        date (int | Unset):
        latest (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillDetailsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bill_id=bill_id,
        year=year,
        month=month,
        date=date,
        latest=latest,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    bill_id: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    date: int | Unset = UNSET,
    latest: bool | Unset = False,
) -> Any | BillDetailsResponse | None:
    """Operation to Get Billing Statement for user owned account.

    Args:
        user_id (int):
        bill_id (str | Unset):
        year (int | Unset):
        month (int | Unset):
        date (int | Unset):
        latest (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillDetailsResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            bill_id=bill_id,
            year=year,
            month=month,
            date=date,
            latest=latest,
        )
    ).parsed
