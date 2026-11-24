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


from ...models.roblox_authentication_api_models_request_confirm_link_candidate_request import (
    RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest,
)
from ...models.roblox_authentication_api_models_response_external_identity_gateway_external_identity_access_response import (
    RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse,
)


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/link-candidate/confirm",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse]:
    """Links the sign-in to the account the user picked, then signs them in to it. With `createNew` it
    instead creates a new account, as sign-up does, and signs them in to that. The session comes back
    the
    way the sign-in's intent asks: a cookie for the web redirect, `RBX-Authentication-Ticket` for the
    app intents.

    Args:
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse]
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
    body: RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse | None:
    """Links the sign-in to the account the user picked, then signs them in to it. With `createNew` it
    instead creates a new account, as sign-up does, and signs them in to that. The session comes back
    the
    way the sign-in's intent asks: a cookie for the web redirect, `RBX-Authentication-Ticket` for the
    app intents.

    Args:
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse]:
    """Links the sign-in to the account the user picked, then signs them in to it. With `createNew` it
    instead creates a new account, as sign-up does, and signs them in to that. The session comes back
    the
    way the sign-in's intent asks: a cookie for the web redirect, `RBX-Authentication-Ticket` for the
    app intents.

    Args:
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse | None:
    """Links the sign-in to the account the user picked, then signs them in to it. With `createNew` it
    instead creates a new account, as sign-up does, and signs them in to that. The session comes back
    the
    way the sign-in's intent asks: a cookie for the web redirect, `RBX-Authentication-Ticket` for the
    app intents.

    Args:
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):
        body (RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityAccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
