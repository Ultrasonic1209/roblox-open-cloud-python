import sys
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_authentication_api_models_request_logout_from_all_sessions_and_reauthenticate_request import (
    RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/logoutfromallsessionsandreauthenticate",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

        return response_200

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_logoutfromallsessionsandreauthenticate"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Logs out user from all other sessions.

    Args:
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_logoutfromallsessionsandreauthenticate"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Logs out user from all other sessions.

    Args:
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_logoutfromallsessionsandreauthenticate"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Logs out user from all other sessions.

    Args:
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_logoutfromallsessionsandreauthenticate"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Logs out user from all other sessions.

    Args:
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):
        body (RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
