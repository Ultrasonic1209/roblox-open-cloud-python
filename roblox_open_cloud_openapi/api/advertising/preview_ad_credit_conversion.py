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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'ad.billing:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.ad_credit_conversion_preview import AdCreditConversionPreview
from ...models.error_envelope import ErrorEnvelope
from ...models.preview_ad_credit_conversion_request import PreviewAdCreditConversionRequest


def _get_kwargs(
    id: str,
    *,
    body: PreviewAdCreditConversionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/billing-accounts/{id}/ad-credit-conversions:preview".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdCreditConversionPreview | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AdCreditConversionPreview.from_dict(response.json())

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
) -> Response[AdCreditConversionPreview | ErrorEnvelope]:
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
    body: PreviewAdCreditConversionRequest,
) -> Response[AdCreditConversionPreview | ErrorEnvelope]:
    """Preview a Robux-to-ad-credit conversion

     Calculates the other side of a conversion from either a Robux amount or an ad credit amount, using
    the account's current Robux balances and rates. An amount the account cannot afford or outside the
    allowed range returns 200 with valid=false and a reason.

    Args:
        id (str):
        body (PreviewAdCreditConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdCreditConversionPreview | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewAdCreditConversionRequest,
) -> AdCreditConversionPreview | ErrorEnvelope | None:
    """Preview a Robux-to-ad-credit conversion

     Calculates the other side of a conversion from either a Robux amount or an ad credit amount, using
    the account's current Robux balances and rates. An amount the account cannot afford or outside the
    allowed range returns 200 with valid=false and a reason.

    Args:
        id (str):
        body (PreviewAdCreditConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdCreditConversionPreview | ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewAdCreditConversionRequest,
) -> Response[AdCreditConversionPreview | ErrorEnvelope]:
    """Preview a Robux-to-ad-credit conversion

     Calculates the other side of a conversion from either a Robux amount or an ad credit amount, using
    the account's current Robux balances and rates. An amount the account cannot afford or outside the
    allowed range returns 200 with valid=false and a reason.

    Args:
        id (str):
        body (PreviewAdCreditConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdCreditConversionPreview | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PreviewAdCreditConversionRequest,
) -> AdCreditConversionPreview | ErrorEnvelope | None:
    """Preview a Robux-to-ad-credit conversion

     Calculates the other side of a conversion from either a Robux amount or an ad credit amount, using
    the account's current Robux balances and rates. An amount the account cannot afford or outside the
    allowed range returns 200 with valid=false and a reason.

    Args:
        id (str):
        body (PreviewAdCreditConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdCreditConversionPreview | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
