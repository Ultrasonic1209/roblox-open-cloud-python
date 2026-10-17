from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

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
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_account_settings_api_trade_privacy_update_response import (
    RobloxAccountSettingsApiTradePrivacyUpdateResponse,
)
from ...models.roblox_account_settings_api_update_trade_privacy_request import (
    RobloxAccountSettingsApiUpdateTradePrivacyRequest,
)


def _get_kwargs(
    *,
    body: RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://accountsettings.roblox.com/v1/trade-privacy",
    }

    if isinstance(body, RobloxAccountSettingsApiUpdateTradePrivacyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAccountSettingsApiUpdateTradePrivacyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAccountSettingsApiTradePrivacyUpdateResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse]:
    """Updates a user's trade privacy setting

    Args:
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse]
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
    body: RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | Unset = UNSET,
) -> Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse | None:
    """Updates a user's trade privacy setting

    Args:
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse]:
    """Updates a user's trade privacy setting

    Args:
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | RobloxAccountSettingsApiUpdateTradePrivacyRequest
    | Unset = UNSET,
) -> Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse | None:
    """Updates a user's trade privacy setting

    Args:
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update
        body (RobloxAccountSettingsApiUpdateTradePrivacyRequest): Request model for trade privacy
            setting update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiTradePrivacyUpdateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
